n = int(input())
arr = list(map(int, input().split()))

ans1 = 0
R = 0

for L in range(n):
    while R + 1 < n and arr[R] <= arr[R + 1]:
        R += 1
    ans1 = max(ans1, R - L + 1)
    if R == L:
        R += 1



ans2 = 0
R = 0
for L in range(n):
    while R + 1 < n and arr[R] >= arr[R + 1]:
        R += 1
    ans2 = max(ans2, R - L + 1)
    if R == L:
        R += 1


print(max(ans1,ans2))


# https://www.acmicpc.net/problem/2491 수열
        
        
        
            