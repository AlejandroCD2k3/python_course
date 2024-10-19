import csv


csv_file = open("my_file.csv", "w+")

csv_writer = csv.writer(csv_file)

csv_writer.writerow(["name", "lastname", "age", "language", "website"])
csv_writer.writerow(["Michael", "Jefferson", 22, "Python", "https://github.com/AlejandroCD2k3"])
        
csv_file.seek(0)

for line in csv_file.readlines():
    print(line)




