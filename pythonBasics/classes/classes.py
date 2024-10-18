class MyEmptyPerson:
    pass


print("Hi")
print(MyEmptyPerson)
print(MyEmptyPerson())

class MyPerson:
    def __init__(self, name, lastname, alias = "No alias") -> None:
        self.fullname = f"{name} {lastname} (Alias: {alias})"
        self.__name = name
        self.__lastname = lastname
        self.__alias = alias

    def walk(self):
        print(f"{self.fullname} is walking")

    def get_name(self):
        return self.__name

my_person = MyPerson("Michael","Clinton")
my_person.walk()

another_person = MyPerson("Bobby","Castle","Tower")

# print(my_person.alias)
# print(another_person.alias)

# my_person.alias = "Dude"

# print(my_person.alias)