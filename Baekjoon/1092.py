n = int(input())  
weight = list(map(int, input().split()))  
m = int(input())  
box = list(map(int, input().split()))  
weight.sort(reverse=True)
box.sort(reverse=True)

if box[0] > weight[0]:
    print(-1)
    exit()

cnt = 0  
while box:
    cnt += 1  
    for w in weight:
        for i in range(len(box)):
            if w >= box[i]:
                box.pop(i)
                break  
print(cnt)

#https://www.acmicpc.net/problem/1092 배