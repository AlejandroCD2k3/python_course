# Handling a .txt file

txt_file = open("my_file.txt","r+")

    # print(txt_file.read())
    # print(txt_file.read(5))
    # print(txt_file.readline)
    # print(txt_file.readlines)

for line in txt_file.readlines():
    print(line)

txt_file.write(", i'm glad being here")

txt_file.close()

with open("my_file.txt", "a") as my_other_file:
    my_other_file.write("\n I'm still here")

# os.remove("my_file.txt")