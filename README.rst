###########
help-tokens
###########

Django app for linking to help pages with short tokens.

|pypi-badge| |ci-badge| |codecov-badge| |pyversions-badge|
|license-badge|


Overview
********

There are various factors that affect what help page an application should link
to:

- There may be a number of relevant books

- The version of the application might affect which book to display

- The application's language might affect which book to display

This small Django app provides a means to use "help tokens" on the application
pages, and then use those tokens, and various other settings, to determine the
actual URL to use.


Documentation
*************

Help-tokens provides a context processor, and a redirection URL.  Configuration
is in a number of settings.

Settings
========

Help-tokens reads these Django settings to create URLs:

* HELP_TOKENS_INI_FILE: Path to a .ini file containing help token definitions.
  The format of the ini file is described below.

* HELP_TOKENS_BOOKS: a dictionary mapping book slugs to URLs.  For example::

    HELP_TOKENS_BOOKS = {
        'learner': 'http://edx.readthedocs.io/projects/learner-guide',
        'course_author': 'http://edx.readthedocs.io/projects/running-a-course',
    }

* HELP_TOKENS_VERSION: a string used as part of the final URL, to choose the
  correct version of the book.  For example, `"latest"`.

* HELP_TOKENS_LANGUAGE_CODE: the language code to use as part of the book URL,
  mapped through the [locales] section of the ini file.

INI file format
===============

The .ini file pointed to by HELP_TOKENS_INI_FILE contains the definitions of
the help tokens themselves.

The `[pages]` section defines the help tokens.  Each help token definition
consists of a book slug (defined in HELP_TOKENS_BOOKS), a colon, and a URL
path.  The `default` token is used for missing tokens.  For example::

    [pages]
    default = learner:index.html
    instructor = learner:SFD_instructor_dash_help.html
    course = learner:index.html

    cohortmanual = course_author:course_features/cohorts/cohort_config.html#assign-learners-to-cohorts-manually
    cohortautomatic = course_author:course_features/cohorts/cohorts_overview.html#all-automated-assignment

The `[locales]` section defines language codes, used with
HELP_TOKENS_LANGUAGE_CODE to determine the language portion of the URL::

    [locales]
    default = en
    en = en
    en_us = en


Context processor
=================

The context processor is `"help_tokens.context_processor"`.  It adds a function
`get_online_help_info`.  Call it with a help token, and it will return a dict
with a `doc_url` entry, the help URL. You can use it like this in a template::

    <a href="${get_online_help_info('visibility')['doc_url']}">...</a>

This interface is a bit verbose, but is to maintain backward compatibility with
a previous implementation of this context processor.


Redirection view
================

The `help_tokens.urls` URLs define a view that redirects to a help URL. You can
include it in your app::

    # For redirecting to help pages.
    url(r'^help_token/', include('help_tokens.urls')),

Then visiting `help_token/foobar` will redirect to the URL defined by the
"foobar" help token.


License
*******

The code in this repository is licensed under the AGPL 3.0 unless otherwise
noted.  Please see ``LICENSE.txt`` for details.

How To Contribute
*****************

Contributions are very welcome.

Please read `How To Contribute <https://github.com/openedx/.github/blob/master/CONTRIBUTING.md>`_ for details.


PR description template should be automatically applied if you are sending PR from GitHub interface; otherwise you
can find it it at `PULL_REQUEST_TEMPLATE.md <https://github.com/openedx/help-tokens/blob/master/.github/PULL_REQUEST_TEMPLATE.md>`_

Issue report template should be automatically applied if you are sending it from GitHub UI as well; otherwise you
can find it at `ISSUE_TEMPLATE.md <https://github.com/openedx/help-tokens/blob/master/.github/ISSUE_TEMPLATE.md>`_

Reporting Security Issues
*************************

Please do not report security issues in public. Please email security@edx.org.

Getting Help
************

Have a question about this repository, or about Open edX in general?  Please
refer to this `list of resources`_ if you need any assistance.

.. _list of resources: https://open.edx.org/getting-help


.. |pypi-badge| image:: https://img.shields.io/pypi/v/help-tokens.svg
    :target: https://pypi.python.org/pypi/help-tokens/
    :alt: PyPI

.. |ci-badge| image:: https://github.com/openedx/help-tokens/workflows/Python%20CI/badge.svg?branch=master
    :target: https://github.com/openedx/help-tokens/actions?query=workflow%3A%22Python+CI%22
    :alt: CI

.. |codecov-badge| image:: http://codecov.io/github/edx/help-tokens/coverage.svg?branch=master
    :target: http://codecov.io/github/edx/help-tokens?branch=master
    :alt: Codecov

.. |pyversions-badge| image:: https://img.shields.io/pypi/pyversions/help-tokens.svg
    :target: https://pypi.python.org/pypi/help-tokens/
    :alt: Supported Python versions

.. |license-badge| image:: https://img.shields.io/github/license/edx/help-tokens.svg
    :target: https://github.com/openedx/help-tokens/blob/master/LICENSE.txt
    :alt: License

