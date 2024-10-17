my_dictionary = dict()

my_other_dictionary = {}

print(type(my_dictionary))
print(type(my_other_dictionary))

my_other_dictionary = {"Name":"Michael", "Last name":"Jefferson", "Age":22, 1:"Python"} # We define a "Key : Value" structure

my_dictionary = {
    "Name":"Stephen",
    "Last name":"Hunnigan",
    "Age": 22,
    "Languages": {"Python","Swift","Kotlin"},
    1:1.77
}

print(my_other_dictionary)
print(my_dictionary)

print(len(my_other_dictionary))

print(my_dictionary["Name"])

my_dictionary["Name"] = "Daryl"

print(my_dictionary["Name"])

print(my_dictionary.items())
print(my_dictionary.keys())
print(my_dictionary.values())

print(my_dictionary.fromkeys("Name", "Hi", "Python"))



