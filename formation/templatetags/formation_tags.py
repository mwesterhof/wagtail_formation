from django.contrib.contenttypes.models import ContentType
from django.template import Library
from django.utils.html import mark_safe

from formation.utils import token_processor

register = Library()


@register.simple_tag(takes_context=True)
def debug(context):
    import ipdb;  # noqa
    ipdb.set_trace()


@register.simple_tag(takes_context=True)
def page_token(context, obj, block_id):
    try:
        token = context['form_token']
    except KeyError:
        obj_id = obj.id
        content_type_id = ContentType.objects.get_for_model(obj.__class__).id
        token = token_processor.generate_token(content_type_id, obj_id, block_id)
    return mark_safe(f'<input type="hidden" name="form_token" value="{token}" />')
