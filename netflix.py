#Netflix Part 1 + Part 2


# if file is in same directory as the code, then can do this:
csvpath = os.path.join('.', 'netflix_ratings.csv')
user_video = input("Which video would you like to see?")


with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
	for row in csvreader:
		if row[0] == user_video:
			print(row[0] + " is rated " + row[1] + " with a rating of " + row[5])