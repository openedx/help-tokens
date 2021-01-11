"""
The core logic for help-tokens.
"""

import configparser
import logging

from django.conf import settings

log = logging.getLogger(__name__)


class HelpUrlExpert:
    """A thing that is good at getting help URLs from tokens."""

    def __init__(self, ini_file_name):
        """Construct an expert, giving the path to the ini file."""
        self.ini_file_name = ini_file_name
        self.config = None

    THE_ONE = None

    @classmethod
    def the_one(cls):
        """Get the single global HelpUrlExpert object."""
        if cls.THE_ONE is None:
            cls.THE_ONE = cls(settings.HELP_TOKENS_INI_FILE)
        return cls.THE_ONE

    def get_config_value(self, section_name, option, default_option="default"):
        """
        Read a value from the configuration, with a default.

        Args:
            section_name (str): name of the section in the configuration from which
                the option should be found.
            option (str): name of the configuration option.
            default_option (str): name of the default configuration option whose
                value should be returned if the requested option is not found.

        Returns:
            str: the value from the ini file.

        """
        if self.config is None:
            self.config = configparser.ConfigParser()
            self.config.read(self.ini_file_name)

        if option:
            try:
                return self.config.get(section_name, option)
            except configparser.NoOptionError:
                log.debug(
                    "Didn't find a configuration option for '%s' section and '%s' option",
                    section_name, option,
                )

        return self.config.get(section_name, default_option)

    def url_for_token(self, token):
        """Find the full URL for a help token."""
        book_url = self.get_config_value("pages", token)
        book, _, url_tail = book_url.partition(':')
        book_base = settings.HELP_TOKENS_BOOKS[book]

        url = book_base

        lang = getattr(settings, "HELP_TOKENS_LANGUAGE_CODE", None)
        if lang is not None:
            lang = self.get_config_value("locales", lang)
            url += "/" + lang

        version = getattr(settings, "HELP_TOKENS_VERSION", None)
        if version is not None:
            url += "/" + version

        url += "/" + url_tail
        return url
