# import the csv and os module
import csv
import os

# Path to collect data from the Resources folder
csvpath = os.path.join("Resources/", "election_data.csv")

# file to hold the output of the budget analysis
outputFile = os.path.join("analysis/", "electiondataAnalysis.txt")

# variables
totalVotes = 0 
candidates = [] # list that holds the candidates in the survey
candidateVotes = {} # dictionary that will hold the votes each candidates receives
winningCount = 0 # holds winning count
winningCandidate = ""

# read the csv file
with open(csvpath) as electionData:
    # create teh csv reader
    csvreader = csv.reader(electionData)

    # read the header
    header = next(csvreader)

    # rows will be lists
        # index 0 is the ballot id
        # index 1 is the county
        # index 2 is the candidate
    # for each row
    for row in csvreader:
        # add on to the total votes
        totalVotes += 1 # same as totalVotes = totalVotes + 1

        # check to see if the candidates is in the list of candidates
        if row[2] not in candidates:
            # if the candidate is not in the list, add the candidate to the list of candidates
            candidates.append(row[2])
    

            # add the value to the dictionary as well
            # { "key" : value}
            # start the count at 2
            candidateVotes[row[2]] = 1

        else:
            #  the candidate is in the list of candidates
            # add a vote to the candidate count
            candidateVotes[row[2]] += 1
            
#print(candidateVotes)
voteOutput = ""


for candidates in candidateVotes:
    # get the vote count and the percentage of the votes
    votes = candidateVotes.get(candidates)
    votePct = (float(votes) / float(totalVotes)) *100.000
    voteOutput += f"{candidates}: {votePct:.3f}% ({votes})\n"

    # compare the votes to the winning count
    if votes > winningCount:
        winningCount = votes
        winningCandidate = candidates


WinnerOutput = f"Winner: {winningCandidate} \n"

# create an output variable to hold the output
output = (
    f"Election Results \n"
    f"------------------------- \n"
    f"Total Votes: {totalVotes:} \n"
    f"------------------------- \n"
    f"{voteOutput}"
    f"------------------------- \n"
    f"{WinnerOutput}"
    f"------------------------- \n"
)

print(output)

# export the output to the output text file
with open(outputFile, "w") as textfile:
    textfile.write(output)
