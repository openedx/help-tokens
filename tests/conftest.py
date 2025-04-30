"""
Fixtures for the help_tokens tests.
"""


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
        'learner': 'https://docs.openedx.org/en/latest/learners',
        'course_author': 'https://docs.openedx.org/en/latest/educators',
    }
    settings.HELP_TOKENS_VERSION = "latest"
    settings.HELP_TOKENS_LANGUAGE_CODE = "en"
    return settings
