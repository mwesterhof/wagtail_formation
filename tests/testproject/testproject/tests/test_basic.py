import re
import unittest

from django.test import Client
from django.urls import reverse

from home.models import HomePage


form_token_regex = b'name="form_token" value="([^"]+)"'

class TestTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.home = HomePage.objects.get()
        self.process_url = reverse('process-block-form')

    def get_form_token(self):
        response = self.client.get(self.home.url)
        form_token = re.search(form_token_regex, response.content).groups(0)[0].decode('utf-8')
        return form_token

    def test_page_works(self):
        response = self.client.get(self.home.url)
        self.assertEqual(response.status_code, 200)

    def test_valid_post(self):
        form_token = self.get_form_token()

        response = self.client.post(
            self.process_url,
            {'name': 'my-name', 'message': 'my-message', 'form_token': form_token}
        )
        self.assertTrue(response.context.get('form_success'))

    def test_missing_field(self):
        form_token = self.get_form_token()

        response = self.client.post(
            self.process_url,
            {'message': 'my-message', 'form_token': form_token}
        )
        self.assertFalse(response.context.get('form_success'))

