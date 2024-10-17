import sys
import heapq
def solution(N, road, K):
    graph = [[] for _ in range(1+N)]
    INF = sys.maxsize
    dist = [INF for _ in range(N+1)]
    dist[1] =0
    pq = []
    for a,b,w in road:
        graph[a].append((w,b))
        graph[b].append((w,a))
    heapq.heappush(pq,(0,1))
    while pq :
        min_dist,min_index = heapq.heappop(pq)
        
        if dist[min_index] != min_dist:
            continue
        
        for target_dist,target_index in graph[min_index]:
            new_dist = target_dist + min_dist
            if dist[target_index] > new_dist:
                dist[target_index] = new_dist
                heapq.heappush(pq,(new_dist,target_index))
    ans =0
    for i in dist[1:]:
        if i <= K:
            ans+=1
    return ans
            

print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3)) #4
print(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4)) #4
 
 
# https://school.programmers.co.kr/learn/courses/30/lessons/12978 배달