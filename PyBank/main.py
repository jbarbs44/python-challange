import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_data_csv) as csv_file:
    
    # create a csvreader
    csv_reader = csv.reader(csv_file, delimiter= ",")

    header_row = next(csv_reader)
 
    #empty lists    
    date_list=[]
    budget_list=[]
    Monthly_Change =[] 
    previous = 0

    #print("Header row:" + str(header_row))
    #Assign values to the empty lists
    for row in csv_reader:
        date_list.append(row[0])
        Total_Months=len(date_list)
        budget_list.append(int(row[1]))
    for i in range(len(budget_list)- 1):
        Monthly_Change.append(int(budget_list[i+1]-budget_list[i]))
        Average_Change = round(sum(Monthly_Change)/len(Monthly_Change),2)
    
    #find the greatest increase & decrease
    Greatest_Increase = max(Monthly_Change)
    Greatest_Decrease = min(Monthly_Change)

    #Use index to find the month
    Greatest_Increase_Month = Monthly_Change.index(max(Monthly_Change))+1
    Greatest_Decrease_Month = Monthly_Change.index(min(Monthly_Change))+1


Net_Total= sum(budget_list)


print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: ${Net_Total}")
print(f"Average Change: ${Average_Change}")
print(f"Greatest Increase in Profits: {date_list[Greatest_Increase_Month]} (${(Greatest_Increase)})")
print(f"Greatest Decrease in Profits: {date_list[Greatest_Decrease_Month]} (${(Greatest_Decrease)})")

