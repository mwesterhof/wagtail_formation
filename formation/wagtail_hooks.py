from wagtail import hooks
from wagtail.admin.viewsets.model import ModelViewSet

from .models import ReusableForm
from .views import ReusableFormChooserViewSet


class ReusableFormAdmin(ModelViewSet):
    model = ReusableForm
    menu_icon = 'form'


@hooks.register('register_admin_viewset')
def register_reusable_form_chooser_viewset():
    return ReusableFormChooserViewSet('form_chooser', url_prefix='form-chooser')
