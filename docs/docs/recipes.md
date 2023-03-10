# Recipes

## Pass custom kwargs to field through block

```
    from formation.blocks import BaseFormBlock, IntegerFieldBlock


    class MyFormBlock(BaseFormBlock):
        fields = StreamBlock([
            ('age', IntegerFieldBlock(field_kwargs={'min_value': 0, 'max_value': 100}),
        ])
```

## Create custom field blocks

```
    from formation.blocks import BaseFieldBlock, IntegerFieldBlock
    from wagtail import blocks


    class BoundedIntegerFieldBlock(IntegerFieldBlock):
        min_value = blocks.IntegerBlock()
        max_value = blocks.IntegerBlock()

        def get_field(self, value, field_kwargs):
            return forms.IntegerField(
                label=value['label'],
                min_value=value['min_value'],
                max_value=value['max_value'],
                **field_kwargs
            )
```

## Override templates

Every block has its own unique template. There's two ways to override these.

1. **Override the template for a specific block subclass**

        class BoundedIntegerFieldBlock(IntegerFieldBlock):
            ...

            class Meta:
                template = 'myapp/blocks/fields/bounded_integer.html'


2. **Override the template for any occurence of a specific field**

It's possible to use standard django template overriding to replace any of the field templates completely. For this
reason, I recommend placing the `formation` app towards the end of your `INSTALLED_APPS`
