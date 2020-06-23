import os   
import csv

csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    csvheader = next(csvreader)
    #allow for multiple parsings of the csv:
    data = [row for row in csvreader]
   
    #Get total vote count and distinct list of candidates:
    totalCount = 0
    candidates = []
    for row in data:
        #Total vote count:
        totalCount += 1
        #Distinct candidate list:
        if row[2] not in candidates:
            candidates.append(row[2])
    
    #Create dictionary for counting votes for each candidate:
    voteCounts = []
    percentage = []
    i = 1
    while i <= len(candidates):
        voteCounts.append(0)
        percentage.append(0)
        i += 1
    candCount = {"Candidate": candidates,"Percentage": percentage, "Count":voteCounts}

    #Loop to count candidates vote:
    for row in data:   
        voteCounts[candidates.index(row[2])] += 1
    
    #Calculate percentage of votes:
    i = 0
    while i <= (len(candidates) - 1):
        percentage[i] = round(100*(voteCounts[i]/totalCount),3)
        i += 1
        
    #Finding winner:
    winner = None
    winner = candidates[voteCounts.index(max(voteCounts))]

#Print Results:
print('Election Results')
print("-------------------------")
print(f"Total Votes: {totalCount}")
print("-------------------------")
i = 0
while i <= (len(candidates) - 1):
    print(f"{candidates[i]}: {percentage[i]}% ({voteCounts[i]})")
    i += 1
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

output_path = os.path.join("Analysis", "pyPollResults.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Total Votes: {totalCount}"])
    csvwriter.writerow(["-------------------------"])
    i = 0
    while i <= (len(candidates) - 1):
        csvwriter.writerow([f"{candidates[i]}: {percentage[i]}% ({voteCounts[i]})"])
        i += 1
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(["-------------------------"])
