# Basic example

We will look at an example of implementing a form with the following specifications:

* The form will ask for a name, message, and for agreement to terms and conditions
* Upon successfull form submit, the form will send an email
* The form may contain its 2 fields and submit button, in any order the cms user wants to put them
* The cms user can add richtext/image elements anywhere within the form, including between the fields
* The cms user provides the email address that any submissions for that specific form are sent to

In order to implement the form for use in wagtail pages, the developer can simply create a custom form class:

```
    from django.core.mail import send_mail
    from formation.blocks import (
        BaseFormBlock, BooleanFieldBlock, SubmitButtonBlock, TextFieldBlock
    )
    from wagtail.blocks import EmailBlock, RichTextBlock, StreamBlock
    from wagtail.images.blocks import ImageChooserBlock


    class MessageFormBlock(BaseFormBlock):
        send_emails_to = EmailBlock()
        ...
```

As this subclasses `BaseFormBlock`, we can simply override its `form_valid` method:

```
    class MessageFormBlock(BaseFormBlock):
        ...
        def form_valid(self, request, value, form):
            name = form.cleaned_data['name']
            message = forms.cleaned_data['message']

            email_to = value['send_emails_to']

            send_mail(
                "message sent",
                f"message from {name}: {message}",
                'no-reply@domain.com',
                [email_to],
            )
```

Next, we make sure that the form block can contain content, including its fields:

```
    class MessageFormBlock(BaseFormBlock):
        fields = StreamBlock([
            ('text', TextFieldBlock()),
            ('check', BooleanFieldBlock()),
            ('submit_button', SubmitButtonBlock()),
            ('image', ImageChooserBlock()),
            ('rich_text', RichTextBlock(features=['bold', 'italic'])),
        ])
        ...
```

As the `form_valid` method expects 2 fields to exist in the form, we can register them as mandatory:

```
    mandatory_field_blocks = [
        ('name', TextFieldBlock),
        ('message', TextFieldBlock),
    ]
```

This will ensure that the cms user will have to add fields with the above names and exact types.

This gives us the following implementation, finally:

```
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

        def form_valid(self, request, value, form):
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']

            email_to = value['send_emails_to']

            send_mail(
                "message sent",
                f"message from {name}: {message}",
                'no-reply@domain.com',
                [email_to],
            )
```
