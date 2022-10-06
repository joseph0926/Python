name = "Kim"
age = 25

print("t1: " + name + str(age))

def printNameAge():
  print("t2: " + name + str(age))

printNameAge()

def ageHandler():
  return age - (age % 10)

print(ageHandler())