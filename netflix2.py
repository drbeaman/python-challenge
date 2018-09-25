#Netflix Part 1 Skip the list print
#Part 2: Just ask which video they would like to see and then print the attributes of that array.
import os
import csv

video = input("What show or movie are you looking for? ")

csvpath = os.path.join("..", "LearnPython", "netflix_ratings.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        if row[0] == video:
            print(row[0] + " is rated " + row[1] + ": " + row[2] + "released in " + row[4] + " with a rating of " + row[5])