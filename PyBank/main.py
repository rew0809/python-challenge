import os   
import csv

csvpath = os.path.join("Resources","budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    csvheader = next(csvreader)
    


    numMonths = 0
    profitLoss = 0
    avgDiffSum = 0
    amounts = [0]
    count = 1
    inc = 0
    monthInc = None
    dec = 0
    monthDec = None
    for row in csvreader:    
        numMonths += 1
        profitLoss += int(row[1])
        
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

    AvgChange = round(avgDiffSum/(numMonths - 1),2)

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {numMonths}")
    print(f"Total: ${profitLoss}")
    print(f"Average Change: ${AvgChange}")
    print(f"Greatest Increase in Profits: {monthInc} (${inc})")
    print(f"Greatest Decrease in Profits: {monthDec} (${dec})")
    
