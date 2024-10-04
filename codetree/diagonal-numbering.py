n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]

num = 1
for k in range(n + m - 1):
    for i in range(n):
        j = k - i                 #i+j = k 
        if 0 <= j < m:
            arr[i][j] = num
            num += 1

for row in arr:
    print(*row)
