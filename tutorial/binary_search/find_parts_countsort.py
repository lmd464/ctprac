N = 5
have = [8, 3, 9, 7, 2]

M = 3
req = [5, 7, 9]

# freq list
freq = [0] * 20

for i in range(len(have)):
    freq[have[i]] += 1

for i in range(len(req)):
    if freq[req[i]] > 0:
        print("yes", end=" ")
    else:
        print("no", end=" ")
