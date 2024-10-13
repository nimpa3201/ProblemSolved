n,m = map(int,input().split()) #가로 세로
graph = [ list(input()) for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(m)]



def can_go_white(x,y):
    return 0<= x <m and 0 <= y < n and not visited[x][y] and graph[x][y] =="W"


def can_go_blue(x,y):
    return 0<= x <m and 0 <= y < n and not visited[x][y] and graph[x][y] =="B"
    


def dfs_white(x,y):
    global cnt
    dirs = { 0 : (0,-1), 1:(0,1) ,2:(-1,0), 3:(1,0)}
    
    for i in range(4):
        nx = x + dirs[i][0]
        ny = y + dirs[i][1]
        
        if can_go_white(nx,ny):
            visited[nx][ny] =1
            cnt+=1
            dfs_white(nx,ny)

      
def dfs_blue(x,y):
    global bluecnt
    dirs = { 0 : (0,-1), 1:(0,1) ,2:(-1,0), 3:(1,0)}
    
    for i in range(4):
        nx = x + dirs[i][0]
        ny = y + dirs[i][1]
        
        if can_go_blue(nx,ny):
            visited[nx][ny] =1
            bluecnt+=1
            dfs_blue(nx,ny)




whiteArr =[]
blueArr=[]
for i in range(m):
    for j in range(n): 
        if can_go_white(i,j):
            visited[i][j] =1
            cnt = 1
            dfs_white(i,j)
            whiteArr.append(cnt)

        
        if can_go_blue(i,j):
            visited[i][j] =1
            bluecnt =  1
            dfs_blue(i,j)
            blueArr.append(bluecnt)
ans_w =0
for w in whiteArr:
    ans_w+=w**2

ans_b=0
for b in blueArr:
    ans_b+=b**2    
print(ans_w,ans_b)
            
        