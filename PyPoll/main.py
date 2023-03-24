#Importing csv for reading the csv file and os for accessing the file system.
import csv
import os

# Set the path to the CSV file
csvpath = os.path.join("Resources","election_data.csv")

# Initialize variables
total_votes = 0
winner_votes = 0
each_candidate_votes = {}
winner_name = ""

#Open and Read the CSV file 
with open(csvpath, encoding="utf-8") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header row
    next(csvreader)
#Count the total votes and votes for each candidate    
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate not in each_candidate_votes:
            each_candidate_votes[candidate] = 1
        else:
            each_candidate_votes[candidate] += 1

# Determine the winner of the election
for candidate in each_candidate_votes:
    votes = each_candidate_votes[candidate]
    if votes > winner_votes:
        winner_votes = votes
        winner_name = candidate

# Print the analysis results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in each_candidate_votes:
    votes = each_candidate_votes[candidate]
    percentage = votes / total_votes * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner_name}")
print("-------------------------")

# Write results to output file
output_file = os.path.join("Analysis","election_result.txt")
with open(output_file, "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("-------------------------\n")
    for candidate in each_candidate_votes:
        votes = each_candidate_votes[candidate]
        percentage = votes / total_votes * 100
        outfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner: {winner_name}\n")
    outfile.write("-------------------------\n")
 
