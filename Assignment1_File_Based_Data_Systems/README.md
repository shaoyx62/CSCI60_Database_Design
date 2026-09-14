# Public Restrooms Census (2015) — Three Data Questions


## Why I Chose This Dataset
I chose the Public Restrooms Census dataset because I found that it's sometimes hard to find a public restroom in NYC.
The dataset contains clear categorical variables such as location type, accessibility, status, and restroom type, 
which makes it useful for research questions and comparing different kinds of facilities.


---

## Three Data Questions

### Question: How many public restroom facilities are located in parks?
park_count = 0
for row in restrooms:
    if row["Location Type"] == "Park":
        park_count += 1
print("Restrooms in parks:", park_count)
**output: 824**

Why the data structure supports this question:
This works because each row represents one public restroom facility, and the Location Type column stores a categorical
label describing where the restroom is located. Counting the rows where Location Type equals "Park" gives the total number of 
restroom facilities located in parks.

### Question: How many restrooms are listed as Fully Accessible, and how many are listed as Not Accessible?
fully_accessible = 0
not_accessible = 0
for row in restrooms:
    if row["Accessibility"] == "Fully Accessible":
        fully_accessible += 1
    elif row["Accessibility"] == "Not Accessible":
        not_accessible += 1
print("Fully accessible:", fully_accessible)
print("Not accessible:", not_accessible)
**output: Fully Accessible: 619, Not Accessible: 218**

Why the data structure supports this question:
This works because Accessibility is a single column that categorizes each restroom facility by its accessibility status.
Since each row represents one facility, counting the rows labeled "Fully Accessible" and "Not Accessible" shows
how many facilities fall into each of those categories.

### Question: Among park restrooms, how many are listed as Fully Accessible, and how many are listed as Not Accessible?
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
**output: Fully Accessible: 470, Not Accessible: 213**

Why the data structure supports this question:
This works because we can filter rows using one column (Location Type == "Park") and then summarize a second column (Accessibility).
The dataset's "one row = one restroom facility" structure makes it possible to combine conditions and count accessibility categories
within the subset of park restrooms.


## What the Data Cannot Answer

A question I might want to answer is: “Which parts of New York City have the best access to public restrooms?”
This dataset cannot fully answer that question because it does not include information such as neighborhood population, traffic, 
or how far people have to travel to reach each restroom. Although the dataset includes restroom locations, it does not tell us
how many people actually need or use each facility. It would be misleading to assume that an area with more listed restrooms
automatically has better public restroom access.



