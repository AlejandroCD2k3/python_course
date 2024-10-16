my_string = "My String"
my_other_string = "Another string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string) # Concatenating strings with a space between them

print("This is a \n line break") # \n works as a line break in a String
print("This is a \t tabulation") # \t works as a tabulation in a String


# ----------- FORMATING -----------

name, age = "Alejandro", 21

print("Hi, my name is %s and i'm %d" %(name, age)) # %s is a String formatting, %d is a int formatting
print("Hi, my name is {} and i'm {}".format(name, age)) # We can also use .format and {}
print(f"Hi, my name is {name} and i'm {age}") # We can also use a f before the string and using variable names between {}

# ----------- CHAR UNPACKING -----------

language = "Python"
a, b, c, d, e, f = language

print(a+b+c)
print(d+e+f)

# ----------- STRING SLICES -----------

language_slice = language[1:3] # This takes from first to second position pace of language's content

print(language_slice)

language_slice = language[1:] # This takes from the first position onward of language's content

print(language_slice)

language_slice = language[-2] # This takes the second last position

print(language_slice)

language_slice = language[::-1] # This reverses the word from the last one position

print(language_slice)

lowercase_language = language.lower() # This turns the string into lower case

print(lowercase_language)

print(lowercase_language.capitalize()) # This turns the first letter of the string into a upper case

print(lowercase_language.upper()) # This turns the String into upper case

print(language.count("t")) # This one count's how muche t's are in language content

print(language.isnumeric()) # If it's numeric it returns true, otherwise it returns false

print("1".isnumeric())

print(lowercase_language.isupper()) # If it's upper case it returns true, otherwise it returns false

print(language.startswith("py")) # If it starts with py, it returns true