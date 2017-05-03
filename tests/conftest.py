# -*- coding: utf-8 -*-
"""
Fixtures for the help_tokens tests.
"""

from __future__ import absolute_import, unicode_literals

import pytest

from help_tokens import core


@pytest.fixture
def sample_expert():
    """Return a HelpUrlExpert based on our sample.ini file."""
    return core.HelpUrlExpert("tests/sample.ini")


@pytest.fixture
def book_settings(settings):
    """Set some HELP_TOKENS settings."""
    settings.HELP_TOKENS_INI_FILE = "tests/sample.ini"
    settings.HELP_TOKENS_BOOKS = {
        'learner': 'http://edx.readthedocs.io/projects/learner-guide',
        'course_author': 'http://edx.readthedocs.io/projects/running-a-course',
    }
    settings.HELP_TOKENS_VERSION = "ver"
    settings.HELP_TOKENS_LANGUAGE_CODE = "en"
    return settings
