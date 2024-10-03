def solution(s):
    li =[]
    n = len(s)+1
    result =n
    for i in range(1,n//2+1):
        ans =''
        tmp = s[0:i]
        cnt =0
        for j in range(0,n,i):
            if tmp == s[j:j+i]:
                cnt+=1
                
            else:
                if cnt !=1:
                    ans += str(cnt)+tmp
                else:
                    ans += tmp
                tmp =s[j:j+i]
                cnt =1
        ans += str(cnt) +tmp if cnt>1 else tmp
        li.append(ans)
        result = min(result,len(ans))
    return result


print(solution("aabbaccc"))    #	7
print(solution("ababcdcdababcdcd"))	#9
print(solution("abcabcdede"))	#8
print(solution("abcabcabcabcdededededede"))	#14
print(solution("xababcdcdababcdcd"))  #	17

# https://school.programmers.co.kr/learn/courses/30/lessons/60057 문자열 압축 leverl2