## Argument Passing

Arguments are turned to list of strings and assigned to argv variable->sys module
Access list: import sys
sys.argv[0]->empty string ie when no script or arg is passed.
when scriptname == '-', sys.argv[0]  is set to '-'(standard input), 
-c sets sys.argv[0] -> '-c' or -m module set sys.argv[0] -> fullname of located module

## Interactive Mode

Commands read from a tty(Interactive mode). >>>(primary prompt) it prompts for the next command, while (...)secondary prompt is for continuation lines
Note: Continuation lines are needed when entering a multi-line constructs
exe01.py used used in illustrating this

## The Interpreter and its Environment

Python source files encoded in UTF-8(characters of most prog languages can be used simultaneously in string literals, comments and identifiers). To display all this characters properly, editor must recognize file is UTF-8 and font of all characters are supported
Note: To declare an encoding other than the default, a comment should be added to the first line of the file Eg.

### -*- cp1252 -*-(Windows-1252 encoding to be used)

Although one exception of *first-line-rule* is the case where file starts with a shebang
Eg. #!/usr/bin/python3 -> In this case it appears on the second line

## An Informal Introduction to Python

A comment may appear at the start of a line, or after a whitespace or code but never within a *string literal*. A hash character within a string literal is a hash character.

## Using python as a Calculator

Note: Division operator always return a floating number in cases of remainders.
// -> Floor division
% -> remainder value
** -> powers
= -> assign value to variable
Note: In interactive mode, the last printed expression is assigned to the '_' variable. This is handy in calculations or situations where last value is easily used or recalled


Error: If a variable is not defined.
NameError:name 'var' is not defined

## Text 

Python can also manipulate text, strings, numbers & characters enclosed in single ' ' or double " " quotes
To quote a quote, either escape it with \ or uses the other type of quoation mark
print() outputs a more readable output by excluding single quotes and printing the escaped characters
If we dont want \ to be interpreted, raw strings can be used by adding r before the first quote.(A raw string may not end in odd number of \ characters)
End of lines are automatically included in a string, although it is possible to prevent this by adding \ at te end of the line
String concatenation -> + operator is used
String duplication -> * operator is used
Two strings in quotes side by side are automatically concatenated. This is particularly useful when long strings are to be broken
Variables and string in quotes cannot be concatenated except '+' is used with it
Characters in strings can be accessed using indexes. Indexes may also be negative.(Starts counting from the right.)
Slicing is also supported to get characters of a string. If the first character is ommited, it is assumed to be 0, while if the second number is omitted, it defaults to the size of the string
Note: s[:i] + s[i:] -> always equals string
For non-negative slice indices, the difference between both numbers is the length
Note: **Python strings are immutable. Values cannot be assign through index** eg
n[0] = 'J' (Error: 'str' object does not support item assignment)
Note **len() returns the length of a string**

## F-STRINGS

exe01.py(coding examples)
modulo operator since the beginning!
functionality: conversion specifiers (%s) which consist of %->conv specifier & s->conv type
Interpolating strings in tuples eg ("name",age)-> TypeError: not all arguments converted during string formatting
this can be fixed by enclosing data in single item tuple eg (("name", age),)

## str.format()

exe01.py(coding examples)
they can be used by providing replacement fields using curly brackets in string literals. It matches them with arguments in format() by positional order.
The order can be specified manually, by specifying using zero-based indexes in replacement fields
keywords arguments can also be used

## f-strings(formatted string literals)

f-strings are string literals that have an f before the opening quotation mark. This behaviour turns f-string into a string interpolation tool