from datetime import datetime
from person import Person


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
dolact = 5678.4576
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

# Interpolating values and objects in F-Strings.
# The syntax is simple, start string literal with a small or capital letter f and embed objects/values in curly braces
print(f"Hello, I am {name}, and {age} years old. Wrritten in f-strings")

#Embedding expressions in f-strings
print(f"{(2+4) * 6}")

# string interpolation through functions, method calls
print(f"My name is {name.upper()}, and i am {age} years old")

print(f"{[2**n for n in range(3,6)]}")

#format() method
# It takes a format specifier and value as arguments
print(format(54678.783, ".2f"))

# format specifiers can also be used with f-strings
print(f"Account Balance: {dolact:.2f}")
print(f"{name:*^20}")

# A wide range of format specifiers can be created
sep = ","
print(f"Account balance seperator: {dolact:,.2f}")
print(f"Account balance seperator: {dolact:{sep}}")

date = (13, 2, 2024)
print(f"{date[0]:03}-{date[1]:02}-{date[2]}")

day = datetime(2024, 2, 13)
print(f"Date: {day:%m-%d-%Y}")

forklift = Person("Paul", 38)
print(f"{forklift!s}")
print(f"{forklift!r}")