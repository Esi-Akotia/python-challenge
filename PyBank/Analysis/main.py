import os
import csv

#read the csv file
budget_csv = r'PyBank\Resources\budget_data.csv'


#calculate the total number of months
total_months = 0
total_amount = 0
average_change = 0




with open(budget_csv, 'r') as csvfile:
   
    budget_file = csv.reader(csvfile, delimiter=',')
 
    header = next(budget_file)

    for row in budget_file:
        total_months = total_months + 1

        amount = int(row[1])
        total_amount = total_amount + amount

        change = int(row[1])
        average_change = average_change - change

average_change /= (total_months)  if total_months > 1 else 0
        
print(average_change)


    # print(total_months)
    # print(total_amount)  
  
       



        






       

   
        

 


