# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 23:43:41 2020

@author: jayanth
"""

# Printing Intro Message
message = 'I will do it'
print(message)

# len is the funct for length of the message
print(len(message))
# [] is for accessing specific letter from string index wise starts from 0
print(message[0])
# prints letters from string from 0 till 5
print(message[0:6])
print(message[:6])  #prints letters from string from 0 till 5
# prints letters from string from 7 till end
print(message[7:])
# to convert the message into all lower case
print(message.lower())
# to convert the message into all upper case
print(message.upper())
# to count number of times a word or a letter is present in the string
print(message.count('l'))
print(message.count('will'))
# to find what index our word starts from
print(message.find('do'))
print(message.find('i'))
print(message.find('shall'))    #when it cant find something i.e. out of string
# Relace a word in the string with another
message = message.replace('I','You') 
print(message)
# To add different strings and form a sentence (for short ones)
greeting = 'Namaste'
name = 'Jayanth'
greet0 = greeting + name
print(greet0)
greet1 = greeting + ', ' + name
print(greet1)
greet2 = greeting + ', ' + name + '. Swagatham!'
print(greet2)
# Another format to combine strings (for larger sentences)
greet3 = '{}, {}. Swagatham!'.format(greeting, name)
print(greet3) # {} this is called Placeholders
# Another format to combine strings called f-Strings (available only in v3.6 or above)
greet4 = f'{greeting}, {name}. Swagatham!'
print(greet4)
greet5 = f'{greeting}, {name.upper()}. Swagatham!' #f-strings enable changing functionality directly.
print(greet5)
# To know all the attributes regarding a particular variable use this -
print(dir(name))
# To call out Help regarding the Strings i.e. to know more about it
print(help(str))
print(help(str.lower)) # Gives particular function info in Strings

