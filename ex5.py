name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %c inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair" % ( eyes, hair)
print "His teeth are usually %s depending on the coffee." %teeth

#this is line is tricky, try to get it exactly right
print "If I add %d, %d, and %d. I get %d." %(age, height, weight, age + height + weight)

centi = 10  #To convert 10 centimeters to inches
pound = 100 #To convert 100 pounds to kg

print "10 centimeters in inches is %r " %(centi / 2.54) #Printing the converted value using formatter
print "100 pounds in kg is %r" %(pound / 2.20)  #Printing the value in kg using general formatter
