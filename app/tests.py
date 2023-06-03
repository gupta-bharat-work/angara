from django.http import QueryDict
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TranslateAPITestCase(APITestCase):
    def test_valid_translation(self):
        params = QueryDict('', mutable=True)
        params.update({
            'source_lang': 'en',
            'target_lang': 'fr'
        })
        url = '{base_url}?{querystring}'.format(
            base_url=reverse('translate'),
            querystring=params.urlencode()
        )
        data = {
            'source_text': 'Hello',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['success'], True)
        self.assertIn('translation', response.data)

    def test_invalid_translation_missing_params(self):
        url = reverse('translate')
        data = {
            'source_text': 'Hello',
        }
        # Missing query params
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Invalid request/query parameters')
