n,m = map(int,input().split())
rectangle = [list(map(int,input())) for _ in range(n)]
maxLength = max(n,m)


for length in range(maxLength):
    for i in range(n-length):
        for j in range(m-length):
            if rectangle[i][j] == rectangle[i][j+length] == rectangle[i+length][j] == rectangle[i+length][j+length]:
                ans =(length+1)*(length+1)
print(ans)

#https://www.acmicpc.net/problem/1051 숫자 정사각형
                
    
    
