def solution(triangle):
    n = len(triangle)
    dp = [[0 for _  in range(i)]  for i in range(1,n+1)]
    dp[0][0] = triangle[0][0]
    
    initialize(triangle,dp,n)
    
    for i in range(2,n):
        for j in range(1,i):
            dp[i][j] = triangle[i][j]+ max(dp[i-1][j-1],dp[i-1][j])
    return max(dp[n-1])

    
    
def initialize(triangle,dp,n): #dp 초기화 함수
    dp[0][0] = triangle[0][0]
    for i in range(1,n):
        dp[i][0] =dp[i-1][0] + triangle[i][0]
        dp[i][-1] = dp[i-1][-1] +triangle[i][-1]

# https://school.programmers.co.kr/learn/courses/30/lessons/43105 정수삼각형 level3        