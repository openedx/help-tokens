# -*- coding: utf-8 -*-
"""
URLs for help_tokens.
"""
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<token>.*)$', views.help_token_redirect),
]
