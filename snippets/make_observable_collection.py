"""Features ObservableList use, for creating a simple list of items displayed in the UI"""
from reflect import make_observable
from reflect_ant_icons import PlusCircleFilled
from reflect_antd import Button, Input, List, Col, Space
from reflect_html import h5


def app():
    users = ["John"]
    users_obs = make_observable(users, key="users")
    new_user_name = make_observable("", key="new user name")

    def add_user():
        users_obs.append(new_user_name())
        new_user_name.set("")

    return Col(
        [
            Space(
                [
                    Input(
                        placeholder="Enter user name",
                        value=new_user_name,
                        onPressEnter=add_user,
                    ),
                    Button(
                        [PlusCircleFilled(), "Add user"],
                        onClick=add_user,
                        type="primary",
                    ),
                ]
            ),
            List(lambda: [List.Item(h5(user)) for user in users_obs]),
        ]
    )
