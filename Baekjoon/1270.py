n = int(input())
for _ in range(n):
    d= dict()
    war = list(map(int,input().split()))
    army = war[0]
    for w in war[1:]:
        if w in d :
            d[w] +=1
        else:
            d[w] =1
    flag = False
    for i in d :
        if d[i] > army//2:
            print(i)
            flag= True
    if not flag:
        print("SYJKGW")
       

#https://www.acmicpc.net/problem/1270 전쟁 - 땅따먹기      