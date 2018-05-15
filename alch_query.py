from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_db import Person

engine = create_engine('sqlite:///main.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()


query = session.query(Person.name).order_by(Person.name)
for name in query:
    print(name)

query = session.query(Person.name).filter(Person.placedOrder != 0).filter(Person.area == "Нижегородский").order_by(Person.name)
for name in query:
    print(name)