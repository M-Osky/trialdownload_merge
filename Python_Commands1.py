#Python




#                   ##############################################
#                   ##############################################
#                   ##                                          ##
#                   ##                  PYTHON                  ##
#                   ##                                          ##
#                   ##############################################
#                   ##############################################








############################################################################################
#############       Python commands, operators and sort     ################################
############################################################################################


#For some reason you cannot call scripts just with their name, you need to write "python" first




#### PRINT: each print command automatically prints in a different line
#######################################################################

print "\nYou can print like this"
no_valid_print_syntax="print(you cannot print like this)"
print "check out this wrong syntax: " + no_valid_print_syntax
print("but you can also print like this" + "\n\n")
#escape is with '\' same as in Perl
# use + to concatenate , use \ to print in the same line lines writen in multiple lines
print "This goes all " \
"in the same line"


#### VARIABLES
##############

#Python kind of like R classifies each variable in a type according to its content

string = "42.6"
integer = 42
decimal = 42.   #add a dot to define a number as a float
Boolean = True

#you can check which kind of data a variable is with type()

type(Boolean)
#either int float string...

#you can transform from one to another
string_to_float = float(string)
float_to_string = str(decimal)
decimal_to_integer = int(string_to_float)    #will not round uyp, just remove the decimal place

#you can print only strings
print string + " was converted to an integer with \'int()\' and now is: " + str(decimal_to_integer)

#You can use "%" in any print statement
#This will allow you to write a single sentence with a variable inside instead of fragments
#It works with string and integers

#Simplest: %s 
print "The Answer is %s, but what is The Question?" % integer
#we can control how many decimals to print, zeros to the left, sign of the number, etc
#d means is a signed number (positive or negative)
# a number indicates how many digits (minimum) to print
# a zero ("0") to the left of the number means fill with zeroes any empty digit
#we can concatenate many variables with multiple % and then add the variables to print in a vector
print "Is not the same to print %s than to print %03d" % (integer, integer)
#%03d => print a number (d) of three  or more digits (3), if less than 3 digits, add zeros (0) to the left.


#STRINGS
long_string = "DO NOT THINK OF IT AS DYING said Death, JUST THINK OF IT AS LEAVING EARLY TO AVOID THE RUSH"
len(long_string)     #number of characters (length)

#some string variables can be edited "on the fly" with a dot and a command to their right
#special string commands, attach them to the rigth of the string
#edit all in upper case or all in lower case!
long_string.upper()
print (long_string.lower())
#check if the variable contains only letters isalpha returns False if there are numbers or symbols
string.isalpha()

#You can call any position of a string by its index, no need for commands
second_char = long_string[1]
another=long_string[40]
from_the_end=long_string[-23]
eight_backwards=long_string[-8]
sixth_back = long_string[-6]

#you can use ranges
range = long_string[5:-1]   #from sixth character til the one before the last
range2 = long_string[1:len(long_string)]    #from the second character tll the last

print "\n\n\t\t" + second_char + another + from_the_end + eight_backwards + sixth_back + "!\n"




### OPERATORS
#############

# As usual: + - /

division_int = integer / 4
division_dec = decimal / 4
reminder_int = integer % 4
reminder_dec = decimal % 4
power_of_two = decimal**2

print "\nIf you divide " + str(integer) + " (as integer) by four you get " + str(division_int) + " and the reminder is " + str(reminder_int)
print "\nIf you divide " + str(decimal) + " (as decimal) by four you get " + str(division_dec) + " and the reminder is " + str(reminder_dec) + "\n\n"


new_integer = integer
upd_integer = integer

#maximum, minimum, absolute value (positive): max(-2,1.6,42); min(); abs(-1.5)


# you can update variables with operator and "="
#Next two lines of code arte exactly the same
new_integer = new_integer + int(decimal)
upd_integer += int(decimal)


# LIBRARIES

#reference a library for extra mathematical functions
import math

#tell python to use a function from a specific library: library_name.function
math.sqrt(integer)

#to import one specific function from a library and overwrite locals:
from math import sqrt
sqrt(integer)

#to check all functions in a module
print dir(math)

#to import all functions from a library and overwrite local use *
from math import *
print "\n\nAll functions imported\n\n"

#get the time and date library
from datetime import datetime

#get the time and date in the moment executed with '.now()'
now = datetime.now()
print now
#choose only part of it with '.month', '.year', '.hour', '.second'
#you can control how to print it and save it in a variable
today = "%02d/%02d/%04d" % (now.day, now.month, now.year)
print today










# Compare as usual with < > >= <= ==
#booleans are evaluated in order: 'not', then 'and', finally 'or'
True_variable_solved = True or not False and False == True or True and False == True or False == True
# or you can just use parenthesis like normal people

#Conditionals
# levels are not controled by keys ({}) but by the level of indent!!!

if 42 > 2:
    print "\nTwo dots as delimiter for conditionals sucks!"
elif 2 > 42:
    print "this is never going to be printed as far as the laws of the universe work"
else:
    print "This also don't gets printed"

#Command line feedback
#get information from command line with raw_input

print "\n\nNow we will ask you some questions\n"
name=raw_input("Please, write your name: ")


#define newfunctions to reuse them
#codename=""
def function_name(parameter):
    """Comments on new function better in triple quotes, it seems that way are better to use as documentation and find by 'help()' command."""
    #here goes the body of the function
    codename = "Mr. " + parameter
    print "\nWell this function just prints this text: %s\n" % codename
    return codename
#That would be it
function_name(name)

#print "It also returns %s" % codename
#print "It also returns %s" % function_name()

#end