from collections import deque
# 시작 좌표 넣고, 상하좌우 미방문 노드 방문
row, col = 5, 6
matrix = [[1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1],
          [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]

visited = [[False] * col for _ in range(row)]  # 방문 여부 저장

diff_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]
'''
    1. 여러 갈래의 길을, 번갈아가면서 한 단계씩 들어감 -> 먼저 도달하는 쪽이 최단경로
    2. BFS를 통하여 이러한 탐색이 가능함
    3. 거리계산 : 현재 노드의 값을 이웃 노드의 값에다 누적시키면 됨

'''


def bfs(r, c):
    # 시작 좌표를 큐에 넣음
    start_point = (r, c)
    queue = deque([start_point])

    while len(queue) > 0:
        # 큐에서 하나 pop하고, 그것과 이웃한 미방문 노드들을 탐색
        point = queue.popleft()
        print(point)
        visited[point[0]][point[1]] = True

        # 도착점일 경우 누적된 거리 반환
        if point[0] == row - 1 and point[1] == col - 1:
            return matrix[point[0]][point[1]]

        #  (최소경로이므로 방문한곳 다시 안감)
        for diff in diff_list:
            dr, dc = point[0] + diff[0], point[1] + diff[1]

            # 상하좌우 인덱스 검사 & 갈 수 있는 길인지 검사 & 방문했는지 확인
            if dr < 0 or dr >= row or dc < 0 or dc >= col or matrix[dr][
                    dc] == 0 or visited[dr][dc]:
                continue

            # 인덱스가 유효하고, 갈 수 있는 길이면 큐에 추가
            else:
                queue.append((dr, dc))
                matrix[dr][dc] = matrix[point[0]][point[1]] + 1


print(bfs(0, 0))
