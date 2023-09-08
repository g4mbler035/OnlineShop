from sqlalchemy import Column, Integer, ARRAY, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Cart(Base):
    __tablename__ = "cart"
    id = Column("id", Integer, primary_key=True)
    list_of_items = Column("list_of_items", ARRAY(Integer), ForeignKey("item.id"))

    def __init__(self, id, list_of_items):
        self.id = id
        self.list_of_items = list_of_items
