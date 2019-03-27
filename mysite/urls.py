from django.conf.urls import url, include
from django.contrib import admin

from .views import first_view, second_view, third_view, fourth_view

urlpatterns = [
    url(r'^first/', first_view, name='first'),
    url(r'^second/', second_view, name='second'),
    url(r'^third/', third_view, name='third'),
    url(r'^fourth/', fourth_view, name='fourth'),
]
