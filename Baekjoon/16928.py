from collections import deque
n,m = map(int,input().split())
ladder = dict()
snake = dict()
visited = [0 for _ in range(101)]
q = deque()
for _ in range(n):
    x,y = map(int,input().split())
    ladder[x] = y
    
for _ in range(m):
    u,v = map(int,input().split())
    snake[u] = v
    
q.append((1,0))
visited[1] =1

def bfs():

    while q:
       num,step = q.popleft()
      
       
       if num == 100:
           return step
       
       
       for i in range(1,7):
            new_num = num + i
            
            if new_num > 100:
                continue 
           
            if new_num in ladder :
                q.append((ladder[new_num],step+1))
                visited[new_num] =1
                visited[ladder[new_num]] =1
            elif new_num in snake :
                q.append((snake[new_num],step+1))
                visited[new_num] =1
                visited[snake[new_num]]=1
            elif 1 <=new_num <=100 and not visited[new_num]:
                q.append((new_num,step+1)) 
                visited[new_num] =1
       
print(bfs())          
           
       
# https://www.acmicpc.net/problem/16928 뱀과 사다리 게임
    