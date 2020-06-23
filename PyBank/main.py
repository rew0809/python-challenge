import os   
import csv

csvpath = os.path.join("Resources","budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    csvheader = next(csvreader)
    

    #Define variables for scanning csv and counting
    numMonths = 0
    profitLoss = 0
    avgDiffSum = 0
    amounts = [0]
    count = 1
    inc = 0
    monthInc = None
    dec = 0
    monthDec = None

    #Count total number of months and total profit/loss
    for row in csvreader:    
        numMonths += 1
        profitLoss += int(row[1])
        
        #logic for calculating greatest increas/decrease and running sum of monthly diffs
        amounts.append(row[1])
        if count > 1:
            if (int(amounts[count]) - int(amounts[count - 1])) > inc:
                inc = (int(amounts[count]) - int(amounts[count - 1]))
                monthInc = row[0]
            if (int(amounts[count]) - int(amounts[count - 1])) < dec:
                dec = (int(amounts[count]) - int(amounts[count - 1]))
                monthDec = row[0]
            avgDiffSum += (int(amounts[count]) - int(amounts[count - 1]))
        count += 1

    #calculate average monthly change
    AvgChange = round(avgDiffSum/(numMonths - 1),2)

#Print Results
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {numMonths}")
    print(f"Total: ${profitLoss}")
    print(f"Average Change: ${AvgChange}")
    print(f"Greatest Increase in Profits: {monthInc} (${inc})")
    print(f"Greatest Decrease in Profits: {monthDec} (${dec})")

output_path = os.path.join("Analysis", "pyBankResults.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Total Months: {numMonths}"])
    csvwriter.writerow([f"Total: ${profitLoss}"])
    csvwriter.writerow([f"Average Change: ${AvgChange}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {monthInc} (${inc})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {monthDec} (${dec})"])


    
