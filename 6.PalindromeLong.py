a = raw_input("Enter a string :")
a = str(a)

c = range(0, len(a))
c.reverse()
b=""

for i in c:
    b = b+a[i]

if b == a:
    print ("Yesss, that's a Palindrome!")
else:
    print ("Nah, not a Palindrome. Next time, learn what is a Palindrome before executing me :X ")
