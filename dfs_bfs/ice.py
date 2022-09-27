#row, col = 4, 5
#mat = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]

# 그래프의 총 개수를 구하는 문제
# 특정 위치를 기준으로 탐색을 하면, 해당 위치와 연결된 부분이 전부 방문처리됨
# 다른 위치에서 탐색을 시도했을 때에, 같은 그래프에 속한다면 이미 방문처리가 되어있음
# 따라서 전체 위치에 대하여 각각 탐색을 시도하고, 해당 위치가 미방문이라면 다른 그래프임
# 다른 그래프일 때만 세면 됨

row, col = map(int, input().split(" "))
mat = []
for _ in range(row):
    mat.append(list(map(int, list(input()))))

# DFS -> "현재위치 방문 처리", "이웃"한 "미방문"노드를 인자로 재귀호출
visited = [[False] * col for _ in range(row)]
'''
    1. 탐색 시작 노드가 칸막이일 경우와, 이미 방문한 경우는 동치임. 
    (주변을 탐색할 필요가 없고, 방문처리할 필요가 없기 때문)
    조건문에서 칸막이 여부만 확인하면 방문 여부를 따로 처리해야 하므로 적절하지 않음
    2. 재귀함수 : 처음의 조건에서 다 걸러야함! 내부에서 따로 거르면 매우 복잡해지므로 절대 X
    -> 조건 발견되는 대로 다 첫 조건에 박아넣기
    3. 이미 방문처리가 되어있으면 False 반환, 미방문이면 True 반환
'''


def dfs(r, c):
    # 전체 탈출경우 "전부" 명시 !!
    # 칸막이이거나, 이미 방문한 노드이거나, 인덱스 벗어남
    if (r < 0 or c < 0 or r >= row
            or c >= col) or mat[r][c] == 1 or visited[r][c]:
        return False

    # 칸막이가 아니고, 미방문이며, 유효한 인덱스임
    else:
        visited[r][c] = True

        # 연결된 노드들 방문 (적정 수행 판별은 호출되면 내부 조건문에서 수행됨, 따로 X)
        # (연결 : 0인 부분끼리 상하좌우방향 인접)
        dfs(r - 1, c)  # 상
        dfs(r + 1, c)  # 하
        dfs(r, c - 1)  # 좌
        dfs(r, c + 1)  # 우
        return True


counter = 0
for i in range(row):
    for j in range(col):
        res = dfs(i, j)
        if res:
            counter += 1

print(counter)
