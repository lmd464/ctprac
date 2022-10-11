# N : 리스트 크기 / M 번 더함 / K : 최대연속개수
# raw = map(int, input().split(" "))
# list = map(int, input().split(" "))
raw = [5, 8, 3]
list = [2, 4, 5, 4, 6]
N, M, K = raw[0], raw[1], raw[2]

# 정렬 -> 1번째, 2번째로 큰거 pop
list.sort()
first = list.pop()
second = list.pop()
counter = 0
result = 0

for _ in range(M):
    if counter == 8:
        break
    for _ in range(K):
        if counter == 8:
            break
        result += first
        counter += 1
    result += second
    counter += 1

print(result)
