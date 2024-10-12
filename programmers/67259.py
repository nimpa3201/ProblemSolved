# def solution(board):
#     global visited,min_val
#     n = len(board)
#     visited = [[0 for _ in range(n)] for _ in range(n)]
#     min_val =600*n*n

#     dfs(board, n, 0, 0, 0, 0, -1)
    
#     return min_val


# def dfs(grid, length, curr_x, curr_y, s, t, prev_dir):
#     global visited,min_val
    
    
#     if s * 100 + t * 500 >= min_val:
#         return
    
#     if curr_x == length - 1 and curr_y == length - 1:
#         min_val = min(min_val, s * 100 + t * 500)
#         return
    
#     dirs = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
    
#     visited[curr_x][curr_y] = 1
    
#     for i in range(4):
#         new_x = curr_x + dirs[i][0]
#         new_y = curr_y + dirs[i][1]
        
#         if can_go(grid, new_x, new_y, length, visited):
            
#             if prev_dir == -1 or i == prev_dir or i == (prev_dir+2)%4:
    
#                 dfs(grid, length, new_x, new_y, s+1, t, i)
#             else:
               
#                 dfs(grid, length, new_x, new_y, s+1 , t+1, i)
            
      
#     visited[curr_x][curr_y] = 0


# def can_go(grid, x, y, n, visited):
#     return 0 <= x < n and 0 <= y < n and visited[x][y] == 0 and grid[x][y] == 0  시간초과 ㅜ ㅜ

from collections import deque

def solution(board):
    n = len(board)

    dirs = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
    
    dp = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]
    

    for i in range(4):
        dp[0][0][i] = 0
    
    queue = deque([(0, 0, -1, 0)]) 
    
    while queue:
        x, y, prev_dir, cost = queue.popleft()
        
        if x == n-1 and y == n-1:
            continue
        
        for i in range(4):
            nx, ny = x + dirs[i][0], y + dirs[i][1]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                new_cost = cost + 100
                if prev_dir != -1 and i != prev_dir and i != (prev_dir + 2) % 4:
                    new_cost += 500
                
                if new_cost < dp[nx][ny][i]:
                    dp[nx][ny][i] = new_cost
                    queue.append((nx, ny, i, new_cost))
    
    return min(dp[n-1][n-1])







#print(solution([[0,0,0],[0,0,0],[0,0,0]]))	#900
#print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))	#3800
#print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])) #2100
#print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))	 #3200


#https://school.programmers.co.kr/learn/courses/30/lessons/67259 경주로 건설 level3