from collections import deque
q =deque()
tmp =0
l =[]
li=[]
def push(x,y):
    global q,tmp,li
    visited[x][y] =1
    q.append((x,y))
    tmp +=int(bli[x][y]) 

def solution(maps):
    cnt=0
    global visited,bli,tmp
    bli=[]
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    for i in maps:
        li=[]
        for j in i:
            li.append(j)
        bli.append(li)
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if can_go(i,j,maps) and bli[i][j]!='X':
                push(i,j)
                bfs()
                tmp+=int(bli[i][j])
                l.append(tmp)
                l.sort()
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if bli[i][j] == 'X':
                cnt+=1
    if cnt == len(maps)*len(maps[0]):
        return [-1]
    else:
        return l
       
            
    
def bfs():
    global q,bli,tmp
    tmp =0
    while q:
        x,y =q.popleft()
        dxs =[0,0,1,-1]
        dys= [1,-1,0,0]
        for dx,dy in zip(dxs,dys):
            nx = x+dx
            ny =y+dy
            if can_go(nx,ny,bli) and bli[nx][ny] !='X':
                push(nx,ny)
    
                

           
def can_go(x,y,maps):
    global visited
    if 0<=x<len(maps) and 0<=y<len(maps[0]) and not visited[x][y]:
        return True
    else:
        return False
    


        
solution(["X591X","X1X5X","X231X", "1XXX1"]) #	[1, 1, 27]
solution(["XXX","XXX","XXX"]) #	[-1)


#https://school.programmers.co.kr/learn/courses/30/lessons/154540 무인도 여행 level2