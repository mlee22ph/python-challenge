import os
import csv

# Open CSV file to write analysis
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header
    csvheader = next(csvreader)

    candidates = dict()
    totalVotes = 0

    # Loop thru rows and count votes for each candidate
    for row in csvreader:

        # Count total votes
        totalVotes += 1

        # Count votes for each candidate
        # Check if new candidate
        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1



# Open TXT file to write analysis
txtpath = os.path.join('.', 'Analysis', 'Result.txt')

with open(txtpath, 'w') as txtfile:

    # Write to file and display to output
    txtfile.write("Election Results")
    txtfile.write("\n\n")
    txtfile.write("----------------------------")
    txtfile.write("\n\n")
    txtfile.write(f"Total Votes: {totalVotes}")
    txtfile.write("\n\n")
    txtfile.write("----------------------------")
    txtfile.write("\n\n")

    print("\nElection Results\n")
    print("----------------------------\n")
    print(f"Total Votes: {totalVotes}\n")
    print("----------------------------\n")

    # Display candidates and results
    # Loop thru dict of candidates, votes
    # Also find winner with largest votes
    winner = ""
    largestVote = 0
    for candidate in list(candidates):
        candidateVote = candidates[candidate]
        percentVote = (candidateVote/totalVotes) * 100

        # Get largest vote
        if largestVote < candidateVote:
            winner = candidate
            largestVote = candidateVote

        # Output to file
        txtfile.write(f"{candidate}: {round(percentVote, 3)}% ({candidateVote})")
        txtfile.write("\n\n")

        # Output to display
        print(f"{candidate}: {round(percentVote, 3)}% ({candidateVote})\n")


    # Display winner
    txtfile.write("----------------------------")
    txtfile.write("\n\n")
    txtfile.write(f"Winner: {winner}")
    txtfile.write("\n\n")
    txtfile.write("----------------------------")
    txtfile.write("\n\n")

    print("----------------------------\n")
    print(f"Winner: {winner}\n")
    print("----------------------------\n")

