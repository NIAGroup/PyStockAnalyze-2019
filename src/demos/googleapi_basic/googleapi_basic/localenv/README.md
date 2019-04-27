# Local Environment File Readme
This folder exists for users to add any and all python files that contain private data in them to them.

The minimum required files that the user must create are:
1. localapikeys.py
	* Must define the following variables in this file:
		* ```google_cse_api_key='api_key_string'```
		* ```google_cse_eng_id='engine_id_string'```
	* To acquire a google API key to use the custom search engine, a google API account must be made:
		* https://developers.google.com/custom-search/v1/overview
2. localuser.py
   * Must contain declaration of variable django_production_key, which is a 50-digit secret key
   * In form ```django_production_key = '01234567890123456789012345678901234567890123456789'```
   * There are various ways to generate random keys--for instance, DJango automatically generates one when a new project is started.
   * This stackoverflow article explains how to generate secret keys: https://stackoverflow.com/questions/4664724/distributing-django-projects-with-unique-secret-keys
   * This website has an automatic secret key generator: https://www.miniwebtool.com/django-secret-key-generator/
3. localwebproxy.py
