"""
Django app for linking to help pages with short tokens.
"""

from __future__ import absolute_import, unicode_literals

from .context_processor import context_processor

__version__ = '1.0.4'

default_app_config = 'help_tokens.apps.HelpTokensConfig'  # pylint: disable=invalid-name
