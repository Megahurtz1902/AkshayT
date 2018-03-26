a = [1, 3, 5, 8, 21, 1, 2, 34, 13, 55, 89]

res = []

for x in a:
    if x < 30:
        res.append(x)
res.sort()
print (res)
