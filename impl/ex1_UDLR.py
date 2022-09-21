# 이동 범위는 (1 ~ n, 1 ~ n)
# 범위 벗어나지 못함

# 시작좌표 (1, 1)
cur_pos = [1, 1]

# 이동
def move(dir, n):
  if dir == "L":
    if cur_pos[1] == 1:
      return
    cur_pos[1] -= 1
    
  elif dir == "R":
    if cur_pos[1] == n:
      return
    cur_pos[1] += 1

  elif dir == "U":
    if cur_pos[0] == 1:
      return
    cur_pos[0] -= 1

  elif dir == "D":
    if cur_pos[0] == n:
      return
    cur_pos[0] += 1


input_n = int(input())
input_dirs = input().split(" ")

for input_dir in input_dirs:
  move(input_dir, input_n)

print(str(cur_pos[0]) + " " + (str(cur_pos[1])))
  
