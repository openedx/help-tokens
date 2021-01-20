"""
The context processor for injecting information into Django templates for help_tokens.
"""

from . import core


def _get_online_help_info(token=None):
    """Inner helper for context_processor."""
    return {
        "doc_url": core.HelpUrlExpert.the_one().url_for_token(token),
    }


def context_processor(request):  # pylint: disable=unused-argument
    """
    The help-tokens context processor.

    The odd structure of the return is to maintain compatibility with the way
    edx-platform uses it.

    """
    return {
        "get_online_help_info": _get_online_help_info,
    }
