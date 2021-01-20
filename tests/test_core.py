"""
Tests for the `help-tokens.core` module.
"""


import pytest

# pylint: disable=unused-argument


def test_get_config_value(sample_expert):
    assert sample_expert.get_config_value("pages", "instructor") == "learner:SFD_instructor_dash_help.html"
    assert sample_expert.get_config_value("pages", "course") == "another_book:something_about_course.html"


def test_get_default_value(sample_expert):
    assert sample_expert.get_config_value("pages", "xyzzy") == "learner:index.html"


def test_missing_section(sample_expert):
    with pytest.raises(Exception):
        sample_expert.get_config_value("foobar", "help")


def test_no_token(sample_expert):
    assert sample_expert.get_config_value("pages", None) == "learner:index.html"


def test_url_for_token(sample_expert, book_settings):
    expected = "http://edx.readthedocs.io/projects/learner-guide/en/ver/SFD_instructor_dash_help.html"
    assert sample_expert.url_for_token("instructor") == expected


def test_no_version(sample_expert, book_settings):
    book_settings.HELP_TOKENS_VERSION = None
    expected = "http://edx.readthedocs.io/projects/learner-guide/en/SFD_instructor_dash_help.html"
    assert sample_expert.url_for_token("instructor") == expected


def test_language_code(sample_expert, book_settings):
    book_settings.HELP_TOKENS_LANGUAGE_CODE = "fr_CA"
    expected = "http://edx.readthedocs.io/projects/learner-guide/fr/ver/SFD_instructor_dash_help.html"
    assert sample_expert.url_for_token("instructor") == expected


def test_unknown_language_code(sample_expert, book_settings):
    book_settings.HELP_TOKENS_LANGUAGE_CODE = "xx"
    expected = "http://edx.readthedocs.io/projects/learner-guide/en/ver/SFD_instructor_dash_help.html"
    assert sample_expert.url_for_token("instructor") == expected


def test_no_language_code(sample_expert, book_settings):
    book_settings.HELP_TOKENS_LANGUAGE_CODE = None
    expected = "http://edx.readthedocs.io/projects/learner-guide/ver/SFD_instructor_dash_help.html"
    assert sample_expert.url_for_token("instructor") == expected
