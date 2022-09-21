# N행 M열
# 열 수 , 행 수 , 현재 방향
# 육지 : 0, 바다(못감) : 1
N, M = map(int, input().split())
row, col, dir = map(int, input().split())
mat = []
for _ in range(N):
    mat.append(list(map(int, input().split())))

# 방문 여부 행렬
visited = []
for _ in range(N):
    t = []
    for _ in range(M):
        t.append(False)
    visited.append(t)


# 현재 방향 따라 좌회전 좌표 구함
def turn_left():
    global dir
    if dir == 0:  # 북 -> 서
        dir = 3
    else:
        dir -= 1


# 현재 방향 따라 앞으로 이동, 다음 좌표 구함
# 이동 못하는 경우도 고려
def get_next_position(row, col, dir):
    dir_list = [0, 1, 2, 3]
    dr_list = [-1, 0, 1, 0]
    dc_list = [0, 1, 0, -1]

    # 방향에 따른 인덱스 변화 구함 (리스트탐색 이용)
    for i in range(len(dir_list)):
        if dir_list[i] == dir:
            dr = dr_list[i]
            dc = dc_list[i]

            # 인덱스 범위 안벗어남 , 방문 X , 바다(1) 아님
            # -> 전부 만족 시 이동 후 좌표 반환
            if 0 <= row + dr and row + dr <= N - 1 and \
                0 <= col + dc and col + dc <= M - 1 and \
                not visited[row + dr][col + dc] and \
                mat[row + dr][col + dc] != 1:
                return [row + dr, col + dc]

            # 이동할 수 없음 -> 좌표 그대로 반환
            else:
                return [row, col]


# 4회전 후 후방이동
def get_back_postition(row, col, dir):
    dir_list = [0, 1, 2, 3]
    dr_list = [1, 0, -1, 0]
    dc_list = [0, -1, 0, 1]

    # 방향에 따른 인덱스 변화 구함 (리스트탐색 이용)
    for i in range(len(dir_list)):
        if dir_list[i] == dir:
            dr = dr_list[i]
            dc = dc_list[i]

            # 인덱스 범위 안벗어남(바다X) , 방문은 상관 X , 바다(1) 아님
            # -> 전부 만족 시 이동 후 좌표 반환
            if 0 <= row + dr and row + dr <= N - 1 and \
                0 <= col + dc and col + dc <= M - 1 and \
                mat[row + dr][col + dc] != 1:
                return [row + dr, col + dc]

            # 이동할 수 없음 -> 좌표 그대로 반환
            else:
                return [row, col]


# 왼쪽 회전 후 -> 전진 or continue로 되돌아감
counter = 0  # 4회 회전하면 벗어나기 위함
visit_count = 0  # 방문한 곳 수
while True:

    # 4방향 모두 이동 X -> 방향 유지, 한칸 뒤로 간 후 카운터 초기화, continue
    if counter == 4:
        new_row, new_col = get_back_postition(row, col, dir)
        if row == new_row and col == new_col:
            break
        else:
            row, col = new_row, new_col
            counter = 0

    # 회전 -> 앞 위치 구하고 비교
    turn_left()
    new_row, new_col = get_next_position(row, col, dir)

    # 다음 위치와 현재 위치가 같음 -> 이동 X, 카운터만 증가 후 반복
    if row == new_row and col == new_col:
        counter += 1
        continue

    # 다음 위치와 현재 위치가 다름 -> 이동, 카운터 초기화, 방문처리
    else:
        row, col = new_row, new_col
        counter = 0
        visited[row][col] = True
        visit_count += 1

print(visit_count)
