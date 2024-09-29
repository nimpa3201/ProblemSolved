import heapq
def solution(A, B):
    heapq.heapify(A) # 주어짐
    heapq.heapify(B)
    
    ans =0
    
    while A :
        
        elemA = heapq.heappop(A)
        
        while B and B[0] <=elemA:
            heapq.heappop(B)
            
        if B :
            heapq.heappop(B)
            ans +=1
    
    return ans

# https://school.programmers.co.kr/learn/courses/30/lessons/12987 숫자게임 level3







print(solution([5,1,3,7],[2,2,6,8]))#3
print(solution([2,2,2,2],[1,1,1,1]))	#0