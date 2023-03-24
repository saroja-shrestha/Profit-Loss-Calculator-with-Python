#Importing csv for reading the csv file and os for accessing the file system.
import csv
import os

# Set up file paths
budget_data = os.path.join("Resources", "budget_data.csv")

# Initialize variables
total_profit_loss = 0
total_months = 0
current_pl = 0
change = 0
date = []
profits = []

# Open and read the CSV file
with open(budget_data, encoding="utf-8") as csvfile:
    csvreader = csv.DictReader(csvfile)

    # Get the first row of data
    first_row = next(csvreader)
    total_months += 1
    total_profit_loss += int(first_row["Profit/Losses"])
    current_pl = int(first_row["Profit/Losses"])

    # Process each row of data after the first row
    for row in csvreader:
        # Keep track of the date
        date.append(row["Date"])

        # Calculate the change, then add it to list of changes
        change = int(row["Profit/Losses"]) - current_pl
        profits.append(change)
        current_pl = int(row["Profit/Losses"])

        # Update total number of months
        total_months += 1

        # Update total net amount of "Profit/Losses over entire period"
        total_profit_loss += int(row["Profit/Losses"])

    # Calculate greatest increase and decrease in profits
    greatest_increase = max(profits)
    greatest_increase_index = profits.index(greatest_increase)
    greatest_date = date[greatest_increase_index]

    greatest_decrease = min(profits)
    greatest_decrease_index = profits.index(greatest_decrease)
    low_date = date[greatest_decrease_index]

    # Calculate average change in "Profit/Losses between months over entire period"
    average_change = sum(profits) / len(profits)

# Print the analysis results
print(f"Financial Analysis\n{'-' * 30}")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {low_date} (${greatest_decrease})")

# Write results to output file
output_file = os.path.join("Analysis","budget_data.txt")
with open(output_file, "w") as outfile:
    outfile.write(f"Financial Analysis\n{'-' * 30}\n")
    outfile.write(f"Total Months: {total_months}\n")
    outfile.write(f"Total: ${total_profit_loss}\n")
    outfile.write(f"Average Change: ${average_change:.2f}\n")
    outfile.write(f"Greatest Increase in Profits: {greatest_date} (${greatest_increase})\n")
    outfile.write(f"Greatest Decrease in Profits: {low_date} (${greatest_decrease})\n")
