from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/images/avatars/')
    favorite_movies = models.ManyToManyField('movie.Movie', related_name='movies')