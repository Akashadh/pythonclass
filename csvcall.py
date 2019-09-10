import csv

with open('akash.csv') as student_list:
    data = csv.reader(student_list)
    for x in data:
        print(x)



