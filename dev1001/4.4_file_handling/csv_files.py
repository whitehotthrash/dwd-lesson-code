import csv

with open('grades.csv', newline='') as f:
  reader = csv.DictReader(f)
  # csv_reader = csv.reader(f)
  # header = next(csv_reader)
  for row in reader:
    # name, subject, grade = row
    print(f"{row['Name']} got {row['Grade']} in {row['Subject']}") # row is a dictionary
    
    
new_data = [
  ["Name", "Subject", "Score"],
  ["Asshole", "History", "88"],
  ["Eve", "Art", "92"]
]

with open('grades.csv', 'a', newline='') as f:
  csv_writer = csv.writer(f)
  csv_writer.writerows(new_data)
