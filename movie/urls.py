from django.urls import path
from .views import *


urlpatterns = [
    path('', catalog, name='catalog'),
    path('film_detail/<int:film_id>',film_detail, name='film_detail'),
    path('leave_review/',leave_review, name='leave_review'),
]