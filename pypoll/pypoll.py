#pypoll
import os
import csv

totalvotes=0
candidateset=set()
candidatelist=[]
summary=[]
khantotal=0
litotal=0
correytotal=0
otooleytotal=0


#open path to csv file 
csvpath= os.path.join('..','pypoll','pypoll.csv')
#read the csv file 
with open(csvpath,newline='')as csvpollfile:
    csvpollread= csv.reader(csvpollfile,delimiter=',')
#skip the header
    csvpollheader=next(csvpollread)
#go through the rows and 
#make a list for the candidates
#make a set for the candidates names
#calculate the total votes for each candidate

    for row in csvpollread:
        totalvotes=totalvotes+1
        candidatelist.append(row[2])
        candidateset.add(str(row[2]))
        if "Khan" == row[2]:
            khantotal=khantotal+1
        elif "Li" == row[2]:
            litotal=litotal+1
        elif "Correy"== row[2]:
            correytotal=correytotal+1
        elif "O'Tooley" == row[2]:
             otooleytotal=otooleytotal+1
#make a list for the total values
summary.append(khantotal)
summary.append(litotal)
summary.append(correytotal)
summary.append(otooleytotal)
#sort the list and take the highest value
summary.sort()
greatestvalue=summary[3]
#compare the highest value with each candidate total so we get the winner
if greatestvalue==khantotal:
     winner="Khan"
elif greatestvalue==litotal:
       winner="Li"
elif greatestvalue==correytotal:
       winner="Correy"
elif greatestvalue==otooleytotal:
       winner="O'Tooley"
    
    
#calculate the percentage for each candidate
    
khanper= round(khantotal/totalvotes *100,2) 
liper= round(litotal/totalvotes *100,0)
correyper= round(correytotal/totalvotes *100,0)
otooleyper=round(otooleytotal/totalvotes *100,0) 


print("Election Results")
print("------------------------------------------------")
print("Total Votes: "+str(totalvotes))
print("------------------------------------------------")
print("Khan:"+str(khanper)+str("%") + str("(") +str(khantotal)+str(")"))
print("Correy:" +str(correyper)+str("%") +str("(")+str(correytotal)+str(")"))
print("Li:"+str(liper)+str("%")+str("(")+ str(litotal)+str(")"))
print("O'Tooley:" +str(otooleyper)+str("%")+str("(")+str(otooleytotal)+str(")"))
print("-------------------------------------------------")
print("Winner:"+str(winner))

