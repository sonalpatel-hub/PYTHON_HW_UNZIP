# * In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# * Your task is to create a Python script that analyzes the records to calculate each of the following:
import os
import csv
from collections import Counter
# READ CSV FILE
# Path to collect data from the Resources folder
budgetdata_csv = os.path.join("..", "PyBank\Resources", "budget_data.csv")

# Open and read csv
with open(budgetdata_csv, newline="") as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
    

#   * The total number of months included in the dataset
    header= next(csvreader)
    total_profit_loss=0
    prevProfitLoss=0
    totalChangeProfitLoss=0
    firstProfitLoss = ""
    gProfit = (0,0) # greatest profit tuple
    gLoss = (0,0) # greatest loss tuple
    monthList = list () # number of months. use dict or list or counter
    firstIteration = True
    for row in csvreader:
        if firstIteration == True:
            prevProfitLoss = int(row[1])
            firstIteration = False
        # months 
        monthList = monthList + [int(row[1])]
        # get current profit/loss
        float_total = int(row[1])
        # get change in profit/loss over last month
        
        changeProfitLoss = (float_total-prevProfitLoss)
        # record profit - greatest
        if changeProfitLoss >0 and changeProfitLoss > gProfit[1] :
            gProfit = (row[0],changeProfitLoss)
        # record loss - greatest
        elif changeProfitLoss <=0 and changeProfitLoss < gLoss[1] :
            gLoss = (row[0],changeProfitLoss)
        totalChangeProfitLoss += changeProfitLoss 
        total_profit_loss += float_total
        prevProfitLoss = float_total

#    totalChangeProfitLoss -= firstProfitLoss

    print("Financial Analysis")
    print("---------------------------------")
    print("Total Months: %d" %(len(monthList)))
    


#   * The net total amount of "Profit/Losses" over the entire period
    print("Total: $%d" %total_profit_loss)

#   * The average of the changes in "Profit/Losses" over the entire period
    #print(totalChangeProfitLoss-firstProfitLoss)
    avgChange=(totalChangeProfitLoss/(len(monthList)-1))
    print ("Average Change: %.2f" %(avgChange))

#   * The greatest increase in profits (date and amount) over the entire period
    print("Greatest increase in Profits: %s ($%d)" %(gProfit))

#   * The greatest decrease in losses (date and amount) over the entire period
    print("Greatest decrease in Profits: %s ($%d)" %(gLoss))

# * As an example, your analysis should look similar to the one below:


#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.