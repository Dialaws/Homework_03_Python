# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 12:33:44 2019

@author: diala
"""
#pybank
import os
import csv
import sys

#Path to collect data
bank_csv= os.path.join('..','pybank','pybank.csv')

total=0
date=[]
newdate=[]
datemax=[]
datemin=[]
newdifference=[]
firstvalue=0
skip=True




#open and read csv file
#open the path to csvfile and read the csv file
with open(bank_csv,newline="") as bankcsv:
    bankread= csv.reader(bankcsv, delimiter=",")

    #Read the header row first
    csv_header= next(bankread)

    #read through each row after the header
    for row in bankread:
        #skip the first value as we do not need to calculate it
        #calculate the difference between each moth and save it in newdifference list
        #get the date in date list
        #calculate the total
        #set the skip to false
        if(skip):
            firstvalue= int(row[1])
            newdifference.append(int(row[1])-firstvalue)
            firstvalue=int(row[1])
            date.append(row[0])
            total=total+int(row[1])
            newdate.append(row[0])
            skip=False
        #do the same for the whole rows without skipping the first value    
        else:
            newdifference.append(int(row[1])-firstvalue)
            firstvalue=int(row[1])
            date.append(row[0])
            total=total+int(row[1])
            newdate.append(row[0])
            
           
           #create a newlist that has both the newdate and newdifference
           #get the date for the max difference
           #get the date for the min difference
         
    newlist=[(x,y)for x,y in zip(newdate,newdifference)]
    datemax=[x for x, y in newlist if y==max(newdifference)]
    datemin=[x for x, y in newlist if y==min(newdifference)]
       

    difference_sum= sum(newdifference)
    greatestincrease=[str(max(newdifference))]
    greatestdecrease= [str(min(newdifference))]
    
   

        
        


print("Financial Analysis")
print("------------------------------------------------------------")
print('Total Months:'+str(len(date)))
print('Total: $'+str(total))
print('Average Change:'+'$'+str(round((difference_sum/(len(date)-1)),2)))
#print('Greatest Increase in Profit: '+str(greatestincrease))
#print('Greatest Decrease in Profit: '+str(greatestdecrease))
print('Greatest Increase in Profit:' + str(datemax) + str(greatestincrease))
print('Greatest Deacrease in Profit:'+ str(datemin) + str(greatestdecrease))

