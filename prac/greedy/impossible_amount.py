N = 5
li = [3, 2, 1, 1, 9]

# 1원부터 점점 올리면서 가능한 지 탐색함 (최솟값을 구해야 하므로)
# 화폐 단위는 가능한 한 큰 것부터 넣어봄 -> 큰 덩어리 먼저 넣고, 작은 걸로 채우기
li.sort(reverse=True)

obj_money = 1    # 대상 화폐량
while True:
    temp_money = obj_money    # 동전값만큼 뺄 임시변수
    possible = False    # 가능 여부

    # 가능한 큰 동전부터 빼면서, 나머지가 0이 될 경우 가능 / 아니면 불가능
    for coin in li:
        if temp_money >= coin:
            temp_money -= coin
        if temp_money == 0:
            possible = True
            break
            
    # 남은 돈이 0이 아니면 불가능하므로 현재 obj_money가 구하는 값임
    if not possible:
        break
    else:
        obj_money += 1

print(obj_money)