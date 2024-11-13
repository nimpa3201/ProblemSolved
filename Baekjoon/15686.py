n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
chicken =list()
home = list()
ans =list()
result = list()


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append((i+1,j+1))
            
        if graph[i][j] == 2:
            chicken.append((i+1,j+1))



def cal(m_chicken,home):
    ans =0
    for a,b in home:
        degree = 1e9
        for c,d in m_chicken:
            degree= min(degree,abs(a-c)+abs(b-d))
        ans +=degree
    return ans


def choose(num,start):
    if num == m :
        result.append(cal(ans,home))
        return
    for i in range(start,len(chicken)):
        ans.append(chicken[i])
        choose(num+1,i+1)
        ans.pop()

choose(0,0)    

print(min(result))


#https://www.acmicpc.net/problem/15686 치킨배달

            
            
