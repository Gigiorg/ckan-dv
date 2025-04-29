"""Tests for helpers.py."""

import ckanext.test.helpers as helpers


def test_test_hello():
    assert helpers.test_hello() == "Hello, test!"
