"""
URLs for help_tokens.
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<token>.*)$', views.help_token_redirect),
]
