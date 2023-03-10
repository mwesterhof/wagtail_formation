from django.http import HttpResponse
from django.views.generic import View
from generic_chooser.views import ModelChooserViewSet

from formation.models import ReusableForm
from formation.utils import find_block_value, token_processor


class ProcessBlockFormView(View):
    def post(self, request, *args, **kwargs):
        form_token = request.POST['form_token']
        content_type_id, object_id, block_id = token_processor.unpack_token(form_token)
        block_value = find_block_value(content_type_id, object_id, block_id)
        block = block_value.block
        form = block.get_form_instance(block_value, request.POST)

        if form.is_valid():
            form_success = True
            block.form_valid(block_value, form)
        else:
            form_success = False
            block.form_invalid(block_value, form)

        result = block_value.render_as_block({
            'form_success': form_success,
            'form_data': request.POST,
            'form_token': form_token,
        })
        return HttpResponse(result)


class ReusableFormChooserViewSet(ModelChooserViewSet):
    model = ReusableForm
    fields = ['name', 'form_content']
