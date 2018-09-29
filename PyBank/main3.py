#Main3

import os
import csv

csvpath = os.path.join("..", "PyBank", "03-Python_homework_PyBank_Resources_budget_data.csv")

def num_rows(group):
    return len(group)

#def getAnalysis(PyBankData):
    #month_count = 0
    #data = list(row[1])
    #month_count = len(data)
print(num_rows)

with open(csvpath, 'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #csv_header = next(csvfile)
    header = next(csvreader)
    #month_count = 0
    #total_profit = 0
    for row in csvreader:
        num_rows
        #month_count = sum(1 for row in csvreader)+1
        #total_profit += int(row[1])
    #print(f"Total Months: {month_count}")
    #print(f"Total Profit: {total_profit}")
    #month_count = sum(1 for row in csvreader)+1
    #total_months = int(PyBankData[1])

    # Average change in Profit/Loss
    #average_change = int(PyBankData[1])
