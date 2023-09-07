from sqlalchemy import Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column("id", Integer, primary_key=True)
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)
    email = Column("email", String)
    list_of_items = Column("list_of_items", )

    def __init__(self, id, first_name, last_name, email, list_of_items):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.list_of_items = list_of_items