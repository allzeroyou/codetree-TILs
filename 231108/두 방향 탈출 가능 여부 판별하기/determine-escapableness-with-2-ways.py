n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

visited = [[0 for _ in range(m)] for _ in range(n)]
# 오른쪽, 왼쪽 이동
dxs, dys = [0, 1], [1, 0]


# 주어진 위치가 범위 내인지
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def can_go(x, y):
    if not in_range(x, y) or visited[x][y] or board[x][y] == 0:  # 범위를 벗거나 방문 했거나 뱀 있는 곳이라면
        return False  # 이동 불가
    return True  # 그 밖에 이동 가능


def dfs(x, y):
    for dx, dy in zip(dxs, dys):
        nx, ny = dx + x, dy + y
        if can_go(nx, ny):
            visited[nx][ny] = True
            dfs(nx, ny)


visited[0][0] = 1
dfs(0, 0)

print(visited[n - 1][m - 1])  # 탐색 후 끝 점을 방문했는지 여부 출력