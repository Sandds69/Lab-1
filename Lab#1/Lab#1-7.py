x = "awesome"

def myfuc():
    print("Python is " + x)

myfuc()

x = "awesome"

def myfunc():
  x = "easy"
  print("Python is " + x)

myfunc()

print("Python is " + x)

def myfunc():
  global x
  x = "hard"

myfunc()

print("Python is " + x)