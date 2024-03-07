import time, math

number = int(input("Enter a number: "))
delay = int(input("Enter delay ms: "))/1000

time.sleep(delay)
print(math.sqrt(number))