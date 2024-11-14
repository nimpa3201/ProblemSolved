all = []
cmd = []

for _ in range(4):
    q = list(map(int, input()))
    all.append(q)

k = int(input())
for _ in range(k):
    num, dir = map(int, input().split())
    cmd.append((num, dir))


def anticlockwise(arr):
    tmp = arr[0]
    for i in range(7):
        arr[i] = arr[i + 1]
    arr[7] = tmp
    return arr


def clockwise(arr):
    tmp = arr[7]
    for i in range(7, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = tmp
    return arr


for n,d in cmd:
    n -= 1
    wise = [0] * 4
    check = [0] * 3

    if all[0][2] != all[1][6]:
        check[0] = 1
    if all[1][2] != all[2][6]:
        check[1] = 1
    if all[2][2] != all[3][6]:
        check[2] = 1

    wise[n] =d

    for i in range(n, 0, -1):
        if check[i - 1] == 1:
            wise[i - 1] = -wise[i]
        else:
            break
    for i in range(n, 3):
        if check[i] == 1:
            wise[i + 1] = -wise[i]
        else:
            break
    
    for i in range(4):
        if wise[i] == 1:
            clockwise(all[i])
        elif wise[i] == -1:
            anticlockwise(all[i])

print(all[0][0] + 2 * all[1][0] + 4 * all[2][0] + 8 * all[3][0])
