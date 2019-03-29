
#pybank
import os
import csv
import sys

#Path to collect data
bank_csv= os.path.join('..','pybank','pybank.csv')

total=0
date=[]
profitlosses=[]
profitlossesf=[]
newdate=[]
datemax=[]
datemin=[]
#greatestincmonth=0
#greatestdecmonth=0





#open and read csv file
with open(bank_csv,newline="") as bankcsv:
    bankread= csv.reader(bankcsv, delimiter=",")

    #Read the header row first
    csv_header= next(bankread)

    #read through each row after the header
    for row in bankread:

        date.append(row[0])
        total=total+int(row[1])
        profitlosses.append(int(row[1]))
        profitlossesf.append(int(row[1]))
        newdate.append(row[0])
        
       
    del(profitlossesf[0])
    del(profitlosses[len(date)-1])
    difference=[x-y for x,y in zip(profitlossesf,profitlosses)]
    del(newdate[0])
    difference_sum= sum(difference)
    greatestincrease=[str(max(difference))]
    greatestdecrease= [str(min(difference))]
    
   
    newlist=[(x,y) for x,y in zip(newdate,difference)]
    datemax= [x for x, y in newlist if y==max(difference)]
    datemin=[x for x,y in newlist if y==min(difference)]
    #for i in range(1,len(newdate)):
    #myset= set(newlist)
    
    #for x in mylist:
        #if str(row[1]) == greatestincrease:
        #    greatestincmonth  = str(row[0])
        #elif str(row[1]) == greatestdecrease:
         #   greatestdecmonth = str(row[0])
         #if greatestincrease in newlist:
          #   greatestincmonth=str(row[0])
         #if greatestdecrease in newlist:
          #   greatestdecmonth=str(row[0])
        

sys.stdout = open('pybank1.txt', 'w+')
print("Financial Analysis")
print("------------------------------------------------------------")
print('Total Months:'+str(len(date)))
print('Total: $'+str(total))
print('Average:'+str(round(difference_sum/(len(date)-1),2)))
#print('Greatest Increase in Profit: '+str(greatestincrease))
#print('Greatest Decrease in Profit: '+str(greatestdecrease))
print('Greatest Increase month:' + str(datemax) + str(greatestincrease))
print('Greatest Deacrease month:'+ str(datemin) + str(greatestdecrease))
sys.stdout.close()
sys.stdout=sys.__stdout__
