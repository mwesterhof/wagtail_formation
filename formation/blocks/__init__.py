from wagtail.snippets.blocks import SnippetChooserBlock

from .forms import BaseFormBlock  # noqa
from .fields import *  # noqa


registered_forms = []


def reusable_form(name):
    def _register(form_block_class):
        registered_forms.append((name, form_block_class()))
        return form_block_class
    return _register


class ReusableFormChooserBlock(SnippetChooserBlock):
    def __init__(self, **kwargs):
        from formation.models import ReusableForm  # noqa
        kwargs['target_model'] = ReusableForm
        super().__init__(**kwargs)

    class Meta:
        icon = 'form'
        group = 'forms'
        template = 'formation/reusable_form.html'
