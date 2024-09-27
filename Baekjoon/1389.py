import sys
n,m = map(int,input().split())
INF = sys.maxsize
dist = [[INF for _ in range(n+1)] for _ in range(n+1)]
ans = INF
for i in range(n+1):
    dist[i][i] =0

for _ in range(m):
    a,b = map(int,input().split())
    dist[a][b] =1
    dist[b][a] =1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dist[i][j]= min(dist[i][k]+dist[k][j],dist[i][j])
for i in range(1,n+1):
    result=sum(dist[i][1:])
    if ans > result:
        ans =result
        curr = i
print(curr)

# https://www.acmicpc.net/problem/1389 케빈 베이컨의 6단계 법칙 플로이드워셜
    