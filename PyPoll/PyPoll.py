#PyPoll
import os
import csv

csvpath = os.path.join("..", "PyPoll",  "03-Python_homework_PyPoll_Resources_election_data.csv")

with open(csvpath, 'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    id_count = 0
    row = csvreader.__next__()
    vote_total = 0
    vote_khan = 0
    vote_correy = 0
    vote_li = 0
    vote_otooley = 0
            
    for row in csvreader:
        vote_total += 1
        id_count += 1
        if row[2] == "Khan":
            vote_khan += 1
        if row[2] == "Correy":
            vote_correy += 1
        if row[2] == "Li":
            vote_li += 1
        if row[2] == "O'Tooley":
            vote_otooley += 1
    
    khan_pct = vote_khan / vote_total * 100
    correy_pct = vote_correy / vote_total * 100
    li_pct = vote_li / vote_total * 100
    otooley_pt = vote_otooley / vote_total * 100  
    candidate_lst = ["Khan","Correy","Li","O'Tooley"]
    candidate_pct_lst = [khan_pct,correy_pct,li_pct,otooley_pt]
    my_max = max(candidate_pct_lst)
    winner = candidate_lst[candidate_pct_lst.index(my_max)] 

    print(f"------------------------------------")
    print(f"Total Votes: {vote_total}")
    print(f"------------------------------------")
    print(f"Khan: {khan_pct}% ({vote_khan})")
    print(f"Correy: {correy_pct}% ({vote_correy})")
    print(f"Li: {li_pct}% ({vote_li})")
    print(f"O'Tooley: {otooley_pt}% ({vote_otooley})")
    print(f"------------------------------------")
    print(f"Winner: {winner}")

my_text = f"""
    ------------------------------------
    Total Votes: {vote_total}"
    ------------------------------------
    Khan: {khan_pct}% ({vote_khan})
    Correy: {correy_pct}% ({vote_correy})
    Li: {li_pct}% ({vote_li})
    O'Tooley: {otooley_pt}% ({vote_otooley})

"""
my_output = open("output.txt", mode = 'w')
my_output.write(my_text)
my_output.close()
    