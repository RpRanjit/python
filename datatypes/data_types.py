#data types

#literal assignment
first ="Ranjit"
last ="Poudel"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first,str))

# constructor function
# pizza =str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza,str))

#Concatenation
# fullname = first + " " +last
# print(fullname)

# fullname += "!"
# print(fullname)

# casting a number to  a string
# decade =str(1555)
# print(type(decade))
# print(decade)

# statement ="I like rock music from the" + decade +"s"
# print(statement)

# multiple line
multiline ='''
Hey, how are you                          

I was just checking in.          
                            All good?

'''
print(multiline)

# Escaping special characters(use instead of multilines)
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# string methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good","ok!"))
print(multiline)

print(len(multiline))
multiline += "                                    "
multiline = "                   " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

# Build a menu
title ="menu".upper()
print(title.center(20,"="))
print('Coffee'.ljust(16, ".") + "$1".rjust(4))
print('Muffin'.ljust(16, ".") + "$2".rjust(4))
print('Cheesecake'.ljust(16, ".") + "$4".rjust(4))

print("")

#string index values
print(first[0])
print(first[-1])
print(first[1:-1])
print(first[1:])

#some methods return boolean data
print(first.endswith("t"))
print(first.startswith("T"))

#Boolean data types
myvalue = True
x=bool(False)
print(type(x))
print(isinstance(myvalue, bool)) 

# Numeric data types
# integer type
price =100
best_price =int(90)
print(type(price))
print(isinstance(best_price, int))

# Float type
grade =3.44
y =float(20.33)
print(type(grade))
print(isinstance(y, float)) 

# complex type
comp_value =5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers
print(abs(grade))
print(abs(grade * -1))
print(round(grade))
print(round(grade, 1))

import math
print(math.pi)
print(math.sqrt(64))
print(math.ceil(grade))
print(math.floor(grade))

# casting a string to a number
zipcode ="1000001"
zip_vaue=int(zipcode)
print(type(zip_vaue))
