# Advanced examples

## Conditionally bypass AJAX-based form handling

By default, formation handles all form posts through AJAX, and simply re-renders the content of the block without a new
page load.

Depending on the functionality of the form, this may not always be desirable. There are some scenarios it would be
better to send the visitor to a different URL, and have something more similar to the standard *success_url*
functonality in normal Django form handling. This can be handled using the *form_valid* and *form_invalid* functions on
a form block, where simply returning a redirect response will change the behavior:

```python
from django.http import HttpResponseRedirect
from formation.blocks import BaseFormBlock

from wagtail import blocks


class RedirectOnSuccessFormBlock(BaseFormBlock):
    success_url = blocks.CharBlock()

    ...

    def form_valid(self, value, form):
        return HttpResponseRedirect(value['success_url'])
```

The above example still handles invalid form posts in the default, AJAX-based way, but all successfull form posts now
redirect to a CMS-editable *success_url*

It's also possible to make this completely conditional:

```python
from django.http import HttpResponseRedirect
from formation.blocks import (
    BaseFormBlock, SubmitButtonBlock, TextFieldBlock
)

from wagtail import blocks


class TestFormBlock(BaseFormBlock):
    fields = blocks.StreamBlock([
        ('text', TextFieldBlock()),
        ('submit', SubmitButtonBlock()),
    ])

    mandatory_field_blocks = [
        ('message', TextFieldBlock),
    ]

    def form_valid(self, value, form):
        message = form.cleaned_data['message']
        if message.startswith('http://') or message.startswith('https://'):
            return HttpResponseRedirect(message)
        do_something_else_with(message)
```

In this example, a successfull form post can lead to both AJAX- and regular responses. The form handler JS provided
with formation handles these variations, and should be used as a basis when writing your own handler.
