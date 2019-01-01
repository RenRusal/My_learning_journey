'''This time it's going to be all about integers and floats'''

# what are ints and floats

print(type(12))        # the output would be 'class <int>' int stand for integer
print(type(12.1))      # this would give us 'class <float>' 
print(type(12.0))      # no!! this isn't an integer it's a float
print(type('13'))      #and this is also not an int it's string type 
#we can change the type of an expression with some functions 
var1 = 12.1
var2 = '14.5'

print(int(var1))      # the int function will change the type of the variable to an integer so the resulting output would be 12
print(int(var2))      # the same case here, the output is : 14 not 14.5 
print(float(13))      # the float function will change the type of the variable to a float so the resulting output would be 13.0
print(str(15.4))      # the str function will change the type of the variable to a string so the resulting output would be '15.4'

# Arithmetic Operators: 

# Addition: 3 + 2 
# Subtraction: 3 - 2 
# Multiplication: 3 * 2 
# Division: 3 / 2 
# Floor Division: 3 // 2 
# Exponent: 3 ** 2 
# Modulus: 3 % 2

# Comparisons: 

# Equal: 3 == 2 
# Not Equal: 3 != 2 
# Greater Than: 3 > 2 
# Less Than: 3 < 2 
# Greater or Equal: 3 >= 2 
# Less or Equal: 3 <= 2e o a 

''' just try to print those examples stated beside the notations
I just felt lazy. '''
                                                                                 
''' What If we wanted to change a string-type expression to an integer or a float.'''

var_3 = '1452'             #note: you can only convert number string-types not letters or words
var_4 = int(var_3)         #change the type of the variable to an integer
var_5 = float(var_3)       #change the type of the variable to a float

print(var_4+9)             # apparently this would leave us with a nmuber equal to 1461
print(var_5)               # output: 1452.0
print(var_5/2)             #output:  726.0
print(var_5  == var_4) #output: True
print(var_5/2  == var_4/2)
''' the same goes if we want to change an integer or float type to a string using the str function.
