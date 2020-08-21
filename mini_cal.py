print("Enter current date")
cd=input()
print("Enter current month")
cm=input()
print("Enter current year")
cy=input()
print("Enter Birth date")
bd=input()
print("Enter Birth month")
bm=input()
print("Enter Birth year")
by=input()
month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
if (bd>cd):
	cm=cm-1
	cd=cd+month[bm-1]
if (bm>cm):
	cy=cy-1
	cm=cm+12
  
calyear=int(cy)- int(by)
calmon=int(cm)-int(bm)
caldays=int(cd)-int(bd)

print("\nYour age is:",caldays,end = '')
print(" Days",calmon, end = '')
print(" Month",calyear, end = '')
print(" Year")

