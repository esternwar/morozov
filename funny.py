from person import Person
import random

def filling():
    names = ["Alex","Viktor","Andry","Max","Stive","Oleg","Vladimir","Gosha"]
    lastnames = ["Grachev","Butusov","Emelin","Voronin","Cruglov","Navalny","Sidorov","Ivanov"]
    areas = ["Нижегородский", "Московский", "Канавинский", "Автозаводский", "Ленинский", "Приокский", "Советский", "Сормовский"]

    people = []

    for j in range(100):
        one = random.randint(0, 7)
        two = random.randint(0, 7)
        num = random.randint(1000000000, 1999999999)
        are = random.randint(0,7)
        place = random.randint(1,100)
        getor = random.randint(1,100)
        rate = random.randint(0,10)
        #people.append(Person(j, names[one]+ " " +lastnames[two],"+7" + str(num), areas[are],place,getor, rate))
        people.append((j, names[one]+ " " +lastnames[two],"+7" + str(num), areas[are],place,getor, rate))

    return people


data = filling()
print(data)