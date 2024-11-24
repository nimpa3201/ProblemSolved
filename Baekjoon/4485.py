import heapq

cnt = 0
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

while True:
    num = int(input())
    cnt += 1
    if num == 0:
        break
    
    graph = [list(map(int, input().split())) for _ in range(num)]
    min_cost = [[float('inf') for _ in range (num)] for _ in range(num)]
    min_cost[0][0] = graph[0][0]
    pq = []
    heapq.heappush(pq, (graph[0][0], 0, 0))

    while pq:
        rupee, x, y = heapq.heappop(pq)

        if x == num - 1 and y == num - 1:
            print(f"Problem {cnt}: {rupee}")
            break

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < num and 0 <= ny < num:
                new_cost = rupee + graph[nx][ny]
                if new_cost < min_cost[nx][ny]:
                    min_cost[nx][ny] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny))

# https://www.acmicpc.net/problem/4485 녹색 옷 입은 애가 젤다지? 