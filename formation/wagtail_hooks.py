from wagtail.snippets.models import register_snippet

from .views import ReusableFormViewSet
from .blocks import registered_forms

if registered_forms:
    register_snippet(ReusableFormViewSet)


# @modeladmin_register
# class ReusableFormAdmin(ModelAdmin):
#     model = ReusableForm
#     menu_icon = 'form'
#
#
# @hooks.register('register_admin_viewset')
# def register_reusable_form_chooser_viewset():
#     return ReusableFormChooserViewSet('form_chooser', url_prefix='form-chooser')
