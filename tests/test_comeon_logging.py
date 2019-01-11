#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `comeon_logging` package."""

import pytest
from comeon_logging import comeon_logging
from comeon_logging import send_slack_message, send_player_missing




@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    
    result = send_slack_message('#test', 'send a test meassage')
    assert result
    
def test_missing_player(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    
    result = send_player_missing('GITHUB: Peter Mustermann')
    assert result
