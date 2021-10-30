mydict = {
    "fruit":"apple",
    "year":"2021",
    "Month":"October"
}

print(mydict["year"])

# output is 2021
# We can access dictionary's value using the key.
# In this case, year is key and 2021 is value

mydict["new key"] = "new value"

print(mydict)

# The output is the previous dic with additional key "new key" with value "new value"

# However, python do not allows us to create duplicate key, if we try it then the old value of the key
# is replaced by the new value

mydict["Month"] = "December"

print(mydict)

# Output
# {'fruit': 'apple', 'year': '2021', 'Month': 'December', 'new key': 'new value'}