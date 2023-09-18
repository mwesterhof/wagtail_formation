from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.views.generic import View
from generic_chooser.views import ModelChooserViewSet

from formation.models import ReusableForm
from formation.utils import find_block_value, token_processor


def is_redirect(response):
    return isinstance(response, HttpResponseRedirect) or isinstance(response, HttpResponsePermanentRedirect)


class ProcessBlockFormView(View):
    def post(self, request, *args, **kwargs):
        form_token = request.POST['form_token']
        content_type_id, object_id, block_id = token_processor.unpack_token(form_token)
        block_value = find_block_value(content_type_id, object_id, block_id)
        block = block_value.block
        form = block.get_form_instance(block_value, request.POST, request.FILES)

        if form.is_valid():
            form_success = True
            block_response = block.form_valid(request, block_value, form)
        else:
            form_success = False
            block_response = block.form_invalid(request, block_value, form)

        if is_redirect(block_response):  # block form handler decided to bypass AJAX
            response = HttpResponse(block_response.url)
            response['formationReplace'] = 0
            return response

        result = block_value.render_as_block({
            'form_success': form_success,
            'form_data': request.POST,
            'form_token': form_token,
        })
        response = HttpResponse(result)
        response.headers['formationReplace'] = 1
        return response


class ReusableFormChooserViewSet(ModelChooserViewSet):
    model = ReusableForm
    fields = ['name', 'form_content']
