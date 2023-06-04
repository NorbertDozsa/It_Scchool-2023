import csv

with open('salarii.csv') as fin:
    reader = csv.reader(fin.readlines())

for line in reader:
    print(f"Full name: {line[0]} {line[1]}")
    print(f"Gross salary: {int(line[-2]) * 0.45}")