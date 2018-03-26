
a = [1, 4, 2, 6, 5, 34, 87, 45, 2, 5]
b = [23, 45, 34, 3, 7, 2, 1]
c = []

# a.sort()
# b.sort()

for x in a:
    if x in b: c.append(x)

print(c)

# Remove Duplicate Values from the list
c.sort()
for x in range(1, len(c)-1):
    if c[x] == c[x-1]: c.pop(x)

print(c)
