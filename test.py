from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///main.db', echo=True)
Base = declarative_base()

class Person(Base):
    """"""
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    area = Column(String)
    rate = Column(Integer)
    order = relationship('Order', back_populates="person")

class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    orderFlg = Column(Integer)
    order_id = Column(Integer, ForeignKey('person.id'))
    person = relationship("Person", back_populates="order")

o = Order()
p = Person()
p.order.append(o)
p.order.append(o)
print(p.order)