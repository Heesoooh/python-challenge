import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join("Resources/", "budget_data.csv")


# file to hold the output of the budget analysis
outputFile = os.path.join("analysis/", "budgetAnalysis.txt")

# Set up a variable to hold total number og month
totalMonth = 0 # initalize the total months to 0
totalNetAmount = 0 # initalzie the total net amount
monthlyChange = [] # intitalize the list of monthly net changes
months = []        # intitalize the list of months


# read the csv file 
with open(csvpath) as budgetData:
    # create a csv reader object
    csvreader = csv.reader(budgetData)

    # read the header row
    header = next(csvreader)
    # move to the first row
    firstRow = next(csvreader)

    # increment the count of the total month
    totalMonth += 1 # same as totalMonth = totalMonth + 1

    # add on to the total net amount
         # Net amount is in the index 1
    totalNetAmount += float(firstRow[1])

    # establish the previous profit/loss
        # Net amount is in the index 1
    previousProfitLoss = float(firstRow[1])

    for row in csvreader:
        # increment the count of the total month
        totalMonth += 1 # same as totalMonth = totalMonth + 1

        # add on to the total net amount
            # Net amount is in the index 1
        totalNetAmount += float(row[1])

        # calculate the net change 
        netChange = float(row[1]) - previousProfitLoss
        # add on to the list of monthly changes
        monthlyChange.append(netChange)

        # add the first month that a change occured
        months.append(row[0])

        # update the previous profit/loss
        previousProfitLoss = float(row[1])

# Calculate the average net changes on Profit/Loss
averageChangePerMonth = sum(monthlyChange) / len(monthlyChange)

greatestIncrease = [months[0], monthlyChange[0]] # holds the month and the value of the greatest increase
greatestDecrease = [months[0], monthlyChange[0]] # holds the month and the value of the greatest decrease


# use loop to calculate the index of the greatest and least monthly change
for m in range(len(monthlyChange)):
    # calculate the greatest increase and decrease
    if(monthlyChange[m] > greatestIncrease[1]):
        # if the value is greatest than the greatest increase, that value becomes the new greatest increase
        greatestIncrease[1] = monthlyChange[m]
        # update the month
        greatestIncrease[0] = months[m]

    if(monthlyChange[m] < greatestDecrease[1]):
        # if the value is greatest than the greatest decrease, that value becomes the new greatest decrease
        greatestDecrease[1] = monthlyChange[m]
        # update the month
        greatestDecrease[0] = months[m]


# start generating the output to the terminal
output = (
    f"Financial Analysis \n"
    f"---------------------------- \n"
    f"Total Months: {totalMonth} \n"
    f"Total: ${totalNetAmount:.0f} \n" 
    f"Average Change: ${averageChangePerMonth:.2f} \n"
    f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]:.0f}) \n"   
    f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]:.0f}) \n"
)

# print to gitbash
print(output)

# export the output to the output text file
with open(outputFile, "w") as textfile:
    textfile.write(output)



