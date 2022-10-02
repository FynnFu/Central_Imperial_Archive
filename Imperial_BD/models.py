from django.db import models

# Create your models here.


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="photos/")
    gender = models.CharField(max_length=50)
    birth_date = models.CharField(max_length=50)
    dynasty = models.CharField(max_length=80)
    tall = models.CharField(max_length=50)
    eye_color = models.CharField(max_length=50)
    hair_color = models.CharField(max_length=50)
    marital_status = models.CharField(max_length=50)
    joke_names = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    organizations = models.CharField(max_length=50)
    biography = models.TextField(blank=True)
