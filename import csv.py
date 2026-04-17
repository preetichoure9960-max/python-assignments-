import csv
f = open("students.csv", "w", newline='')
writer = csv.writer(f)
writer.writerow(["Name", "Marks"])
writer.writerow(["Amit", 85])
writer.writerow(["Riya", 90])
f.close()
f = open("students.csv", "r")
reader = csv.reader(f)
for row in reader:
	print(row)
f.close()
