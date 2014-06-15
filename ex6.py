#x can be a string with a formatted with an integer number
x = "There are %d types of people." %10
#another variable as a string
binary = "binary"
#Assigning string to another variable
do_not = "don't"
#Another variable with strings, which inturn has strings. 
y = "Those who know %s and those who %s." % (binary, do_not)

#Printing string by calling the variable
print x
#Printing string by calling the variable
print y

#Print sentence with a formatter associated with a variable
print "I said: %r." % x
#Printing a string with another string associated with an variable
print "I also said: '%s'" %y

#Assigning a variable with a state
hilarious = False

#Assigning a variable to a string that has an unassigned formatter
joke_evaluation = "Isn't that joke so funny?! %r"

#Printing the variable complete with a formatter variable which in turn is a string
print joke_evaluation % hilarious

#Assign a string to a variable
w = "This is the left side of..."
#Assign a string to a variable
e = "a string with a right side."

#You print two strings side by side by using + sign
print w + e