from django.utils.translation import gettext_lazy as _
from generic_chooser.widgets import AdminChooser

from .models import ReusableForm


class ReusableFormChooser(AdminChooser):
    choose_one_text = _("Choose a form")
    choose_another_text = _("Choose another form")
    model = ReusableForm
    choose_modal_url_name = 'form_chooser:choose'
    icon = 'form'
