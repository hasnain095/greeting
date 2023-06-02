"""
URLs for greeting.
"""
from django.urls import re_path , path # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import
from .view import greeting

urlpatterns = [
    # re_path(r'', TemplateView.as_view(template_name="greeting/base.html")),
    re_path(r"^greeting/", greeting)
]
