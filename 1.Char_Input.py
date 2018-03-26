
try:
    x = input("Enter some number: ")
except:
    print ""
    print "Your input is utterly unacceptable!"
    print ""
    print "Please enter either a Valid number or text in single quotes"
    x = None
    
print "Entered Number is : ", x