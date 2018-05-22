from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///main.db', echo=True)
Base = declarative_base()


########################################################################
class Person(Base):
    """"""
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    area = Column(String)
    rate = Column(Integer)
    order = relationship('Order', back_populates="person")


    def __init__(self, id, name, phone, area, rate):
        self.id = id
        self.name = name
        self.phone = phone
        self.area = area
        self.rate = rate

class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    orderFlg = Column(Integer)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship("Person", back_populates="order")

    def __init__(self, id, name,orderFlg):
        self.id = id
        self.name = name
        self.orderFlg = orderFlg

# create tables
Base.metadata.create_all(engine)