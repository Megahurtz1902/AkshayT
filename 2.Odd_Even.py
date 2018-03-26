
x = raw_input("Think of a number and type it here...: ")

try:
    x = int(x)
except:
    print "Oh No... I wanted a number :("
    print "Exiting..."
    exit()

y=x%2
if y == 0:
    print "Even Number Inputted"
    #Extra Part-1
    y=x%4
    if y==0:
        print "The number is also divisible by 4!"
else:
    print "Odd Number Spotted"

# Extra Part 2

try:
    (check, num) = input("Enter two number separated by Comma [eg. 6, 3]")


try:
    check = int(check)
    num = int(num)
except:
    print "One of the numbers is not really a number. Kindly fix it to stop seeing such messages"
    exit()

z=check%num

if z == 0:
    print check, "is a perfect multiple of", num
else:
    print check, "is not even remotely related to", num
