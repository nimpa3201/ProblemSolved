from collections import deque

def solution(priorities, location):
    processes = deque()
    for idx, process in enumerate(priorities):
        processes.append((process,idx))
    cnt =0
    while processes:
        elem = processes.popleft()
        if processes:
            max_value = max(processes)
        if elem[0] < max_value[0] :
            processes.append(elem)
        else:
            cnt+=1
            if elem[1] == location:
                return cnt    

print(solution([2, 1, 3, 2]	,2)) #1
print(solution([1, 1, 9, 1, 1, 1],0)) #5


#https://school.programmers.co.kr/learn/courses/30/lessons/42587 프로세스 level2