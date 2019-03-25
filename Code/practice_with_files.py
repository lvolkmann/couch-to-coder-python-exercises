#Practice with reading files!
f = open("C:\\Users\\Landon\\OneDrive\\UMKC\\Fall 2018\\SI\\Code\\EmployeeData.txt")
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


import csv

with open("EmployeeData.csv.txt") as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) >= 3 and row[2].strip()=="True":
            print(row[1])

f.close()
