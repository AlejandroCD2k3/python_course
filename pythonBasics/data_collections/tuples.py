my_tuple = tuple() # Defyning a tuple
my_other_tuple = () # This is a tuple too! :D

my_tuple = (35, 1.77, "Michael", "Stallon")
my_other_tuple = (28, 2.26, "Fredrick", "Last")

print (my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple.count("Michael"))
print(my_tuple.index(35))

# my_tuple[1] = 1.80    This is not possible! A tupple data can't be modified

print(my_tuple+my_other_tuple)
print(my_other_tuple[1:3])

my_other_tuple = list(my_other_tuple) # We can transform a tuple into a list
print(type(my_other_tuple))

del my_other_tuple # This deletes the tuple
# print(my_other_tuple)  