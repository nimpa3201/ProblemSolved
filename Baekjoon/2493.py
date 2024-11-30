n = int(input())
arr = list(map(int, input().split()))
stack = []
ans = []

for i in range(n):
    while stack and stack[-1][0] <= arr[i]:
        stack.pop()
    if not stack:
        ans.append(0)
    else:
        ans.append(stack[-1][1] + 1)
    stack.append((arr[i], i))

print(*ans)

#https://www.acmicpc.net/problem/2493 탑