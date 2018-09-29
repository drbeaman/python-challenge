#MainPyBank
import os
import csv
import statistics

csvpath = os.path.join("..", "PyBank", "03-Python_homework_PyBank_Resources_budget_data.csv")


with open(csvpath, 'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #csv_header = next(csvfile)
    header = next(csvreader)
    month_count = 0
    total_profit = 0
    row = csvreader.__next__()
    profit = int(row[1])
    #month_start = int(row[0])
    profit_end = 0
    profit_change = []
    average_change = int(profit_change / month_count)
        
    for row in csvreader:
        profit = int(row[1])
        month_count += 1
        total_profit += int(row[1])
        profit_end += int(row[1])
        profit_change = float((total_profit - profit)/profit)  
        average_change = float(profit_change)/month_count
        
    
    print(f"Total Months: {month_count}")
    print(f"Total Profit: {total_profit}")
    print(f"Total Average Change: profit change")
        
    #print("Average Change: line_change()")
        