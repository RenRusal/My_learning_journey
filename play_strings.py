"""this is the first ever program that i contribute to python
 it's going to be all about strings,and someways to manipulate them """

message1 = 'my name is RenRusal'                                # A string is a python datatype
message2 = ",and I'm a beginner self-taught programmer"         # we can type strings by whether using double quotes
message3 = 'this program is written using python.'              # ...or single quotes

print(message1, message2, message3)

'''let's say I want to use just one element of the string, What can I do?? '''

new_message1 = message1[11:]                 # if you run the program you'll note that new_message1 holds


print(new_message1, '.')                     # ...only a slice of the variable message1 this method is called slicing

"""you can think of a string more of a combination of characters (including blank-space).
each of the characters is indexed with an integer number (positive and negative). 
for example: the string 'Hello' can be seen as 

| H | e | l | l | o |
_____________________
| 0 | 1 | 2 | 3 | 4 | 
_____________________
|-5 |-4 |-3 |-2 |-1 |
"""
new_message2 = message2[-4]                  # the variable new_message2 will hold only one character this method

print(new_message2)                          # ... is called indexing

""" we can manipulate strings using methods """

string = "Hello, World "

print(string.count('RenRusal'))           # .count() is used to count the number of times an argument exist in a string
print(string.count('Hello'))
print(string.count('hello'))
""" 'hello' and 'Hello' are different, in this case
     we say that python is case-sensitive"""

print(string+ ' My name is RenRusal')    # we call this method concatenation

print('Hi my name is {}'.format('RensRusal'))

print(string.upper())
print(string.lower())
