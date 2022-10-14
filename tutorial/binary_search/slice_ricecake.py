N = 4  # 떡 개수
M = 6  # 요청한 떡 길이

dl = [19, 15, 10, 17]  # 보유한 떡 길이

# 1. 높이를 높게 설정 -> 떡이 덜 잘림 : 높이를 최대한으로 함 (최대한 덜 자르기)
# 높이의 최댓값 -> 높은 곳에서부터 탐색 필요
# -> 높이를 최댓값에서부터 점점 줄인다 (M 만큼 제공이 될 때까지)

# 2. 높이는 0 ~ 10억의 범위이므로 순차탐색에 한계가 있음 (1000만 단위 이상)
# log의 시간복잡도를 가지는 방식 필요 : 이진탐색
# -> 범위 : 전부 다 주기(0) ~ 하나도 안주기(최대) : (0, 떡길이의 최댓값)
# -> 목표값은 M으로 설정, 뺀 합계가 M보다 작아질 시에 반환 루틴 or 마저탐색

dl.sort()  # [10, 15, 17, 19]
dl_max = dl[len(dl) - 1]

# 초기 범위 : 0 ~ 최대 떡 길이
start, end = 0, dl_max

while start <= end:
    mid = (start + end) // 2

    cut = [x - mid if x > mid else 0 for x in dl]  # 자른 후
    print(cut)
    curr_lensum = sum(cut)

    result = mid

    # 너무 많이 잘라냄 : 높이를 더 높게 설정 -> start를 mid로 설정
    if curr_lensum > M:
        start = mid + 1

    # 너무 적게 잘라냄 : 높이를 더 낮게 설정 -> end를 mid로 설정
    else:
        end = mid - 1

print(result)



    

    
