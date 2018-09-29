#MainPyBank
import os
import csv

csvpath = os.path.join("..", "PyBank", "03-Python_homework_PyBank_Resources_budget_data.csv")

with open(csvpath, 'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    month_count = 0
    total_profit = 0
    #row = csvreader.__next__()
    last = 0
    total_profit = 0
    change = 0
    profit_change_list = []

    for row in csvreader:
        num = int(row[1])
        profit = int(row[1])
        month_count += 1
        total_profit += num
        if (last == 0):
            last = num
        else:
            change = num - last
            last = num
            profit_change_list.append(change)
    #print(profit_change_list)
    profit_change = int(total_profit - profit)
    def average_change(l):
        average_change = sum(l) / len(l)
        greatest_profit_inc = max(l)
        greatest_profit_dec = min(l)
        result = [average_change,greatest_profit_inc,greatest_profit_dec]
        return (result)   
        
    result = average_change(profit_change_list)
    #for num in range(len(profit_change_list)):
     #       profit_change_list[num] = int(profit_change_list[num])
    
    print(f"Total Months: {month_count}")
    print(f"Total Profit: {total_profit}")
    #print(f"Total Profit Change: {profit_change_list}")
    print(f"Total Average Change: {result[0]}")
    print(F"Greatest Increase in Profits: {result[1]}")
    print(f"Greatest Increase in Profits: {result[2]}")


    my_text = f"""
    Total Months: {month_count}
    Total Profit: {total_profit}
    Total Average Change: {result[0]}
    Greatest Increase in Profits: {result[1]}
    Greatest Increase in Profits: {result[2]}
    """


    my_output = open("output.txt", mode = 'w')
    my_output.write(my_text)
    my_output.close()