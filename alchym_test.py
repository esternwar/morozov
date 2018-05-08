from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///student.db', echo=True)
Base = declarative_base()


########################################################################
class Student(Base):
    """"""
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    area = Column(String)
    placedOrder = Column(String)
    giveOrder = Column(String)
    rate = Column(String)

    # ----------------------------------------------------------------------
    class Person:
        def __init__(self, id, name, phone, area, placedorder, giveOrder, rate):
            self.id = id
            self.name = name
            self.phone = phone
            self.area = area
            self.placedOrder = placedorder
            self.giveOrder = giveOrder
            self.rate = rate


# create tables
Base.metadata.create_all(engine)