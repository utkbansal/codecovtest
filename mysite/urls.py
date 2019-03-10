from django.conf.urls import url, include
from django.contrib import admin

from .views import foo_view, bar_view, hello2_view

urlpatterns = [
    url(r'^foo/', foo_view, name='foo'),
    url(r'^bar/', bar_view, name='bar'),
    # url(r'^hello/', hello_view, name='hello'),
    url(r'^hello/', hello2_view, name='hello'),
]
