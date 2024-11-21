n,score,p = map(int,input().split())
if n > 0:   
    scores = list(map(int,input().split()))
if n ==0:
    scores = []

# 랭킹 리스트에 올라갈 수 없을 정도로 낮다면 -1을 출력
if len(scores) == p and scores[n-1] >= score:
    print(-1)

else:
    scores.append(score)
    scores.sort(reverse=True)
    for i in range(n+1):
        if scores[i] == score:
            print(i+1)
            break
