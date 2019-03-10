from django.conf.urls import url, include
from django.contrib import admin

from .views import foo_view

urlpatterns = [
    url(r'^foo/', foo_view, name='foo'),
]
