# To learn and validate regular expressions: https://regex101.com/

import re

my_string = "This is regular expression class"
my_other_string = "This isn't data structures class"

match = re.match("This is regular", my_string, re.I)

print(match)
print(match.span())

start, end = match.span()

print(my_string[start:end])

#print(re.match("This is regular", my_string, re.I))
#print(re.match("This is regular", my_other_string, re.I))

#-------------------------------------------------------------

search = re.search("is regular", my_string, re.I)

print(search)

start, end = search.span()

print(my_string[start:end])

#-------------------------------------------------------------

find = re.findall("is", my_string, re.I)

print(find)

#-------------------------------------------------------------

print(re.split("is", my_string))

#-------------------------------------------------------------

print(re.sub("is|iS", "Is", my_string))
print(re.sub("i[s|S]", "Is", my_string))

# ------------------------------ PATTERNS ------------------------------

pattern = r"i[sS]|class"

print(re.findall(pattern, my_string, re.I))

#-------------------------

pattern = r"[a-z]"

print(re.findall(pattern, my_string, re.I))

pattern = r"[0-9]"

print(re.findall(pattern, my_string, re.I))

pattern = r"\d"

print(re.findall(pattern, my_string, re.I))

pattern = r"\D"

print(re.findall(pattern, my_string, re.I))

pattern = r"[i]"

print(re.findall(pattern, my_string, re.I))

pattern = r"[i].*"

print(re.findall(pattern, my_string, re.I))

# ------------------------------ EMAIL VALIDATION ------------------------------

email = "myEmail20@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

print(re.match(pattern, email))

