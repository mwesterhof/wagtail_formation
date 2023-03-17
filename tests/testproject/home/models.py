from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from .blocks import MessageFormBlock


class HomePage(Page):
    content = StreamField([
        ('message_form', MessageFormBlock()),
    ], use_json_field=False)

    content_panels = Page.content_panels + [
        FieldPanel('content')
    ]
