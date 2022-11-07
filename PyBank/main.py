# modules
import os
import csv
# set path to to the csv:
budget_csv = os.path.join('/Users/terryschoch/Desktop/Data_Analytics/python-challenge/Resources/budget_data.csv')

months = []
profit_loss = []
profit_loss2 = []

#Open the file, Specify the variable to hold the contents & account for header
with open(budget_csv) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(reader) 
    # loop for info then add months & profit and losses to lists
    for row in reader:
        months.append(row[0])
        profit_loss.append(row[1])
        profit_loss2.append(row[1])
    
# prepare and convert profit_loss1 & 2 for subtraction
profit_loss2.pop(0)
profit_loss2.append(profit_loss[(len(profit_loss) - 1)])
newprofit_loss = [int(item) for item in profit_loss]
newprofit_loss2 = [int(item) for item in profit_loss2]
                                
# create list to hold individual monthly changes and for loop to find them
changes = list()
for i in range(len(newprofit_loss)):
     monthly_change = newprofit_loss2[i] - newprofit_loss[i]
     changes.append(monthly_change)
# print(profit_loss2)
# print(changes)

# Print summaries: Header, total number of months, total profit/loss
print("Financial Analysis")
print("-" * 30)
# total_months = len(months)
# print("Total Months: " + str(total_months))
print("Total Months: " + str(len(months)))
# total_profit = sum(newprofit_loss)
# print("Total: $" + str(total_profit))
print("Total: $" + str(sum(newprofit_loss)))
average_change = round(sum(changes)/(len(changes) - 1), 2)
print("Average Change: $" + str(average_change))
# determine max increase, its index and corresponding months; repeat for decrease - print results
grincrease = max(newprofit_loss)
increase_index = newprofit_loss.index(grincrease)
grincrease_month = months[increase_index]
print("Greatest Increase in Profits: " + str(grincrease_month) + " ($" + str(grincrease) + ")")
grdecrease = min(newprofit_loss)
decrease_index = newprofit_loss.index(grdecrease)
grdecrease_month = months[decrease_index]
print("Greatest Decrease in Profits: " + str(grdecrease_month) + " ($" + str(grdecrease) + ")")



# changes = list()
# for item1, item2 in zip(newprofit_loss, newprofit_loss2):
#     changes.append(item1 - item2)
#     print(changes)

    # changes = int(profit_loss[0]) - int(profit_loss[1])
    # print(changes)
    # # n = 0
    # for changedamount in newprofit_loss[n]:
    #     (newprofit_loss[n] - newprofit_loss[1])
            

    #     print(changes)

# alternatively you can do the index and result in one line as below
# grincrease = newprofit_loss[newprofit_loss.index(max(newprofit_loss))]
# print max increase month and amount


# grincrease = max(newprofit_loss)
# print("Greatest Increase in Profits: $" + str(grincrease))
    
# grdecrease = min(newprofit_loss)
# print("Greatest Decrease in Profits: $" + str(grdecrease))


# print(newprofit_loss)
# print(max(newprofit_loss))
# print(newprofit_loss[index])
# print(months[index])
 

# for profit_index in range(len(profit_loss)):
#     grincrease = (max(profit_loss[profit_index]))
#     grincrease_month = (months[profit_index])
# print("Greatest Increase in Profits: " + grincrease_month + " ($" + str(grincrease) + ")")



# print("Average Change: " + average_change)