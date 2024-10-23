N, r, c = map(int, input().split())

def fun(x, y, size, num):
    if (x <= r < x + size) and (y <= c < y + size):
        if size == 1:
            print(num)
            return True
        half = size // 2
        
        if fun(x, y, half, num):
            return True
        if fun(x, y + half, half, num + half * half):
            return True
        if fun(x + half, y, half, num + 2 * half * half):
            return True
        if fun(x + half, y + half, half, num + 3 * half * half):
            return True

    return False

fun(0, 0, 2**N, 0)

# https://www.acmicpc.net/problem/1074 Z