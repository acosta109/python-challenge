import os
import csv

#create path to CSV file
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#open CSV file

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    totalProfit = 0
    totalMonths = 0
    deltaArray = []
    avgDelta = 0
    #skip header row 
    next(csvreader)

    for rows in csvreader:
        totalProfit += int(rows[1])
        totalMonths +=1

        #track change in profit int(rows[1]) is the current month's profit 
        # and lastProfit is last months profit
        if totalMonths > 1:
            deltaArray.append(int(rows[1]) - lastProfit)

        lastProfit = int(rows[1])    

    avgDelta = round(sum(deltaArray)/len(deltaArray), 2)

    #print(avgDelta) #debugging code
    #print(lastProfit) debugging code
    #print(totalProfit) #debugging code 
    #print(totalMonths) #debugging code
    #print(max(deltaArray)) #debugging code
    #print(min(deltaArray)) #debugging code

    print("Financial Analysis \n")
    print("---------------------------- \n")
    print(f'Total Months: {totalMonths}\n')
    print(f'Total: ${totalProfit}\n')
    print(f'Average Change: ${avgDelta}\n')
    print(f'Greatest Increase in Profits: {max(deltaArray)}\n')
    print(f'Greatest Decrease in Profits: {min(deltaArray)}\n')