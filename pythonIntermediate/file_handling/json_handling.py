import json  # Import the built-in json module to work with JSON data.

# Open (or create if it doesn't exist) a file named 'my_file.json' in write and read mode ('w+').
# 'w+' allows both writing to and reading from the file, but any existing content will be overwritten.
json_file = open("my_file.json", "w+")

# Define a dictionary containing some data, including strings, a list, and an integer.
json_text = {
    "name": "Michael", 
    "last_name": "Jefferson", 
    "age": 22, 
    "language": ["Python", "Swift", "Java"],
    "website": "https://github.com/AlejandroCD2k3"
}

# Use json.dump() to write the dictionary (json_text) to the file in JSON format.

json.dump(json_text, json_file, indent=4)

# Move the file's internal pointer back to the start using seek(0)
json_file.seek(0)

# Read and print each line of the file using a loop. This will output the JSON data to the console.
for line in json_file.readlines():
    print(line)

# Close the file after reading (important for file operations).
json_file.close()

# Open the file again (this time using the default read mode 'r') and load its content into a dictionary.
json_dict = json.load(open("my_file.json"))
print(type(json_dict)) 