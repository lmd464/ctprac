# column의 알파벳을 숫자로 변환
alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
num_list = [1, 2, 3, 4, 5, 6, 7, 8]

# 현재 위치 입력받아 숫자화
file_input = input()
r = int(file_input[1])
c = num_list[alpha_list.index(file_input[0])]

# 8가지 이동 경우의 수 세기
counter = 0

# 이동 가능한 경우를 리스트로 묶기
movements = [(-2, -1), (-2, 1), (2, -1), (2, 1), 
            (-1, -2), (-1, 2), (1, -2), (1, 2)]


# *** 이동 "가능" 한 경우의 수 ***
for movement in movements:
  if r + movement[0] <= 8 and r + movement[0] >= 1 \
    and c + movement[1] <= 8 and c + movement[1] >= 1:
    counter += 1

print(counter)



'''
# 노가다 : 이렇게 하지 말 것

if r + 2 <= 8 and c + 1 <= 8:
  counter += 1
if r + 2 <= 8 and c - 1 >= 1:
  counter += 1
if r - 2 >= 1 and c + 1 <= 8:
  counter += 1
if r - 2 >= 1 and c - 1 >= 1:
  counter += 1
if r + 1 <= 8 and c + 2 <= 8:
  counter += 1
if r + 1 <= 8 and c - 2 >= 1:
  counter += 1
if r - 1 >= 1 and c + 2 <= 8:
  counter += 1
if r - 1 >= 1 and c - 2 >= 1:
  counter += 1
'''