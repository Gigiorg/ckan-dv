"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.test.logic import validators


def test_test_reauired_with_valid_value():
    assert validators.test_required("value") == "value"


def test_test_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.test_required(None)
