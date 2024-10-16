from PythonForTester.model.group import Group


def test_add_group(app):
    app.group.create(Group(name="new", header="qweqwe", footer="qweqweqweqwe"))



def test_add_empty_group(app):
    app.group.create(Group(name="new", header="qweqwe", footer="qweqweqweqwe"))

