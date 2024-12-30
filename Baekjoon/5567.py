from collections import deque
n = int(input())
m = int(input())
visited = [ 0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    ans =0
    q= deque()
    q.append(1)
    visited[1] =1 
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if not visited[nx] :
                visited[nx] = visited[x]+1
                q.append(nx)
                if 2<=visited[nx]<=3:
                    ans+=1
                else:
                    break
    return ans            
print(bfs())

# https://www.acmicpc.net/problem/5567 결혼식
           
    
    
