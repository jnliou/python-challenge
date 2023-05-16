import os
import csv

# Set the current working directory
current_directory = os.getcwd()
print(current_directory)

# Set the path to the new directory
new_directory = os.path.join(current_directory, 'Resources')

# Set the path to the CSV file within the new directory
pybank_csv = os.path.join(new_directory, 'budget_data.csv')

# Open and read csv
with open(pybank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

        # Initialize variables
    total_months = 0
    total_profit_loss = 0
    prev_profit_loss = None
    change_list = []
    date = []

    # Read through each row of data after the header
    for row in csv_reader:
        # Increment total months counter
        total_months += 1

        # Add profit/loss to total
        total_profit_loss += int(row[1])

        # Add date and profit/loss to lists

        date.append(row[0])

        # Calculate change from previous month
        if prev_profit_loss is not None:
            change = int(row[1]) - prev_profit_loss
            change_list.append(change)

        # Set current profit/loss to previous for next iteration
        prev_profit_loss = int(row[1])

    # Calculate total change and average change
    total_change = sum(change_list)
    avg_change = total_change / len(change_list)

    #Find the greatest increase in profits (date and amount) over the entire period
    max_inc = max(change_list)
    max_index = change_list.index(max_inc)
    max_date = date[max_index+1] 

    #Find the greatest decrease in profits (date and amount) over the entire period
    min_inc = min(change_list)
    min_index = change_list.index(min_inc)
    min_date = date[min_index+1]  
    # Output results
    print("Financial Analysis:")
    print("---------------------")
    print(f"Total months assessed: ${total_months}")
    print(f"Total Profit/Loss: ${total_profit_loss}")
    print(f"Average total change: ${avg_change:.2f}")
    print(f"The greatest increase in profit was in {max_date} (${max_inc})")
    print(f"The greatest increase in profit was in {min_date} (${min_inc})")

# Set the path for the output file
output_directory = os.path.join(current_directory, 'analysis')
output_file = os.path.join(output_directory, 'pybank_final.txt')

# Open the output file
with open(output_file, "w") as datafile:
    # Write the rows
    datafile.write('Financial Analysis:\n')
    datafile.write('--------------------------------\n')
    datafile.write(f'Total months assessed: {total_months}\n')
    datafile.write(f'Total Profit/Loss assessed: ${total_profit_loss}\n')
    datafile.write(f'Average total change: ${avg_change:.2f}\n')
    datafile.write(f'The greatest increase in profit was in {max_date} (${max_inc})\n')
    datafile.write(f'The greatest decrease in profit was in {min_date} (${min_inc})\n')

