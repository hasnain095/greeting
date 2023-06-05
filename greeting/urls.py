"""
URLs for greeting.
"""
from django.conf.urls import url
from .views import Greeting, greeting_func, login, authorize

urlpatterns = [
    url(r'^v1/greeting/$', Greeting.as_view(), name='greeting'),
    url(r'^v2/greeting/$', greeting_func, name='greeting'),
    url(r'^v1/login/$', login, name="login"),
    url(r'^v1/authorize', authorize, name="authorize")
]
