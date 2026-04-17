import json
import csv
json_file = open("students.json", "r")
data = json.load(json_file)
json_file.close()
csv_file = open("students.csv", "w", newline=’’)
headers = data[0].keys()
writer = csv.DictWriter(csv_file, fieldnames=headers)
writer.writeheader()
writer.writerows(data)
csv_file.close()
print("Conversion completed! Check students.csv file.")