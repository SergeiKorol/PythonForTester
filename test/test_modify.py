from PythonForTester.model.group import Group


def test_modify_group_name(app):
    old_groups = app.group.get_groups_list()
    app.group.modify_first_group(Group(name="new_name2"))
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    old_groups = app.group.get_groups_list()
    app.group.modify_first_group(Group(header="new_header2"))
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_footer(app):
    old_groups = app.group.get_groups_list()
    app.group.modify_first_group(Group(footer="new_footer2"))
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups)
