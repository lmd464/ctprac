N = 5
have = [8, 3, 7, 9, 2]

M = 3
req = [5, 7, 9]

have = set(have)

for r in req:
    if r in have:
        print("yes", end=" ")
    else:
        print("no", end=" ")
