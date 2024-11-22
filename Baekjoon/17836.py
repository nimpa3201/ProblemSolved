from collections import deque
n,m,t = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            pos_x, pos_y = i,j


def bfstoGram():
    q = deque()
    q.append((0,0,0))
    visited[0][0]=1
    dirs = { 0 : (1,0) , 1 : (-1,0) , 2: (0,-1), 3:(0,1)}
    
    while q : 
        x,y ,step= q.popleft()
        
        if x == pos_x and y == pos_y:
            return step + +abs(n-1-pos_x)+abs(m-1-pos_y)
        
        
        for i in range(4):
            nx = x + dirs[i][0]
            ny = y + dirs[i][1]
            
            if 0<=nx < n and 0<= ny < m and not visited[nx][ny] and graph[nx][ny] !=1:
                q.append((nx,ny,step+1))
                visited[nx][ny] =1
    return False



def bfstoNotGram():
    visited = [[0 for _ in range(m)] for _ in range(n)]
    q= deque()
    q.append((0,0,0))
    visited[0][0] =1
    dirs = { 0 : (1,0) , 1 : (-1,0) , 2: (0,-1), 3:(0,1)}
    
    while q:
       x,y,step = q.popleft()
       
       if x == n-1 and y == m-1 :
           return step
       
       for i in range(4):
           nx = x + dirs[i][0]
           ny = y + dirs[i][1]
           
           if 0<=nx<n and 0<= ny < m and not visited[nx][ny] and graph[nx][ny]==0:
               q.append((nx,ny,step+1))
               visited[nx][ny] =1
    return False


mid= bfstoGram()
end =bfstoNotGram()

if mid ==False and end == False:
    print("Fail")
elif mid ==False and end != False:
    print(end if end <=t else "Fail")
elif mid !=False and end == False:
    print(mid if mid <=t else "Fail" )
else:
    ans = min(end,mid)
    print(ans if ans <= t else "Fail")

#https://www.acmicpc.net/problem/17836 공주님을 구해라!