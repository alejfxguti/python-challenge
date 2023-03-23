# python-challenge
Module 3 Challenge: Two Python challenges, PyBank and PyPoll

## PyBank

In this challenge I was given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

My task was to create a Python script that analyzes the records to calculate each of the following values:
- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The changes in "Profit/Losses" over the entire period, and then the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in profits (date and amount) over the entire period

## PyBank Script Breakdown

The script first imports the csv module to read the CSV file. It then opens the CSV file using the with statement and creates a csv.reader object to read the file. The next() function is used to skip the header row of the file.

Next is establishing variables for the script. The script sets up several variables, including empty lists to store month names and profit/loss changes, and counters to keep track of the number of months and the total profit/loss over the period.

The script reads the data from the CSV file using the csv.reader() function and loops through each row. It extracts the month name and profit/loss data from each row and calculates the net profit/loss for the period.

The script calculates the monthly profit/loss changes by subtracting the previous month's profit/loss from the current month's profit/loss. It stores these changes in the profit_loss_changes list.

The script calculates various summary statistics, including the total number of months, total profit/loss, average monthly change, and the greatest increase and decrease in profit/loss over the period.

The script prints the analysis results to the console using print statements and exports the same results to a text file using the os and open() functions.

## PyPoll

In this Challenge, I was given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 

My task was to create a Python script that analyzes the votes and calculates each of the following values:
- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote

## PyPoll Python Script Breakdown

The script first imports the csv module to read the CSV file. It also opens a text file that will copy the printed results and write them in a text file. 

It then opens the CSV file using the with statement and creates a csv.reader object to read the file. The next() function is used to skip the header row of the file.

The script uses an empty dictionary vote_counts to store the vote count for each candidate. It then loops over each row in the CSV file and updates the vote counts for each candidate in the vote_counts dictionary. If the candidate already exists in the dictionary, the vote count is incremented by 1. If the candidate does not exist in the dictionary, a new key-value pair is added with a vote count of 1.

After counting the votes, the script prints the election results using the print() function. It prints the total vote count and a separator line.

The script then loops over the key-value pairs in the vote_counts dictionary and calculates the percentage of votes for each candidate using the formula votes / total_votes * 100. It prints the candidate's name, their percentage of votes with three decimal places, and their total vote count.

Finally, the script finds the candidate with the most votes using the max() function with the vote_counts.get method as the key. It then prints the name of the winner.
