print("This is the database module and python calls it ()".format(__name__))

from blood_calculator import *
# Using a star is the easiest but the problem is that it is difficult to keep your work organized 
# Star is considered poor practice 
# In your career as a coder you are more likely to spend 2-3x as much time reading code as you are writing it


# from analysis import check_HDL
# if you have two packages and within them you have to lines called the same. Python will only run the first one
# To help with this it is better to just import the module

HDL_value = 55

classificication = check_HDL(HDL_value)
# otheranswre analysis.check_HDL()
# how you could call this second one
# but an alias like "bc" is better too
print("55 is ()".format(classificication))
x = check_LDL(200)

