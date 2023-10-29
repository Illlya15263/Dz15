from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('product/<id>', product),
    path('sent_review/', post_review)
]