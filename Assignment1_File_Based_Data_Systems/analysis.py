import csv

def load_csv(filepath):
    data = []

    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    return data


#load dataset
restrooms = load_csv("Public_Restrooms.csv")


#1. print the first 2 rows
print(restrooms[0:2])

#2. print the first row
print(restrooms[0])

#3. print rows 10-19
print(restrooms[10:20])

#4. print column names
print(restrooms[0].keys())

#5. print the first 10 values of one column
for row in restrooms[0:10]:
    print(row["Status"])

#6. print the first 10 rows of three columns
for row in restrooms[0:10]:
    print(
        row["Facility Name"],
        row["Location Type"],
        row["Accessibility"]
    )


#question 1: How many public restroom facilities are located in parks?
park_count = 0

for row in restrooms:
    if row["Location Type"] == "Park":
        park_count += 1

print("Restrooms in parks:", park_count)


#question 2: How many restrooms are fully accessible vs. not accessible?
fully_accessible = 0
not_accessible = 0

for row in restrooms:
    if row["Accessibility"] == "Fully Accessible":
        fully_accessible += 1
    elif row["Accessibility"] == "Not Accessible":
        not_accessible += 1

print("Fully accessible:", fully_accessible)
print("Not accessible:", not_accessible)


#question 3: Among park restrooms, how many are fully accessible vs. not accessible?
park_fully_accessible = 0
park_not_accessible = 0

for row in restrooms:
    if row["Location Type"] == "Park":
        if row["Accessibility"] == "Fully Accessible":
            park_fully_accessible += 1
        elif row["Accessibility"] == "Not Accessible":
            park_not_accessible += 1

print("Fully accessible park restrooms:", park_fully_accessible)
print("Not accessible park restrooms:", park_not_accessible)



