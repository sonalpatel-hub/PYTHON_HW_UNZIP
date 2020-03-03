import os
import csv
from collections import Counter
# READ CSV FILE
# Path to collect data from the Resources folder
electiondata_csv = os.path.join("..", "PyPoll\Resources", "election_data.csv")

totalVoteCnt = 0
# Open and read csv
with open(electiondata_csv, newline="") as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")

    # * The total number of votes cast
    header= next(csvreader)
    
#   * A complete list of candidates who received votes

    candidateVoteCnt = dict()

    for row in csvreader: 
   #     if row[2] not in candidateVoteCnt:
   #         candidateVoteCnt[row[2]] = 0
        totalVoteCnt += 1
        candidateVoteCnt[row[2]] = candidateVoteCnt.get(row[2],0) + 1



#    value = len(list(csvreader))
   # print(value)
    print("Election Results")
    print("---------------------------------")
    print("Total votes: %d" %totalVoteCnt)

#for row in candidateVoteCnt
#    print("Candidate %s has %d votes:" %(dict[row].key))

for i in candidateVoteCnt.keys():
    print("Candidate %s has %d votes that is %f  " %(i,candidateVoteCnt[i],(candidateVoteCnt[i]/totalVoteCnt)*100))


#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.