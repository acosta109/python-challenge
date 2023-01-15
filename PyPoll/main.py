import os
import csv

#establish pathway to file
csvpath = os.path.join("..", "Resources", "election_data.csv")

#open csv file

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    candidates = {}
    totalVote = 0

    #skip header row
    next(csvreader)

    for rows in csvreader:
        #every row is a vote casted
        totalVote += 1

        #track who's being voted on
        candidate = rows[2]

        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

    print("Election Results\n")
    print("-------------------------\n")
    print(f'Total Votes: {totalVote}\n')
    print("-------------------------\n")
    #print out candidates and vote share


    for candidate in candidates:
        voteShare = round(((candidates[candidate])/totalVote)*100, 3)
        print(f'{candidate}: {voteShare}% ({candidates[candidate]})\n')

    print("-------------------------\n")
    maxKey = max(candidates.items(), key=lambda x: x[1])[0]
    print(f'Winner: {maxKey}\n')
    print("-------------------------\n")

    file2 = os.path.join('Analysis', 'election_results.txt')
    with open(file2, 'w') as file:
        file.write("Election Results\n")
        file.write("-------------------------\n")
        file.write(f'Total Votes: {totalVote}\n')
        file.write("-------------------------\n")
        for candidate in candidates:
            voteShare = round(((candidates[candidate])/totalVote)*100, 3)
            file.write(f'{candidate}: {voteShare}% ({candidates[candidate]})\n')
        file.write("-------------------------\n")
        file.write(f'Winner: {maxKey}\n')
        file.write("-------------------------\n")




    

    




