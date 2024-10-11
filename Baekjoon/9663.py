n = int(input())
row = [0 for _ in range(n)]
ans =0
def check(x):
    for i in range(x):
        if row[x]  == row[i] or abs(row[x]-row[i]) == abs(x-i):
            return False
    return True        

def dfs(start):
    global ans
    
    
    if start == n : 
        ans+=1
        return
    
    else:
        for i in range(n):
            row[start] = i
            
            if check(start) :
                dfs(start+1)
                                
dfs(0)                
print(ans)

#https://www.acmicpc.net/problem/9663  N-Queen
        