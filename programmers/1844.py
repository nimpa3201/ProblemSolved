from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited =[ [0 for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((0,0,1))
    visited[0][0]=1
    dirs = {0 :(-1,0), 1:(1,0), 2:(0,1), 3:(0,-1) }
    
    while q:
        x,y,ans = q.popleft()
        
        if x ==n-1 and y == m-1:
            return ans
        
        
        for i in range(4):
            nx = x + dirs[i][0]
            ny = y + dirs[i][1]
            if 0<= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny]==1:
                q.append((nx,ny,ans+1))
                visited[nx][ny] =1
    return -1
    
    
    
   




print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))	#11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))	#-1