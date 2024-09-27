import heapq
import sys

def dijkstra(s,e):
    global graph,node
    INF = sys.maxsize
    dist = [INF for _ in range(node+1)]
    dist[s] =0
    pq = []
    heapq.heappush(pq,(0,s))
    while pq :
        min_dist,min_index = heapq.heappop(pq)
        if min_dist != dist[min_index]:
            continue
        for target_index,target_dist in graph[min_index]:
            new_dist = dist[min_index] + target_dist
            if new_dist < dist[target_index]:
                dist[target_index] = new_dist
                heapq.heappush(pq,(new_dist,target_index))
    return dist[e]



def solution(n, s, a, b, fares):
    global node,graph
    node =n
    ans = sys.maxsize
    graph= [[] for _ in range(n+1)]
    for v1,v2,w in fares:
        graph[v1].append((v2,w))
        graph[v2].append((v1,w))
  
    for i in range (1,n+1):
      ans =min(ans,dijkstra(s,i)+dijkstra(i,a)+dijkstra(i,b))

    return ans



print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]) ) #18


#https://school.programmers.co.kr/learn/courses/30/lessons/72413 합승택시요금 level3