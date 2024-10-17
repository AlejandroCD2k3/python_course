my_set = set() # This is how we define a set

print(type(my_set))

my_set = {} # This initially is a dictionary 

print(type(my_set))

my_set = {35, 1.77, "Michael", "Stallon"}

my_other_set = {"Michael", "Italy", 28}

print(type(my_other_set))

print(len(my_other_set))

# print(my_other_set[0])    Sets doesn't have a specific order, so it can't use index!

my_other_set.add("Rome")

print(my_other_set)

my_other_set.add("Rome")

print(my_other_set) # Sets can't have repeated elements

# print(my_set + my_other_set)  Concatenation in sets is not supported, we'll use union instead

print(my_set.union(my_other_set))

print(my_set.difference(my_other_set))
