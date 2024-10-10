from collections import deque
n = int(input())
stones = [0]+list(map(int,input().split()))
start = int(input())
q = deque()
visited = [0 for _ in range(n+1)]

q.append(start)
visited[start] =1

while q:
    x =  q.popleft()
    if 1<=x - stones[x] < n+1 :
       q.append(x-stones[x])
       visited[x-stones[x]] =1
    
    if 1<= x+stones[x] < n+1 :
        q.append(x+stones[x])  
        visited[x+stones[x]]=1
cnt=0     
for i in visited :
    if i !=0:
        cnt+=1
print(cnt)

#https://www.acmicpc.net/problem/14248 점프 점프