# Instuctions: create a Python script that analyzes the records to calculate each of the following values:
    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in profits (date and amount) over the entire period

# import packages necessary to run pyton script
import os
import csv

# Define variables
months = []
profit_loss_changes = []
months_count = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0

# set up file path to collect data from the Resources folder
budget_csv = os.path.abspath('Resources/budget_data.csv')

# open and read the csv file using the csv module
with open(budget_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    csv_header = next(csv_file)
    
    for row in csv_reader:
        # count total # of months
        months_count = months_count + 1
        
        # calculate net total "profit/losses"
        current_month_profit_loss = int(row[1])
        net_profit_loss = net_profit_loss + current_month_profit_loss

        if (months_count == 1):
            # make previous month profit loss equal to current month
            previous_month_profit_loss = current_month_profit_loss
            continue

        else:

            # calculate change in profit loss
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            # append each month to the months[]
            months.append(row[0])

            # append each profit_loss change to the profit_loss_changes
            profit_loss_changes.append(profit_loss_change)

            # make current_month_loss to be previous_month_loss for next loop
            previous_month_profit_loss = current_month_profit_loss

    #sum and average of the changes in "Profit/Losses" over the entire period
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(months_count - 1), 2)

    # highest and lowest changes in "Profit/Losses" over the entire period
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    # Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period
    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)

    # Assign best and worst month
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {months_count}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")


# Export a text file with the results
analysis_file = os.path.abspath('analysis/fin.analysis.txt')
with open(analysis_file, "w") as outputfile:
    outputfile.write(f"Financial Analysis\n"
                     f"----------------------------\n"
                     f"Total Months:  {months_count}\n"
                     f"Total:  ${net_profit_loss}\n"
                     f"Average Change:  ${average_profit_loss}\n"
                     f"Greatest Increase in Profits:  {best_month} (${highest_change})\n"
                     f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")