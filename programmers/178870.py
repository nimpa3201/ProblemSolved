def solution(sequence, k):
    L = 0
    R = 0
    n = len(sequence)
    curr_sum = 0
    arr = []

    while R < n:
        curr_sum += sequence[R]

        while curr_sum > k and L <= R:
            curr_sum -= sequence[L]
            L += 1

        if curr_sum == k:
            arr.append((L, R))

        R += 1

    min_len = n + 1
    curr_L = 0
    curr_R = 0
    for L, R in arr:
        if R - L < min_len:
            min_len = R - L
            curr_L = L
            curr_R = R

    return [curr_L, curr_R]


            
            
solution([1, 2, 3, 4, 5] ,7) #[2, 3]
solution([1, 1, 1, 2, 3, 4, 5],5)	#[6, 6]
solution([2, 2, 2, 2, 2],6) #	[0, 2]

#https://school.programmers.co.kr/learn/courses/30/lessons/178870 연속된 부분 수열의 합 level2