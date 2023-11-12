import os
import csv


BUDGET_CSV_PATH = r'PyBank\Resources\budget_data.csv'


total_months = 0
total_profit = 0
total_change = 0
previous_profit = None
max_change_value = -999
min_change_value = -999


with open(BUDGET_CSV_PATH, 'r') as csvfile:
    budget_reader = csv.reader(csvfile)
    header = next(budget_reader)
  
    for row in budget_reader:
        total_months = total_months + 1

        #total amount of profit/loss
        current_profit = int(row[1])
        current_month = row[0]

        total_profit = total_profit + current_profit

        #average change over time
        if previous_profit is not None:
            current_change = current_profit - previous_profit
            total_change = total_change + current_change
            if current_change > max_change_value:
                max_change_value = current_change
                max_change_month = current_month
            if current_change < min_change_value:
                min_change_value = current_change
                min_change_month = current_month

               
        #for next row
        previous_profit = current_profit

average_change = total_change/(total_months - 1)

print(average_change)
print(total_months)
print(total_profit)        
print(average_change)
print(max_change_month)
print(max_change_value)
print(min_change_month)
print(min_change_value)


#  # Set variable for output file
#  OUTPUT_PATH = os.path.join("analysis.txt")


# Financial Analysis
# ----------------------------
# Total Months: {total_months}
# Total: ${total_amount}
# Average Change: ${average_change}
# Greatest Increase in Profits: {date} (${geratest})
# Greatest Decrease in Profits: {date} (${lowest})
  

    
       



        






