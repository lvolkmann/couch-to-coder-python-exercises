"""
Write a program to read file EmployeeData.csv and print the id of every employee suspected of arson
BONUS: Try doing it with and without the csv module
"""
# Without CSV
f = open("EmployeeData.csv")
header = f.readline()

employeeList = f.readlines()
suspectID = []
for employee in employeeList:
    entry = employee.split(',')
    if len(entry) < 3:
        continue
    if entry[2].strip()=="True":
        suspectID.append(entry[1])

for i in suspectID:
    print(i)

f.close()

# With CSV

import csv

with open("EmployeeData.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) >= 3 and row[2].strip()=="True":
            print(row[1])

f.close()
