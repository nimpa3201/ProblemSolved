def solution(A,B):
    ans =0
    A.sort(reverse = True)
    B.sort()
    for i in range(len(A)):
        ans +=A[i] * B[i]
    return ans

#https://school.programmers.co.kr/learn/courses/30/lessons/12941 최소값 만들기 level2
   