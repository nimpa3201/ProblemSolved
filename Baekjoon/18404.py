from collections import deque

n, m = map(int, input().split())
x, y = map(int, input().split())
arr = []
for _ in range(m):
    a, b = map(int, input().split())
    arr.append((a - 1, b - 1))

dirs = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

def bfs(x, y):
    q = deque()
    q.append((x, y, 0))
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 0
    while q:
        x, y, time = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                visited[nx][ny] = time + 1
                q.append((nx, ny, time + 1))
    return visited

distance = bfs(x - 1, y - 1)

ans = []
for a,b in arr:
    ans.append(distance[a][b])

print(*ans)

# https://www.acmicpc.net/problem/18404 현명한 나이트