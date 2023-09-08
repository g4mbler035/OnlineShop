from models.User import User
from database.db_connect import create_session
from models.enum.Type import Type

type = Type.USER
def add_user(user):
    session = create_session(type)

    session.add(user)

    session.commit()

def get_users():
    users = []

    session = create_session(type)

    results = session.query(User).all()

    for result in results:
        user = {f"First name": result.first_name, "Last name": result.last_name, "Email": result.email,
                  "List of items": result.list_of_items}

        users.append(user)

    session.commit()

    return users

def delete_user(first_name, last_name):
    session = create_session(type)

    session.query(User).filter(User.first_name == first_name and User.last_name == last_name).delete()

    session.commit()


def update_user(id, user):
    session = create_session(type)

    session.query(User).filter(User.id == id).update(
        {User.first_name: user.first_name, User.last_name: user.last_name, User.email: user.email,
         User.list_of_items: user.list_of_items}, synchronize_session=False
    )

    session.commit()
