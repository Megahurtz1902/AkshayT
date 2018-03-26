x = input('Enter a number for checking available divisors: ')

try:
    x = int(x)
except:
    print(x, "isn't a number. Execution cannot continue, sorry!")
    exit()

# res = []
# i = 1
#
# while i < x-1:
#     if x%i == 0:
#         res.append(i)
#     i=i+1
#
# print(res)

rng = range(1, x+1)
res = []

for i in rng:
    if x%i == 0: res.append(i)

print("The divisors of", x, "are:", res)

# for p in res: print(p)
