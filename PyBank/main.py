import os
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')


with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header row
    csvheader = next(csvreader)

    totalMonths = 0
    totalProfitLoss = 0
    greatestIncrease = 0
    greatestDecrease = 0
    greatestIncreaseMonth = ''
    greatestDecreaseMonth = ''
    previousProfitLoss = 0
    totalChange = 0

    # Read each row
    for row in csvreader:

        # Count number of months
        totalMonths += 1


        #
        totalProfitLoss += int(row[1])

        # Check greatest increase, if value is greater than previous there is profit
        if int(row[1]) > previousProfitLoss:
            if totalMonths > 1:
                totalChange += int(row[1]) - previousProfitLoss
            if greatestIncrease < (int(row[1]) - previousProfitLoss):
                greatestIncrease = int(row[1]) - previousProfitLoss
                greatestIncreaseMonth = row[0]
       # Check greatest decrease, if value is lesser than previous there is loss
        else:
            if totalMonths > 1:
                totalChange -= previousProfitLoss - int(row[1])
            if greatestDecrease < (previousProfitLoss - int(row[1])):
                greatestDecrease = previousProfitLoss - int(row[1])
                greatestDecreaseMonth = row[0]
            
        previousProfitLoss = int(row[1])

    #
    aveChange = totalChange / (totalMonths - 1)

 
    # Display output
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {totalMonths}")
    print(f"Total: ${totalProfitLoss}")
    print(f"Average Change: ${round(aveChange,2)}")
    print(f"Greatest Increase in Profits: {greatestIncreaseMonth} (${greatestIncrease})")
    print(f"Greatest Decrease in Profits: {greatestDecreaseMonth} ($-{greatestDecrease})")
