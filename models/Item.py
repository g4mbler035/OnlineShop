from sqlalchemy import Column, String, Integer, CHAR, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Item(Base):
    __tablename__ = "item"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    price = Column("price", Float)
    quantity = Column("quantity", Integer)
    cart_id = Column("cart_id", Integer)

    def __init__(self, id, name, price, quantity, cart_id):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.cart_id = cart_id