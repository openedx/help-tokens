"""
Django app for linking to help pages with short tokens.
"""

from importlib.metadata import version

from .context_processor import context_processor

__version__ = version("help-tokens")
