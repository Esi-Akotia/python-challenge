import os
import csv

# Path to retrieve the csv file from the Resources folder
BUDGET_CSV_PATH = r'PyBank\Resources\budget_data.csv'

# Set variables
total_months = 0
total_profit = 0
total_change = 0
previous_profit = None
max_change_value = 0
min_change_value = -999


with open(BUDGET_CSV_PATH, 'r') as csvfile:
    budget_reader = csv.reader(csvfile)
    header = next(budget_reader)
    
    # Read through the csv file and run the calculations
    for row in budget_reader:
        total_months = total_months + 1

        #total amount of profit/loss
        current_profit = int(row[1])
        current_month = row[0]

        total_profit = total_profit + current_profit

        # Find average change over time and the maximum increase & decrease
        if previous_profit is not None:
            current_change = current_profit - previous_profit
            total_change = total_change + current_change
            if current_change > max_change_value:
                max_change_value = current_change
                max_change_month = current_month
            if current_change < min_change_value:
                min_change_value = current_change
                min_change_month = current_month              
        
        previous_profit = current_profit

    average_change = round(total_change/(total_months - 1), 2)


# Set variable for output file
OUTPUT_PATH = os.path.join("analysis.txt")

with open(OUTPUT_PATH, 'w') as textfile:

    # print financial analysis
    financial_analysis = (
        f"\n\nFinancial Analysis\n"
        f"---------------------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_profit}\n"
        f"Average Change: ${average_change}\n"
        f"Greatest Increase in Profits: {max_change_month} $({max_change_value})\n"
        f"Greatest Decrease in Profits: {min_change_month} $({min_change_value})\n")
    
    print(financial_analysis)

    # Save financial analysis to text file
    textfile.write(financial_analysis)

  

    
       



        






