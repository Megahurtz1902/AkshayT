a = raw_input("Enter a String: ")
a = str(a)

if a == a[::-1]:
	print ("Palindrome Spotted!")
else:
	print ("This ain't no Palindrome")