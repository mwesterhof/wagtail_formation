from django.urls import path
from formation.views import ProcessBlockFormView


urlpatterns = [
    path('process-block-form/', ProcessBlockFormView.as_view(), name='process-block-form'),
]
