import os
import csv

# Set the current working directory
current_directory = os.getcwd()
print(current_directory)

# Set the path to the new directory
new_directory = os.path.join(current_directory, 'PyPoll', 'Resources')

# Set the path to the CSV file within the new directory
pypoll_csv = os.path.join(new_directory, 'election_data.csv')

# Open and read csvd
with open(pypoll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Set the variables
    total_votes = 0 
    candidates = []
    votes = {}
    most_votes = 0 
    candidate_name = ""
    

    # The total number of votes cast and list of candidates who received votes
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            votes[candidate] = 0
        votes[candidate] += 1
  
      # Print the results   
    print('Election Results:')
    print('-------------------')
    #Total Results
    print(f'Total votes: {total_votes}')
    print('-------------------')
    #Candidate votes and percentages 
    for candidate in candidates:
        vote_percentage = votes[candidate] / total_votes * 100
        
        if votes[candidate] > most_votes:
            most_votes = votes[candidate]
            candidate_name = candidate

        
        print(f'{candidate}: {vote_percentage:.2f}% ({votes[candidate]})')
    print('-----------------------')
   #The winner of the election based on popular vote
      
print(f'Winner: {candidate_name}')
print('-------------------------')

# Set the path for the output file
output_directory = os.path.join(current_directory, 'Pypoll','analysis')
output_file = os.path.join(output_directory, 'pypoll_final.csv')

# Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile, delimiter='\t')

    # Write the rows
    writer.writerow(['Election Results:'])
    writer.writerow(['--------------------------------'])
    writer.writerow(['Total votes:', total_votes])
    for candidate in candidates:
        vote_percentage = votes[candidate] / total_votes * 100
        writer.writerow([f'{candidate}: {vote_percentage:.2f}% ({votes[candidate]})'])
    writer.writerow(['Winner:', candidate_name])
