import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_db import Person, Order
import random

engine = create_engine('sqlite:///main.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

def create_list_ord(n):
    oder_names = ["картошка", "учебник", "плюшка", "крышка люка", "шишка", "игрушка", "балалайка", "водка", "матрёшка"]

    order = []
    for j in range(n):
        name = random.randint(0, 8)
        pr_flag = random.randint(0, 1)
        order.append(Order(j, oder_names[name], pr_flag))
        #session.add(Order(j, oder_names[name], pr_flag))
    #session.commit()

    create_list_per(n, order)

def create_list_per(n,ord):
    names = ["Alex", "Viktor", "Andry", "Max", "Stive", "Oleg", "Vladimir", "Gosha"]
    lastnames = ["Grachev", "Butusov", "Emelin", "Voronin", "Cruglov", "Navalny", "Sidorov", "Ivanov"]
    areas = ["Нижегородский", "Московский", "Канавинский", "Автозаводский", "Ленинский", "Приокский", "Советский",
             "Сормовский"]

    per = []

    for j in range(n):
        one = random.randint(0, 7)
        two = random.randint(0, 7)
        num = random.randint(1000000000, 1999999999)
        are = random.randint(0, 7)
        rate = random.randint(0, 10)

        #per.append(Person(j, names[one]+ " " +lastnames[two],"+7" + str(num), areas[are], rate))
        obj = Person(j, names[one]+ " " +lastnames[two],"+7" + str(num), areas[are], rate)
        obj.order.append(ord[0])
        per.append(obj)
        #session.add(obj)
    session.add_all(ord)
    session.add_all(per)
    session.commit()
    #session.close()

create_list_ord(5)