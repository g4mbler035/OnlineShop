from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
from models.User import User
from models.Item import Item
from models.Cart import Cart
from models.enum.Type import Type

url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="aleksa",
    host="localhost",
    database="shop"
)

def create_session(type):

    engine = create_engine(url)

    if Type.USER == type:
        User.__table__.create(bind=engine, checkfirst=True)
    if Type.ITEM == type:
        Item.__table__.create(bind=engine, checkfirst=True)
    if Type.CART == type:
        Cart.__table__.create(bind=engine, checkfirst=True)

    Session = sessionmaker(bind=engine)

    return Session()