# 최대한 많이 나눠야 빨리 작아짐
x, div = map(int, input().split(" "))

count = 0
while x > 1:
  if x % div == 0:
    x /= div
    count += 1
  else:
    x -= 1
    count += 1

print(count)
  
