# 전체 데이터의 개수가 100만 개 이하일 땐 완전탐색이 적절

n = int(input())

counter = 0
for hour in range (n + 1):
  for min in range(60):
    for sec in range(60):
      if '3' in str(hour) or \
          '3' in str(min) or \
          '3' in str(sec):
          counter += 1

print(counter)
  