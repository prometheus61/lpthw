name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print ("Let's talk about %(name)s. who is %(height)d inches tall" % ({'name':'Zed Shaw' , 'height':79}))
print "He's %x inches tall." % height # hexadecimal values
print "He's %o pounds heavy." % weight # octal value
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky to get just right
print "If I add %d, %d, and %d I get %d" %(age, height, weight, age + height + weight)	