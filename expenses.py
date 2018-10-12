import re
import urllib2
import csv
import httplib
import sys
import getopt
from support import *
import datetime

file1 = open('expenses1.txt','r')
content=file1.read().splitlines()
file1.close()


#print content

if(len(sys.argv)<2):
	calc(content)
if(len(sys.argv)>2):
	if(sys.argv[1] == "check"):
		calc(content);
	if(sys.argv[1] == "add"):
		if(len(sys.argv)>2):
			try:
				val = float(sys.argv[2])
			except ValueError:
				print("The second number is not an argument")
		addRecord("test",1)
	
#getExchangeRate()
#print("\n"+months)

#print("Average spending per day is %.2f" %(fullsum/(l)))
#print("Projected spending per month is %.2f" %((fullsum/(l))*30))
#print("Money saved relative to goal %.2f" %(l*22.28-fullsum))
#print("Money to be saved on track with average %.2f" %((92-l)*(22.28-fullsum/l)))
#print("Projected total of saved money %.2f" %((l*22.28-fullsum)+(92-l)*(22.28-fullsum/l)))

	
#getExchangeRate()
