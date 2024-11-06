import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
graph = [0 for _ in range(n)]

mk = 0

for i in range(n):
    graph[i] = list(map(int, input().split()))
    mk = max(mk, max(graph[i]))

k = 0
sa = 0

def dfs(x, y, tk):
    visited[x][y] = 1
    lst = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]
    for nx, ny in lst:
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and graph[nx][ny] > tk:
            dfs(nx, ny, tk)

for ki in range(1, mk):
    visited = [[0] * m for _ in range(n)]
    s = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and graph[i][j] > ki:
                dfs(i, j, ki)
                s += 1
    if sa < s:
        sa = s
        k = ki

print(k, sa)