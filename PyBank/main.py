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
    dateArray = []
    avgDelta = 0
    #skip header row 
    next(csvreader)

    for rows in csvreader:
        totalProfit += int(rows[1])
        totalMonths +=1
        
        #the first time we go get a change in price, track it

        #track change in profit int(rows[1]) is the current month's profit 
        # and lastProfit is last months profit
        if totalMonths > 1:
            deltaArray.append(int(rows[1]) - lastProfit)
            dateArray.append(str(rows[0]))

        lastProfit = int(rows[1])    

    avgDelta = round(sum(deltaArray)/len(deltaArray), 2)
    greatestIncIndex = deltaArray.index(max(deltaArray))
    greatestDecIndex = deltaArray.index(min(deltaArray))

    incDate = dateArray[greatestIncIndex]
    decDate = dateArray[greatestDecIndex]

    
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
    print(f'Greatest Increase in Profits: {incDate} (${max(deltaArray)})\n')
    print(f'Greatest Decrease in Profits: {decDate} (${min(deltaArray)})\n')

with open('financial_results.txt', 'w') as file:
    file.write("Financial Analysis \n")
    file.write("---------------------------- \n")
    file.write(f'Total Months: {totalMonths}\n')
    file.write(f'Total: ${totalProfit}\n')
    file.write(f'Average Change: ${avgDelta}\n')
    file.write(f'Greatest Increase in Profits: {incDate} (${max(deltaArray)})\n')
    file.write(f'Greatest Decrease in Profits: {decDate} (${min(deltaArray)})\n')
