# -*- coding: utf-8 -*-
"""URL views for help-tokens."""

from __future__ import absolute_import, unicode_literals

from django.http import HttpResponseRedirect

from . import core


def help_token_redirect(request, token=None):       # pylint: disable=unused-argument
    """Redirect to the URL for a help token."""
    return HttpResponseRedirect(core.HelpUrlExpert.the_one().url_for_token(token))
