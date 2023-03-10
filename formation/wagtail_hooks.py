from wagtail import hooks
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import ReusableForm
from .views import ReusableFormChooserViewSet


@modeladmin_register
class ReusableFormAdmin(ModelAdmin):
    model = ReusableForm
    menu_icon = 'form'


@hooks.register('register_admin_viewset')
def register_reusable_form_chooser_viewset():
    return ReusableFormChooserViewSet('form_chooser', url_prefix='form-chooser')
