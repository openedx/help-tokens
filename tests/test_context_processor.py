"""
Tests for the `help-tokens.context_processor` module.
"""


from help_tokens import context_processor

# pylint: disable=unused-argument


def test_context_processor(book_settings):
    context = context_processor(None)
    actual = context['get_online_help_info']('instructor')['doc_url']
    expected = "http://edx.readthedocs.io/projects/learner-guide/en/ver/SFD_instructor_dash_help.html"
    assert actual == expected
