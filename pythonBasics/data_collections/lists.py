my_list = list() # Defyning a list (It's not an array!)

my_other_list = [] # This is a list too

print(len(my_list)) # We can see our list lenght (It's dynamic :D)

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Michael", "Stallon"] # It can save different types

print(my_other_list[1]) # Printing list's second position
print(my_other_list.count(35)) # We can count items in a list

print(my_list + my_other_list) # We can also concatenate lists

my_other_list.append("First") # We can add items to our list in the last position

print(my_other_list)

my_other_list.insert(2,"New") # And we can also add items in a specific position

print(my_other_list)

my_other_list.remove("First") # Removing an item

print(my_other_list)

my_other_list.pop() # This removes the last item (If we don't specify)

print(my_other_list)

del my_other_list[2] # This is another way of removing items from a list in a certain index

print(my_other_list)

my_list.clear() # This clear the whole list

print(my_list)

my_other_list.insert(0,42) # If we insert an item in an already occupied possition, this will override the information
my_other_list[1] = 2.99

print(my_other_list)

my_list = my_other_list.copy() # We can copy a list into another

my_list.reverse() # And we can reverse the items inside

print(my_list)

my_other_list.sort() # This sorts the items in the list

print(my_other_list)