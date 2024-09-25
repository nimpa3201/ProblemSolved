def solution(s):
    stack = list()
    flag = False
    left =0
    if len(s) ==1:
        return False
    for i in range(len(s)):
        if s[i] =="(":
            stack.append("(")
            flag = True
            left +=1
        if stack and s[i] == ")":
            stack.pop()
        if s[i] == ")":
            left-=1
    if stack or not flag or left !=0: 
        return False
    else:
        return True
    
    

print(solution("(((())))")) #True
print(solution("(((((")) # false
print(solution(")))))))")) #false
print(solution("("))  #false
print(solution("()()")) #true
print(solution("(())()")) #true
print(solution(")()("))	#false
print(solution("(()(")) #false
print(solution("(()))")) #false

#https://school.programmers.co.kr/learn/courses/30/lessons/12909 올바른괄호 level2