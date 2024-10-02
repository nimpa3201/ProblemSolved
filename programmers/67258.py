def solution(gems):
    s = set(gems)
    R = -1
    n = len(gems)
    d = {}
    ans = n + 1
    start, end = 0, 0

    for L in range(n):
        while R + 1 < n and len(d) < len(s):
            R += 1
            if gems[R] in d:
                d[gems[R]] += 1
            else:
                d[gems[R]] = 1

        if len(d) == len(s):
            if R - L + 1 < ans:
                ans = R - L + 1
                start, end = L, R

        if gems[L] in d:
            d[gems[L]] -= 1
            if d[gems[L]] == 0:
                del d[gems[L]]

    return [start + 1, end + 1]

solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])	#[3, 7]
solution(["AA", "AB", "AC", "AA", "AC"])  #[1, 3]
solution(["XYZ", "XYZ", "XYZ"]) #[1, 1]
#https://school.programmers.co.kr/learn/courses/30/lessons/67258 보석쇼핑 level3