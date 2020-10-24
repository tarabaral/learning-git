# Declaring a variable and initializing it
f=0
print(f)

# Re-declaring a variable works in python
f="abc"
print(f)

# ERROR! variables of different types can not be combined
print("This is a string" + 123)

# But the variables of same type can be combined
print("This is a string" + str(123))

# Global vs local variable
f="Global value"

def myFunction():
  f="local value"
  print(f)
  
someFunction()
print(f)


## Here, this piece of code outputs following
# local variable
# Global variable

## PRO-TIP!
# global f => to use global variable and change its value accordingly
# del f deletes the decleration of the variable. It is used for undefining variable in real time
