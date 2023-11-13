board = [list(map(int, input().split())) for _ in range(4)]

for row in board:
    ans = 0
    for col in row:
        ans += col
    print(ans)