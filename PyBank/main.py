import os
import csv

# Open CSV file to read data
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

        # Collect total Profit/Loss
        totalProfitLoss += int(row[1])

        # Check greatest increase, if value is greater than previous there is profit
        # Also accumulate total change, comparison of change each month progressing
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

    # Get average of total change
    aveChange = totalChange / (totalMonths - 1)

# Open TXT file to write analysis
txtpath = os.path.join('.', 'Analysis', 'Result.txt')

with open(txtpath, 'w') as txtfile:

    # Write to file
    txtfile.write("Financial Analysis")
    txtfile.write("\n\n")
    txtfile.write("----------------------------")
    txtfile.write("\n\n")
    txtfile.write(f"Total Months: {totalMonths}")
    txtfile.write("\n\n")
    txtfile.write(f"Total: ${totalProfitLoss}")
    txtfile.write("\n\n")
    txtfile.write(f"Average Change: ${round(aveChange,2)}")
    txtfile.write("\n\n")
    txtfile.write(f"Greatest Increase in Profits: {greatestIncreaseMonth} (${greatestIncrease})")
    txtfile.write("\n\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatestDecreaseMonth} ($-{greatestDecrease})")
    txtfile.write("\n\n")

    # Display output
    print("\nFinancial Analysis\n")
    print("----------------------------\n")
    print(f"Total Months: {totalMonths}\n")
    print(f"Total: ${totalProfitLoss}\n")
    print(f"Average Change: ${round(aveChange,2)}\n")
    print(f"Greatest Increase in Profits: {greatestIncreaseMonth} (${greatestIncrease})\n")
    print(f"Greatest Decrease in Profits: {greatestDecreaseMonth} ($-{greatestDecrease})\n")
