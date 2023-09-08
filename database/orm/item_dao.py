from models.Item import Item
from database.db_connect import create_session
from models.enum.Type import Type

type = Type.ITEM

def add_item(item):
    session = create_session(type)

    session.add(item)

    session.commit()

def get_items():
    items = []

    session = create_session(type)

    results = session.query(Item).all()

    for result in results:
        item = {f"Name": result.name, "Price": result.price, "Quantity": result.quantity, "Cart id": result.cart_id}
        items.append(item)

    session.commit()

    return items

def delete_item(id):
    session = create_session(type)

    session.query(Item).filter(Item.id == id ).delete()

    session.commit()


def update_user(id, item):
    session = create_session(type)

    session.query(Item).filter(Item.id == id).update(
        {
            Item.name: item.name,
            Item.price: item.price,
            Item.quantity: item.quantity,
            Item.cart_id: item.cart_id
        },
        synchronize_session=False
    )

    session.commit()
