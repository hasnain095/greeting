"""
URLs for greeting.
"""
from django.conf.urls import url
from .views import Greetingy, greeting_func

urlpatterns = [
    url(r'^v1/greeting/$', Greeting.as_view(), name='greeting'),
    url(r'^v2/greeting/$', greeting_func, name='greeting'),
]
