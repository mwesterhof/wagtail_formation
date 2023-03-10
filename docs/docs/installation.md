# Installation

Simply install the package with pip;

```
pip install wagtail_formation
```

Add the following to your `INSTALLED_APPS`, preferably at the end;

```
INSTALLED_APPS = [
    ...
    'formation',
    'generic_chooser',
]
```

Finally, make sure that the following is registered somewhere in your url config;

```
from formation.views import ProcessBlockFormView


urlpatterns = [
    ...
    path('process-block-form/', ProcessBlockFormView.as_view(), name='process-block-form'),
    ...
]
```

*(TODO: document the correct javascript setup)*
