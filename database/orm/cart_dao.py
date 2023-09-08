from models.Cart import Cart
from database.db_connect import create_session
from models.enum.Type import Type

type = Type.CART
def add_cart(cart):
    session = create_session(type)

    session.add(cart)

    session.commit()

def get_carts():
    carts = []

    session = create_session(type)

    results = session.query(Cart).all()

    for result in results:
        cart = {f"Id": result.id, "List of items": result.list_of_items}

        carts.append(cart)

    session.commit()

    return carts

def delete_cart(id):
    session = create_session(type)

    session.query(Cart).filter(Cart.id == id).delete()

    session.commit()


def update_cart(id, cart):
    session = create_session(type)

    session.query(Cart).filter(Cart.id == id).update(
        {Cart.id: cart.id, Cart.list_of_items: cart.list_of_items}, synchronize_session=False
    )

    session.commit()
