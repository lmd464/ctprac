N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A 오름차순, B 내림차순 정렬 후
# 맨 앞 인덱스부터 탐색하며 같은 위치 바꿔치기 하면 됨
# A의 최솟값과, B의 최댓값을 교환
A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break

print(sum(A))
