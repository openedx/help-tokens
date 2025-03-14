"""
Tests for the help-tokens urls and views.
"""


# pylint: disable=unused-argument


def test_redirect(client, book_settings):
    response = client.get("/instructor")
    assert response.status_code == 302
    expected = "https://docs.openedx.org/en/latest/learners/SFD_instructor_dash_help.html"
    assert response['location'] == expected
