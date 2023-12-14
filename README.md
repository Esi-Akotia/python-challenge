# python-challenge

This assignment is complete and contains all the required submissions:

1. Scripts for both PyBank and PyPoll data sets stored as 'main.py' in their respective folders
3. Text files for the outputs for both data sets stored as 'analysis.txt' in their respective folders

Note: for the csv file paths in each of the scripts (main.py), I used the relative path to the folder my Python file is in. 

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
      
| Task     | Sub task   | Assigned to:   | Support:  |
| ------------- |-------------| :-----:|  :-----:|
| GitHub Set Up | Main GitHub Host | Behnoosh |  |
| " | README file | Behnoosh, Esi | Amir, Hamza, Sharvil |
| Prepare Data | Retrieve datasets from StatCan | Amir, Sharvil | Esi |
| " | Get data from API (REST Countries, World Bank) | Behnoosh, Hamza | Amir |
| " | Clean Countries Population & GDP API data & save as csv | Behnoosh  |  |
| " | Clean Income by Province data & save as csv  | Sharvil  |  |
| " | Clean Gender data & save as csv  | Sharvil  |  |
| " | Clean World Graduate data & save as csv  | Hamza  |  |
| " | Clean Census Income & Enrollment data & save as csv  | Amir |  |
| " | Clean Graduate data from Census data  | Esi |  |
| Analysis | Analyze gender & graduate data and plot graphs | Behnoosh   |    Amir, Esi, Hamza, Sharvil |
| " | Analyze country & education data and plot graphs | Behnoosh   |    Amir, Esi, Hamza, Sharvil |
| " | Analyze income & graduate data and plot graphs  | Esi   |    Amir, Behnoosh, Hamza, Sharvil |
| " | Analyze enrollment by country data and plot graphs  | Sharvil   |    Amir, Behnoosh, Esi, Hamza |
| " | Analyze world enrollment data and plot heat maps  | Amir  |    Esi, Behnoosh, Hamza, Sharvil |
| Presentation | Set up Google Slides template | Esi |  |
| " | Update slides with output from analysis | Amir, Behnoosh, Esi, Hamza, Sharvil |  |
| " | Class presentation | Behnoosh, Esi | Amir, Hamza, Sharvil |