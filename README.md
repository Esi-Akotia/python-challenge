# python-challenge

This assignment is complete and contains all the required submissions:

1. Scripts for both PyBank and PyPoll data sets stored as 'main.py' in their respective folders
2. Text files for the outputs for both data sets stored as 'analysis.txt' in their respective folders

Support from AskBCS & Tutor:
Pleae note that I got assistance from my tutor and the Learning Assistants with the following lines of code:

*PyBank Data:*

Lines 31 - 33: 
    
    if previous_profit is not None:
    
    current_change = current_profit - previous_profit
    
    total_change = total_change + current_change

Line 41:
    
    previous_profit = current_profit

*PyPoll Data:*

Lines 33 & 36:
    
    candidate_votes[candidate] = 0
    
    candidate_votes[candidate] = candidate_votes[candidate] + 1

Lines 39 - 40:
    
    for candidate in candidate_votes:
    
    votes = candidate_votes.get(candidate)

Line 43:

    vote_tally.append(all_votes)
      
