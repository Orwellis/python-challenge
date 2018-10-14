import csv
#We'll use numby to calcuate a list average
import numpy as np

#Data we are examining includes two columns
#"Date" and "Profit/Losses"
budget_data_path = "budget_data.csv"

#Goals:                             #Method:
#Count the total number of months   #Add to count as we loop through data
number_of_months = 0                
#Calculate the net Profit/Losses    #Add to total as we loop through data
net_profit = 0                       
#Calculate the average change       #Create a list of the change between every two months
change_from_previous_month = []     #Then sum the list and divide by its length
previous_month = False              #We don't want to compare the first month to 0
profits_last_month = 0
#Find the greatest profit           #Check each month against current greatest
greatest_profit = 0
greatest_profit_month = ""
#Find the greatest loss             #Check each month against current greatest
greatest_loss = 0
greatest_loss_month = ""
#Print results in readable format to terminal
#Create text file with results

with open(budget_data_path) as csvfile:
    budget_data = csv.reader(csvfile, delimiter=',')
    #pull out header we don't need this data
    csv_header = next(budget_data)
    #loop through months to find number_of_months, net_profit,
    #greatest_profit, greatest_loss, and generate change list
    for row in budget_data:
        this_month = row [0]
        profits_this_month = int(row[1])
        #step month count by one
        number_of_months += 1
        #add to net profit
        net_profit += profits_this_month
        #check to see if we have a new greatest profit
        #as the data is in ascending order this will return
        #the most recent month if multiple are tied for
        #greatest profit
        if profits_this_month >= greatest_profit:
            greatest_profit = profits_this_month
            greatest_profit_month = this_month
        #check to see if we have a new greatest profit loss
        #we will return the most recent month for loss as well
        if profits_this_month <= greatest_loss:
            greatest_loss = profits_this_month
            greatest_loss_month = this_month
        #Check the difference between the month and the previous
        if previous_month:
            change_from_previous_month.append(profits_this_month - profits_last_month) 
        #record this month's profits/losses for analysis with next month
        profits_last_month = profits_this_month
        previous_month = True

        #print results to check code
        #print(f"{this_month} {profits_this_month} Max: {greatest_profit} Min: {greatest_loss} \
        #    Dif: {change_from_previous_month}")
csvfile.close()

#Calclulate average from list we have generated
average_change = round(np.mean(change_from_previous_month),2)

#Format Results
Results = f"Financial Analysis\n\
------------------\n\
Total Months: {number_of_months}\n\
Total: ${net_profit}\n\
Average Change: ${average_change}\n\
Greatest Increase in Profits: {greatest_profit_month} (${greatest_profit})\n\
Greatest Decrease in Profits: {greatest_loss_month} (${greatest_loss})"

print(Results)

#create text file
new_text_file = "budget_data_analysis.txt"
with open(new_text_file,'w') as text:
    text.write(Results)
text.close()

