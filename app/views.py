# import requests
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
from googletrans import Translator
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Translation


class TranslateAPIView(APIView):

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        try:
            source_text = request.data.get('source_text')
            source_lang = request.query_params.get('source_lang')
            target_lang = request.query_params.get('target_lang')

            if not source_text or not source_lang or not target_lang:
                return Response({'error': 'Invalid request/query parameters'}, status=400)

            # Create unique key in cache for each translation
            cache_key = f'{source_text}-{source_lang}-{target_lang}'

            # Check if translation exists in the cache
            translation_cache_obj = cache.get(cache_key)

            # Check if translation not exists in cache but in database
            translation_db_obj = Translation.objects.filter(
                source_text=source_text,
                source_lang=source_lang,
                target_lang=target_lang
            ).first()

            if translation_cache_obj:
                translation = translation_cache_obj

            elif translation_db_obj:
                translation = translation_db_obj.translation

            else:
                # Perform translation
                translation = self.translate(source_text, source_lang, target_lang)
                cache.set(cache_key, translation)

                # Store translation in the database
                Translation.objects.create(
                    source_text=source_text,
                    source_lang=source_lang,
                    target_lang=target_lang,
                    translation=translation
                )

            return Response({'success': True, 'translation': translation}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def translate(self, text, source_language, target_language):

        # This is the alternate approach to perform translation by using Google Translation API with API Key, currently
        # we are not having any billing account i.e. required to work with Google Cloud Translation API.

        '''
        api_key = 'AIzaSyAVVH5NFVSyVhSm_ejRhDzJcWwdme7iWzQ'
        url = f'https://translation.googleapis.com/language/translate/v2?key={api_key}'
        params = {
            'q': source_text,
            'source': source_lang,
            'target': target_lang,
        }
        response = requests.post(url, params=params)
        translation = response.json()['data']['translations'][0]['translatedText']
        '''

        # Set up the Google Translator
        translator = Translator()

        # Translate the text
        result = translator.translate(text, src=source_language, dest=target_language)

        translated_text = result.text
        return translated_text
