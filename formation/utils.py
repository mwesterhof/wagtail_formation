# TODO: investigate if it makes sense to just generate random key and iv
# this would invalidate a token open restart
from base64 import b64encode, b64decode
import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from django.contrib.contenttypes.models import ContentType
from wagtail.blocks import ListBlock, StreamBlock, StructBlock
from wagtail.fields import StreamField


class TokenProcessor:
    def __init__(self):
        key = os.urandom(32)
        self.iv = os.urandom(16)
        self.cipher = Cipher(algorithms.AES(key), modes.CBC(self.iv))

    def generate_token(self, content_type_id, object_id, block_id):
        content_ids = f'{content_type_id}:{object_id}'.ljust(11)
        to_encrypt = bytes(f'{content_ids}:{block_id}', 'utf-8')

        encryptor = self.cipher.encryptor()
        return str(
            b64encode(encryptor.update(to_encrypt) + encryptor.finalize()),
            'utf-8'
        )

    def unpack_token(self, token_encoded):
        token = b64decode(token_encoded)
        decryptor = self.cipher.decryptor()
        decrypted = decryptor.update(token) + decryptor.finalize()
        content_type_id, object_id, block_id = str(decrypted, 'utf-8').split(':')

        return int(content_type_id), int(object_id), block_id


token_processor = TokenProcessor()


def extract_elements_recursive(container, results, check_method, id_based=False):
    for i, element in enumerate(container):
        if hasattr(container, 'raw_data'):
            block_id = container.raw_data[i]['id']
        elif hasattr(container, 'bound_blocks'):
            block_id = container.bound_blocks[i].id

        if check_method(element):
            element = getattr(element, 'value', element)
            if id_based:
                results[block_id] = element
            else:
                results.append(element)
        elif isinstance(element.block, ListBlock) or isinstance(element.block, StreamBlock):
            extract_elements_recursive(element.value, results, check_method, id_based)
        elif isinstance(element.block, StructBlock):
            value = getattr(element, 'value', element)
            extract_elements_recursive([
                element for _, element in value.bound_blocks.items()
            ], results, check_method, id_based)


def find_block_value(content_type_id, object_id, block_id):
    obj = ContentType.objects.get(pk=content_type_id).model_class().objects.get(pk=object_id)

    fields = [
        getattr(obj, field.name)
        for field in obj._meta.fields
        if isinstance(field, StreamField)
    ]
    form_blocks = {}

    def _formblock_check(element):
        from formation.blocks import BaseFormBlock
        return isinstance(element.block, BaseFormBlock)

    for field in fields:
        extract_elements_recursive(field, form_blocks, _formblock_check, True)

    return form_blocks[block_id]
