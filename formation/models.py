from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import PreviewableMixin

from .blocks import registered_forms


class ReusableForm(PreviewableMixin, models.Model):
    name = models.CharField(max_length=200)
    form_content = StreamField(registered_forms, min_num=1, max_num=1, use_json_field=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('form_content'),
    ]

    def __str__(self):
        return self.name

    def get_preview_template(self, request, mode_name):
        return 'formation/admin/reusable_form_preview.html'
