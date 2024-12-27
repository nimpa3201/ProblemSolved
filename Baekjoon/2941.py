word = input()
string = {"c=", "c-", "dz=","d-", "lj","nj","s=","z="}
ans =0
idx =0
while idx != len(word):
    if word[idx:idx+3] == "dz=":
        ans+=1
        idx += 3
    elif word[idx:idx+2] in string:
        ans+=1
        idx+=2
    else:
        idx+=1
        ans+=1
print(ans)
        
#https://www.acmicpc.net/problem/2941 크로아티아 알파벳
