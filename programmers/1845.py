def solution(nums):
    select = len(nums)//2
    d= dict()
    
    for i in nums:
        if i not in d:
            d[i]= 1
        else:
            d[i]+=1
    arr = d.values()
    
    if len(arr) >= select:
        return select
    else:
        return len(arr)
#https://school.programmers.co.kr/learn/courses/30/lessons/1845 폰켓몬