from PythonForTester.model.group import Group
from PythonForTester.fixture.application import Application
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="new", header="qweqwe", footer="qweqweqweqwe"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="new", header="qweqwe", footer="qweqweqweqwe"))
    app.session.logout()
