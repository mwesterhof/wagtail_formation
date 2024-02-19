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

Because marking form blocks as reusable in your code will affect a model definition in formation, you'll have to choose
a project folder to house formation migrations;

```
MIGRATION_MODULES = {
    'formation': 'formation_migrations',  # this can be any convenient location in your project
}
```

Because formation uses a generic chooser panel for reusable form blocks, it's possible to directly create the reusable
forms from this chooser. This will open a modal interface. If the reusable form relies on yet another chooser panel,
opening yet another modal isn't handled correctly by wagtail. In those cases, it's recommended to turn off the
ReusableForm creation from the chooser widget, using the following setting:

```
FORMATION_SHOW_REUSABLE_FORM_CREATE = False
```

Finally, make sure that the following is registered somewhere in your url config;

```
from formation import urls as formation_urls


urlpatterns = [
    ...
    path("formation/", include(formation_urls)),  # of course, feel free to use any other URL
    ...
]
```

Make sure to create missing migrations and run them.

Forms should be posted through AJAX requests. You may implement this yourself, or rely on formation's example
implementation;

```
{% block extra_js %}
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/js-cookie@3.0.1/dist/js.cookie.min.js"></script>
<script src="{% static 'js/formation.js' %}"></script>
{% endblock extra_js %}
```
