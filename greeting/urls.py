"""
URLs for greeting.
"""
from django.conf.urls import url
from .views import Greeting

urlpatterns = [
    url(r'^v1/greeting/$', Greeting.as_view(), name='greeting'),
]
