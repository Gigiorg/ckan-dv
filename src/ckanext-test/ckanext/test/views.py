from flask import Blueprint


test = Blueprint(
    "test", __name__)


def page():
    return "Hello, test!"


test.add_url_rule(
    "/test/page", view_func=page)


def get_blueprints():
    return [test]
