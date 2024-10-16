from PythonForTester.model.group import Group


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="new_name2"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="new_header2"))


def test_modify_group_footer(app):
    app.group.modify_first_group(Group(footer="new_footer2"))
