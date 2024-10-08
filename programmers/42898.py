def solution(m, n, puddles):
    road = [[0 for _ in range(m)] for _ in range(n)]
    road[0][0] =1
    for x,y in puddles:
        road[y-1][x-1] = "."
    
    for i in range(1,m):
        if road[0][i] != ".":
            road[0][i] =road[0][i-1]
        else:
            road[0][i] = 0
    for i in range(1,n):
        if road[i][0] != ".":
            road[i][0] = road[i-1][0]
        else:
            road[i][0] =0
    for i in range(1,n):
        for j in range(1,m):
            if road[i][j] !=".":
                road[i][j] = road[i-1][j]+road[i][j-1]
            else:
                road[i][j] =0
    return road[n-1][m-1] %1000000007
    

solution(4,	3,[[2, 2]]) #	4

#https://school.programmers.co.kr/learn/courses/30/lessons/42898 등굣길 level3