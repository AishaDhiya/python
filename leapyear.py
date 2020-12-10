print("to check the given year is a leap year or not")
y=int(input("enter a year"))
if y%400 ==0 or(y%100 != 100 and y%4 ==0):
	print(y,"is a leap year")
else:
	print(y,"is not a leap year")	

