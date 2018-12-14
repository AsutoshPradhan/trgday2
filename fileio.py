import datetime;
import time;
day= str(datetime.datetime.now())

#print (day)


f = open("C:\Users\asupradhan\Documents\Landing\ProposalInitiatives\COE\Training\Deploy\UAT\log.txt", "a")

f.write(day)

f.write("\n")
f.close()


f=open("log.txt")
x=f.read()
print(x)
f.close()

