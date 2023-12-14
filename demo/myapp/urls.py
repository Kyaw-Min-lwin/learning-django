from django.urls import path
from myapp.views import contact
from django.contrib import admin


urlpatterns = [
    path("", contact, name="contact"),
]
