import csv

data = []
headers = []

with open("dataset_2.csv", "r") as f:
    csvReader = csv.reader(f)
    for i in csvReader:
        data.append(i)
headers = data[0]
planetData = data[1:]

for item in planetData:
    item[0] = item[0].lower()

planetData.sort(key=lambda planetData: planetData[0])

with open("dataset_2_sorted.csv", "a+") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planetData)
    
