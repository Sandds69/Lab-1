from datetime import *

firstInp = input("Enter Date in day.month.year format\n")
secondInp = input("Enter Date in day.month.year format\n")
firstDate = datetime.strptime(firstInp, "%d.%m.%Y")
secondDate = datetime.strptime(secondInp, "%d.%m.%Y")

delta = abs(secondDate - firstDate)
days = delta.days


print(days*24*60*60)