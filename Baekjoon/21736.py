import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(input()) for _ in range(n)]
visited =[[ 0 for _ in range(m)] for _ in range(n)]

def dfs(x,y):
    global cnt
    dirs = {0 : (1,0) , 1 : (-1,0) , 2: (0,1), 3:(0,-1) }
    
    for i in range(4):
        nx = x + dirs[i][0]
        ny = y + dirs[i][1]
        
        if 0<=nx<n and 0<=ny <m and not visited[nx][ny] and graph[nx][ny] !="X" :
            if graph[nx][ny] =="O":
                visited[nx][ny] =1
                dfs(nx,ny)
            if graph[nx][ny] == "P":
                visited[nx][ny] =1
                cnt+=1
                dfs(nx,ny)
    return cnt
        

cnt =0
for i in range(n):
    for j in range(m):
        if graph[i][j] =="I":
            visited[i][j] =1
            dfs(i,j)

print(cnt if cnt !=0 else "TT")



# https://www.acmicpc.net/problem/21736 헌내기는 친구가 필요해