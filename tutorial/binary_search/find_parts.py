'''
import sys

N = int(sys.stdin.readline().rstrip())
have = sys.stdin.readline().rstrip().split()
M = int(sys.stdin.readline().rstrip())
req = sys.stdin.readline().rstrip().split()
'''

# 재고
N = 5
have = [8, 3, 7, 9, 2]

# 요청
M = 3
req = [5, 7, 9]


# 이진 탐색
def bs(start, end, arr, obj):
    if start > end:
        return None

    mid = (start + end) // 2
    if obj == arr[mid]:
        return arr[mid]
    elif obj < arr[mid]:
        return bs(start, mid - 1, arr, obj)
    else:
        return bs(mid + 1, end, arr, obj)


# 정렬 필요!!
have.sort()

# 요청 목록 순회, 검색
for i in range(M):
    obj = req[i]
    res = bs(0, len(have) - 1, have, obj)
    if res == None:
        print("no", end=" ")
    else:
        print("yes", end=" ")
