"""Tests for views.py."""

import pytest

import ckanext.test.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "test")
@pytest.mark.usefixtures("with_plugins")
def test_test_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("test.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, test!"
