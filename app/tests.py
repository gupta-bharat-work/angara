from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

'''
# This test cases are written for Google Cloud Translation API

class TranslateAPITestCase(APITestCase):

    def test_single_word_translation(self):
        url = reverse('translate', args=['hello', 'en', 'fr'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['translation'], 'bonjour')

    def test_phrase_translation(self):
        url = reverse('translate', args=['How are you?', 'en', 'fr'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['translation'], 'Comment ça va ?')

    def test_paragraph_translation(self):
        source_text = 'Hello, how are you? I hope you\'re doing well.'
        expected_translation = 'Bonjour, comment ça va ? J\'espère que tu te portes bien.'
        url = reverse('translate', args=[source_text, 'en', 'fr'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['translation'], expected_translation)

    def test_missing_source_text(self):
        url = reverse('translate', args=[None, 'en', 'fr'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unsupported_language(self):
        url = reverse('translate', args=['hello', 'en', 'xyz'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_api_key(self):
        url = reverse('translate', args=['hello', 'en', 'fr'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def test_response_structure(self):
        url = reverse('translate', args=['hello', 'en', 'fr'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('translation', response.data)

'''


class TranslateAPITestCase(APITestCase):
    def test_valid_translation(self):
        url = reverse('translate')
        data = {
            'source_text': 'Hello',
            'source_lang': 'en',
            'target_lang': 'fr'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['success'], True)
        self.assertIn('translation', response.data)

    def test_invalid_translation_missing_params(self):
        url = reverse('translate')
        data = {
            'source_text': 'Hello',
            # Missing source_lang and target_lang
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['error'], 'Invalid request/query parameters')
