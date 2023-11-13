import os
import csv

# Path to retrieve the csv file from the Resources folder
POLL_CSV_PATH = r'PyPoll\Resources\election_data.csv'

# Set variable for output file
OUTPUT_PATH = os.path.join("analysis.txt")

# Set variables
total_votes = 0
winner_votes = 0
winner_name = ""
candidate_list = []
candidate_votes = {}
vote_tally = []


with open(POLL_CSV_PATH, 'r') as csvfile:
    poll_reader = csv.reader(csvfile)
    header = next(poll_reader)

    # Read through the csv file and run calculations
    for row in poll_reader:
        total_votes = total_votes + 1

        candidate = row[2]

        # Get the unique values for candidates 
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            
            candidate_votes[candidate] = 0

        # Count the number of times each candidate appears in the dictionary     
        candidate_votes[candidate] = candidate_votes[candidate] + 1

    # Calculate the percentage of each candidate's votes
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = round(int(votes) / int(total_votes) * 100, 3)
        all_votes = (f"{candidate}: {vote_percentage}% ({votes})")
        vote_tally.append(all_votes)
    
        # Find the winner
        if votes > winner_votes:
            winner_votes = votes
            winner_name = candidate

with open(OUTPUT_PATH, 'w') as textfile:

    # Print election results
    election_summary = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
        f"{vote_tally[0]}\n"
        f"{vote_tally[1]}\n"
        f"{vote_tally[2]}\n"
        f"-------------------------\n"
        f"Winner: {winner_name}\n"
        f"-------------------------\n")

    print(election_summary)
    
    # Save election results to text file
    textfile.write(election_summary)


