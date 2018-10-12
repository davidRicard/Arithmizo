def calc(content):
	l = 0
	weeklysum = 0.0
	fullsum = 0.0
	daily = 0.0
	previous = 0.0
	m = 0
	months = ""
	for j in content:
	
		templist = j.split(";")
		daily = float(templist[1])
		m = m+1
		weeklysum = weeklysum+daily
		fullsum = fullsum+daily
		if(m%7 == 0):
			m = m + 1
			print("Weekly expenses for week %d are %.2f"%(m,weeklysum))
			weeklysum = 0
		if(m%30 == 0):
			months = months+("Month %d Expenses are %.2f \n"%(l/30,fullsum-previous))
			previous = fullsum
		
	print("The sum of your expenses is %.2f for %d days" %(fullsum,m))

def addRecord(date, amount):
	print("Success")
