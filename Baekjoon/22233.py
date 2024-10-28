import sys
input= sys.stdin.readline
n,m = map(int,input().split())
keyword =set()

for _ in range(n):
    word = input().strip()
    keyword.add(word)


for _ in range(m):
    memo = list(input().strip().split(","))
    
    for word in memo:
        if word in keyword:
            keyword.remove(word)
    
    print(len(keyword))
    
#https://www.acmicpc.net/problem/22233 가희와 키워드
    
    