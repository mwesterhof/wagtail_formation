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
from formation import urls as formation_urls


urlpatterns = [
    ...
    path("formation/", include(formation_urls)),  # of course, feel free to use any other URL
    ...
]
```

Forms should be posted through AJAX requests. You may implement this yourself, or rely on formation's example
implementation;

```
{% block extra_js %}
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/js-cookie@3.0.1/dist/js.cookie.min.js"></script>
<script src="{% static 'js/formation.js' %}"></script>
{% endblock extra_js %}
```
