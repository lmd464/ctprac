temp = list(map(int, input().split(" ")))
row_count, col_count = temp[0], temp[1]

# 각 줄을 입력받아 2차원배열로 저장
arr = []
for _ in range(row_count):
  arr.append(list(map(int, input().split(" "))))

# 각 행별로 min을 구하고, 가장 큰 min 선택
min_num = -1
for i in range(row_count):
  row_min = min(arr[i])
  if min_num < row_min:
    min_num = row_min

print(min_num)
