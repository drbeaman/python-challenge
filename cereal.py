#Cereal
import os
import csv

csvpath = os.path.join("..", "LearnPython", "cereal.csv")
cereal_csv = os.path.join("..", "LearnPython", "cereal.csv")
with open(csvpath, 'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        next(csv_reader, None)

    print(f"Header)
    name_list = []
    fiber_list = []
    fiber_list5 = [i for i in fiber_list if i >= 5]
    
    for item in list:
        fiber_list.append(float(item))
        #[float(i) for i in fiber_list]
    
        name_list = row[0]
        fiber_list = row[7]
        print(name_list,fiber_list5)