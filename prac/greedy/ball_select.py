N = 8
M = 5
ball_weights = [1, 5, 4, 3, 2, 4, 5, 2]

ball_weights.sort()

result = 0
for i in range(len(ball_weights)):
    for j in range(i + 1, len(ball_weights)):
        # i, j : 1, 2번째 공
        if ball_weights[i] != ball_weights[j]:
            result += 1

print(result)