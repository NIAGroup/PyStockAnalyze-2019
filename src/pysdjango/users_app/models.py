from django.db import models

# Create your models here.
class UProfile (models.Model):
	organization = models.CharField(max_length=100)
	date = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(upload_to="media", default="empty")
	# List of field types:
	# https://www.webforefront.com/django/modeldatatypesandvalidation.html

	# To make a new model:
	# [1] Add to the models.py
	# [2] python manage.py makemigrations
	# [3] python manage.py migrate


class UserProfile(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField()
	email = models.CharField(max_length=100)
	