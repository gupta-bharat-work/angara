# Translation API

### **Versions**

**Python : 3.9.9**

**OS : Mac**

This is a REST API that provides translation services for words, phrases, and paragraphs. Google Cloud Translation API to perform the translations [code is included (#)] because of billing GCP account, Currently implemented with googletrans (pypi package to perform with Google translation). The API is built using Django and Django Rest Framework.

## Installation
1. Clone the repository to your local machine.


2. Create a virtual environment by running the following command:


      python -m venv myenv


3. Activate virtual environment by running following command:

   ##### For Windows
   
       venv\Scripts\activate

   ##### For Unix/Linux:

       source venv/bin/activate

4. Install the required dependencies by running the following command:


      pip install -r requirements.txt

5. Currently, using SQLite3 as database, Configure the Django settings by updating the settings.py file with your database settings, if you want to use any other databases.


6. Apply the database migrations by running the following command:


      python manage.py migrate

7. Start the development server by running the following command:


      python manage.py runserver

8. The API will now be accessible at 

   
      http://localhost:8000/translate/

### API Usage

The API provides a single endpoint for translation: `/translate/`.

### Request

* URL: /translate/
* Method: POST
* Data Format: JSON

#### Request Parameters

The following parameters are required in the request:

* **Request Body:**

  * `source_text` (string): The text to be translated.


* **Query Parameters:**

  * `source_lang` (string): The language code of the source text.
  * `target_lang` (string): The language code of the target translation.


* **Example Request:**

    **_POST:_** /translate/?source_lang=en&target_lang=fr

    **_Content-Type:_** application/json


      {"source_text": "Hello"}


### Response

* Success Response:
  * Status Code: 200
  * Data Format: JSON

* Example Response:


      {"success": true, "translation": "Bonjour"}


* Error Response
  * Status Code: 400
  * Data Format: JSON

* Example Response:


      {"success": false, "message": "Invalid request/query parameters"}


### Caching

* The API implements caching to improve performance and reduce the number of translation requests made to the server.

* When a translation is requested, the API checks if the translation is already available in the cache. If found, the translation is retrieved from the cache and returned to the response. If not found, the translation is performed using the Translator, and the translation is stored in the cache for future requests.

* The cache uses a key generated from the combination of the source text, source language, and target language. This ensures that each translation has a unique cache entry.


### Testing

The API includes unit tests to verify the functionality and correctness of the translation endpoint.

To run the tests, use the following command:


      python manage.py test

The tests cover scenarios such as valid translations, invalid requests.

### Limitations and Future Improvements
* Currently, the API uses the Google Translator for performing translations. If you wish to use a different translation service, you need to modify the implementation accordingly.
* The API assumes that the source text is provided in a single language. Handling mixed-language or multi-lingual text may require additional logic.
* The caching mechanism implemented in the API is a basic in-memory cache. For production use or scenarios with high traffic, consider using a more robust caching solution such as Redis or Memcached.
* Error handling could be improved by providing more specific error messages and handling specific exceptions thrown during translation.
