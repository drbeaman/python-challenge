#Udemy

import os
import csv
csvpath = os.path.join("..", "LearnPython", "udemy_starter.csv")

with open(csvpath, 'r', encoding='utf8', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    title_list = []
    price_list = []
    subscriber_count_list = []
    number_reviews_list = []
    course_length_list = []

    for row in csvreader:
        #print(row[0],row[4],row[5],row[6],row[9])
        title = row[1]
        price = row[4]
        subscriber_count = row[5]
        number_review = row[6]
        course_length = row[9]

        title_list.append(title)
        price_list.append(price)
        subscriber_count_list.append(subscriber_count)
        number_reviews_list.append(number_review)
        course_length_list.append(course_length)
    #print(title_list)
    #print(price_list)
    #print(subscriber_count_list)
    #print(number_reviews_list)
    #print(course_length_list)
    z = list(zip(title_list,price_list,subscriber_count_list,number_reviews_list,course_length_list))
   
output_path = os.path.join("..", "LearnPython", "udemy_ouput.csv")

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['title','price','numSubscribers','numReviews','contentInfo'])
    for row in z:
        csvwriter.writerow(row)
