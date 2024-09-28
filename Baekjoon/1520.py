import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

m,n = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(m)]
visited = [[-1 for _ in range(n)]for _ in range(m)]
visited[m-1][n-1] =1

def dfs(x,y):
    
    if visited[x][y] != -1:
        return visited[x][y]
    ans =0
    dirs = {0 : (1,0) , 2: (-1,0) , 3:(0,1), 4:(0,-1) }
    for i in dirs:
        nx = x + dirs[i][0]
        ny = y + dirs[i][1]
        if 0<= nx < m and 0 <= ny < n and maps[x][y] > maps[nx][ny]:
            ans +=dfs(nx,ny)
            
    visited[x][y] = ans
    return visited[x][y]

print(dfs(0,0))


#https://www.acmicpc.net/problem/1520 내리막길
    
