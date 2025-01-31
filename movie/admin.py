from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


@admin.register(MoviePerson)
class MoviePersonAdmin(admin.ModelAdmin):
    pass


@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass