"""
URLs for help_tokens.
"""

from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^(?P<token>.*)$', views.help_token_redirect),
]
