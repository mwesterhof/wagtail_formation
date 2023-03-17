from django.core.mail import send_mail
from formation.blocks import (
    BaseFormBlock, BooleanFieldBlock, SubmitButtonBlock, TextFieldBlock
)
from wagtail.blocks import EmailBlock, RichTextBlock, StreamBlock
from wagtail.images.blocks import ImageChooserBlock


class MessageFormBlock(BaseFormBlock):
    send_emails_to = EmailBlock()

    fields = StreamBlock([
        ('text', TextFieldBlock()),
        ('check', BooleanFieldBlock()),
        ('submit_button', SubmitButtonBlock()),
        ('image', ImageChooserBlock()),
        ('rich_text', RichTextBlock(features=['bold', 'italic'])),
    ])

    mandatory_field_blocks = [
        ('name', TextFieldBlock),
        ('message', TextFieldBlock),
    ]

    def form_valid(self, value, form):
        name = form.cleaned_data['name']
        message = form.cleaned_data['message']

        email_to = value['send_emails_to']

        send_mail(
            "message sent",
            f"message from {name}: {message}",
            'no-reply@domain.com',
            [email_to],
        )
