import uuid

from django import forms
from wagtail import blocks


class FieldBlockBase(blocks.StructBlock):
    is_field_block = True

    name = blocks.CharBlock()
    label = blocks.CharBlock()
    is_required = blocks.BooleanBlock(required=False, default=True)

    def __init__(self, *args, **kwargs):
        self.field_kwargs = kwargs.pop('field_kwargs', {})
        super().__init__(*args, **kwargs)

    def get_named_field(self, value):
        kwargs = self.field_kwargs.copy()
        kwargs['required'] = value['is_required']
        return value['name'], self.get_field(value, kwargs)

    def get_field(self, value, field_kwargs):
        return forms.Field(label=value['label'], required=value['is_required'], **field_kwargs)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        form = context['form']

        context.update({
            'errors': context['form'].errors.get(value['name']),
            'field_id': uuid.uuid4().hex,
            'field_value': form.data.get(value['name'], '')
        })
        return context

    class Meta:
        icon = 'edit'
        group = 'fields'


class TextFieldBlock(FieldBlockBase):
    def get_field(self, value, field_kwargs):
        return forms.CharField(label=value['label'], **field_kwargs)

    class Meta:
        template = 'formation/blocks/text_field.html'
        icon = 'openquote'


class TextareaFieldBlock(FieldBlockBase):
    def get_field(self, value, field_kwargs):
        return forms.CharField(label=value['label'], **field_kwargs)

    class Meta:
        template = 'formation/blocks/textarea_field.html'
        icon = 'openquote'


class IntegerFieldBlock(FieldBlockBase):
    def get_field(self, value, field_kwargs):
        return forms.IntegerField(label=value['label'], **field_kwargs)

    class Meta:
        template = 'formation/blocks/integer_field.html'
        icon = 'order'


class BooleanFieldBlock(FieldBlockBase):
    def get_field(self, value, field_kwargs):
        return forms.BooleanField(label=value['label'], **field_kwargs)

    class Meta:
        template = 'formation/blocks/boolean_field.html'
        icon = 'tick'


class ChoiceFieldBase(FieldBlockBase):
    options = blocks.ListBlock(
        blocks.StructBlock([
            ('name', blocks.CharBlock()),
            ('label', blocks.CharBlock()),
        ])
    )

    def get_field(self, value, field_kwargs):
        return forms.ChoiceField(
            label=value['label'], choices=[
                (option['name'], option['label'])
                for option in value['options']
            ], **field_kwargs
        )


class SubmitButtonBlock(blocks.StructBlock):
    button_text = blocks.CharBlock()

    class Meta:
        template = 'formation/blocks/submit_button.html'
        icon = 'resubmit'
        group = 'fields'


class SelectFieldBlock(ChoiceFieldBase):
    class Meta:
        template = 'formation/blocks/select_field.html'
        icon = 'tasks'


class RadioFieldBlock(ChoiceFieldBase):
    class Meta:
        template = 'formation/blocks/radio_field.html'
        icon = 'radio-empty'


class DateFieldBlock(FieldBlockBase):
    def get_field(self, value, field_kwargs):
        return forms.DateField(label=value['label'], **field_kwargs)

    class Meta:
        template = 'formation/blocks/date_field.html'
        icon = 'date'


class DateTimeFieldBlock(FieldBlockBase):
    def get_field(self, value, field_kwargs):
        return forms.DateTimeField(label=value['label'], **field_kwargs)

    class Meta:
        template = 'formation/blocks/datetime_field.html'
        icon = 'time'


class EmailFieldBlock(FieldBlockBase):
    def get_field(self, value, field_kwargs):
        return forms.EmailField(label=value['label'], **field_kwargs)

    class Meta:
        template = 'formation/blocks/email_field.html'
        icon = 'mail'


BASIC_FIELD_SPEC = [
    ('text', TextFieldBlock()),
    ('textarea', TextareaFieldBlock()),
    ('integer', IntegerFieldBlock()),
    ('select', SelectFieldBlock()),
    ('radio', RadioFieldBlock()),
]

FULL_FIELD_SPEC = BASIC_FIELD_SPEC + [
    ('boolean', BooleanFieldBlock()),
    ('date', DateFieldBlock()),
    ('datetime', DateTimeFieldBlock()),
    ('email', EmailFieldBlock()),
]
