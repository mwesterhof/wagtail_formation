from wagtail import hooks
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from .models import ReusableForm
from .views import ReusableFormChooserViewSet


class ReusableFormAdmin(SnippetViewSet):
    model = ReusableForm
    icon = "form"
    add_to_admin_menu = True
    list_display = ["name"]


@hooks.register('register_admin_viewset')
def register_reusable_form_chooser_viewset():
    return ReusableFormChooserViewSet('form_chooser', url_prefix='form-chooser')


register_snippet(ReusableFormAdmin)
