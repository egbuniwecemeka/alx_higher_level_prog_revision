my_name = False
if my_name:
    print("Software Engineer")
else:
    print("Python Session")
    
# String interpolatio -> modulo operator
name = "Chuks"
print("my name is %s" % name)

# For more than one object(Using a tuple to group objects)
# Note: a string and integer have been used. The %s specifier converts integers to string
age = 30
account = 40**5
print("name: %s, age: %s, accountBal: %s" %(name, age, account))


# dictionaries can also be use
print("%(name)s, %(age)s, %(bal)s," % {"name":"Emma", "age":25, "bal": account})

"""
    When you use the % operator for string interpolation, you can use conversion specifiers. 
    They provide some string formatting capabilities that take advantage of conversion types, 
    conversion flags, and some characters like the period (.) and the asterisk (*). 
    Consider the following example: 
"""
dolact = 5678.45
exp = 2
company = "FC"
print("Balance: $%.2f" % dolact)

print("name: %15s" % (name))

# str.format()
print("Hello, I worked at {1}, for {0} years. Lol!!!".format(company, exp))

# keyword argument
print("Myy name is {name}, and I am {age} years old".format(name="Junior", age=35))

# dictionaries
values = {"name":"Junior", "age":29}
# ** dictionary unpacking operator
print("My name is {name}, and i am {age} years old".format(**values))

# .format also accepts string specifiers
print("${:.2f}".format(5467.8790))

print("{:=^20}".format("Centred name"))