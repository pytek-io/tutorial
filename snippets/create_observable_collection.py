"""Features ObservableList use, for creating a simple list of items displayed in the UI"""
import reflect as r
import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def app():
    users = ["John"]
    users_obs = r.ObservableList(users, key="users")
    new_user_name = r.ObservableValue("", key="new user name")

    def add_user():
        users_obs.append(new_user_name())
        new_user_name.set("")

    return antd.Col(
        [
            antd.Space(
                [
                    antd.Input(
                        placeholder="Enter user name",
                        value=new_user_name,
                        onPressEnter=add_user,
                    ),
                    antd.Button(
                        [ant_icons.PlusCircleFilled(), "Add user"],
                        onClick=add_user,
                        type="primary",
                    ),
                ]
            ),
            antd.List(lambda: [antd.List.Item(html.h3(user)) for user in users_obs]),
        ]
    )
