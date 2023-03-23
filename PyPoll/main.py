# Instructions: create a Python script that analyzes the records to calculate each of the following values:
    # The total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote
    # import packages necessary to run pyton script

import os
import csv

# set up file path to collect data from the Resources folder
election_csv = os.path.abspath('Resources/election_data.csv')
# set up file path to text file in analalysis folder
analysis_file = os.path.abspath('analysis/elect.res.txt')

# Open text file to write election results
with open(analysis_file, "w") as outputfile:
    outputfile.write("Election Results\n")
    outputfile.write("-------------------------\n")

# open and read the csv file using the csv module
    with open(election_csv, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_header = next(csv_file) # skip the header row
        vote_counts = {} # A dictionary is created to each candidate's vote count

# for loop goes over each csv row extracting unique candidates as key
# counts votes for each candidate and updates the key's value accordingly

        for row in csv_reader:
            # count total # of votes cast
            candidate = row[2]
            if candidate in vote_counts:
                vote_counts[candidate] = vote_counts[candidate] + 1
            else:
                vote_counts[candidate] = 1

# sum calculates total votes by adding up values in vote_counts dictionary.
# The election results are then printed using the print() function.

        total_votes = sum(vote_counts.values())
        print("Election Results") # print to terminal
        print("-------------------------") # print to terminal
        print(f"Total Votes: {total_votes}") # print to terminal
        outputfile.write(f"Total Votes: {total_votes}\n")# copied to write to text file
        print("-------------------------") # print to terminal
        outputfile.write("-------------------------\n") # copied to write to text file

# another for loop is run through each key-value pair in the 
# dictionary to calculate percentages and print candidate results

    for candidate, votes in vote_counts.items():
        vote_percentage = votes / total_votes * 100
        print(f"{candidate}: {vote_percentage:.3f}% ({votes})") # print to terminal
        outputfile.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n") # copied to write to text file
    

    print("-------------------------")
    outputfile.write("-------------------------\n") # copied to write to text file
    # Find candidate with most votes and print the winner 
    # using the vote_counts dictionary
    winner = max(vote_counts, key=vote_counts.get)
    print(f"Winner: {winner}") # print to terminal
    outputfile.write(f"Winner: {winner}\n") # copied to write to text file
    print("-------------------------") # print to terminal
    outputfile.write("-------------------------\n") # copied to write to text file