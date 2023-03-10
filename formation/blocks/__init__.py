from django.utils.functional import cached_property
from wagtail.blocks import ChooserBlock

from .forms import BaseFormBlock  # noqa
from .fields import *  # noqa


registered_forms = []


def reusable_form(name):
    def _register(form_block_class):
        registered_forms.append((name, form_block_class()))
        return form_block_class
    return _register


class ReusableFormChooserBlock(ChooserBlock):
    @cached_property
    def target_model(self):
        from formation.models import ReusableForm  # noqa
        return ReusableForm

    @cached_property
    def widget(self):
        from formation.widgets import ReusableFormChooser  # noqa
        return ReusableFormChooser()

    def get_form_state(self, value):
        return self.widget.get_value_data(value)

    class Meta:
        icon = 'form'
        template = 'formation/reusable_form.html'
