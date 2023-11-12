import os
import csv


POLL_CSV_PATH = r'Resources\election_data.csv'


total_votes = 0
winner_votes = 0
winner_name = ""
candidate_list = []
candidate_votes = {}


with open(POLL_CSV_PATH, 'r') as csvfile:
    poll_reader = csv.reader(csvfile)
    header = next(poll_reader)

    for row in poll_reader:
        total_votes = total_votes + 1

        candidate = row[2]

        if candidate not in candidate_list:
            candidate_list.append(candidate)
            
            candidate_votes[candidate] = 0
            
        candidate_votes[candidate] = candidate_votes[candidate] + 1

    print(candidate_votes)
        
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = round(int(votes) / int(total_votes) * 100, 2)
        vote_tally = (f"{candidate}: {vote_percentage}% ({votes})") #---------> doesn't work, need to fix!

        if votes > winner_votes:
            winner_votes = votes
            winner_name = candidate
    


print(total_votes)   
print(candidate_list)
print(winner_name)
print(winner_votes)
print(vote_tally)


# Election Results
# -------------------------
# Total Votes: {total_votes}
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: {winner_name}
# -------------------------

