from django import forms
from django.utils.translation import gettext as _
from wagtail.blocks.struct_block import StructBlockValidationError
from django.forms.utils import ErrorList
from wagtail import blocks

from ..utils import extract_elements_recursive


class BaseFormBlock(blocks.StructBlock):
    form_name = blocks.CharBlock()
    fields = blocks.StreamBlock([
    ])

    mandatory_field_blocks = []

    def clean(self, value):
        result = super().clean(value)
        error_list = []

        field_spec = self._get_field_spec(value)
        for name, block_type in self.mandatory_field_blocks:
            field = field_spec.get(name)
            found_block = getattr(field, 'block', None)

            if type(found_block) != block_type:
                error_list.append(
                    _("This form requires a %(block_type_name)s named \"%(name)s\" ") % {
                        'block_type_name': block_type.__name__,
                        'name': name,
                    }
                )
            elif not field['is_required']:
                error_list.append(
                    _("The %(block_type_name)s named \"%(name)s\" should be required ") % {
                        'block_type_name': block_type.__name__,
                        'name': name,
                    }
                )

        if error_list:
            errors = {'form_name': ErrorList(error_list)}
            raise StructBlockValidationError(errors)
        return result

    def _get_block_id(self, context):
        for name, value in context.items():
            if getattr(value, 'block', None) is self:
                return value.id

    def _get_field_spec(self, value):
        fields = self._get_fields(value)
        result = {}
        for field in fields:
            result[field['name']] = field

        return result

    def _get_form_class_name(cls):
        return getattr(cls, 'form_class_name', 'BlockForm')

    def _get_fields(cls, value):
        fields = value['fields']
        blocks = []

        def _input_block_check(element):
            return getattr(element.block, 'is_field_block', False)

        extract_elements_recursive(fields, blocks, _input_block_check, False)
        return blocks

    def _get_form_class(cls, value):
        blocks = cls._get_fields(value)

        return type(
            cls._get_form_class_name(),
            (forms.Form,),
            dict(
                [
                    element.block.get_named_field(element)
                    for element in blocks
                ]
            )
        )

    def get_form_instance(cls, value, data=None):
        form_class = cls._get_form_class(value)
        return form_class(data)

    def get_context(self, value, parent_context=None):
        self.id = self._get_block_id(parent_context)
        context = super().get_context(value, parent_context=parent_context)
        form_data = context.get('form_data', None)
        context.update({
            'form': self.get_form_instance(value, form_data),
        })
        context['self'].id = self.id
        return context

    def form_valid(self, value, form):
        return

    def form_invalid(self, value, form):
        return

    class Meta:
        template = 'formation/blocks/base_form.html'
        icon = 'form'
        group = 'forms'
