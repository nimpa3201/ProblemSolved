n = int(input())
for _ in range(n):
    d= dict()
    war = list(map(int,input().split()))
    army = war[0]
    winner =[]
    for w in war[1:]:
        if w in d :
            d[w] +=1
        else:
            d[w] =1
    
    for i in d :
        if d[i] > army/2:
            winner.append(i)
    
    if len(winner) ==0:
        print("SYJKGW")
    else:
        print(*winner)      

#https://www.acmicpc.net/problem/1270 전쟁 - 땅따먹기      