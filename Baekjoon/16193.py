import heapq
n = int(input())
nums = list(map(int,input().split()))
nums.sort()
small_pq =[]
big_pq =[]
new_arr = [0 for _ in range(n+1)]
if n %2 ==0:
    smll_num = nums[:n//2]
    big_num = nums[n//2:]

    for i in smll_num:
        heapq.heappush(small_pq,-i)
    for i in big_num:
        heapq.heappush(big_pq,i)

    for i in range(1,len(big_num)+1):
        if i %2 ==0:
            samll = heapq.heappop(small_pq)
            big  = heapq.heappop(big_num)
            new_arr[i] =-samll
            new_arr[-i] = big
        else:
            samll = heapq.heappop(small_pq)
            big  = heapq.heappop(big_num)
            new_arr[i] = big
            new_arr[-i] =- samll
    ans =0
    for i in range(1,len(new_arr)-1):
        ans += abs(new_arr[i]-new_arr[i+1])
    print(ans)
        
else:
    small_num = nums[:n//2]
    big_num = nums[n//2:]
    tmp = big_num[0]
    big_num = big_num[1:]
   
    
    for i in small_num:
        heapq.heappush(small_pq,-i)
    for i in big_num:
        heapq.heappush(big_pq,i)

    for i in range(2,len(big_num)+2):
        if i %2 ==0:
            samll = heapq.heappop(small_pq)
            big  = heapq.heappop(big_num)
            new_arr[i-1] =-samll
            new_arr[-i] = big
        else:
            samll = heapq.heappop(small_pq)
            big  = heapq.heappop(big_num)
            new_arr[i-1] = big
            new_arr[-i] =- samll
    ans =0
    
    if abs(new_arr[1] - tmp ) < abs(new_arr[n-1]-tmp):
        new_arr[n] = tmp
        for i in range(1,len(new_arr)-1):
            ans += abs(new_arr[i]-new_arr[i+1])
        print(ans)
    else:
        new_arr[0] = tmp
        for i in range(0,len(new_arr)-2):
            ans += abs(new_arr[i]-new_arr[i+1])
        print(ans)
# https://www.acmicpc.net/problem/16193 차이를 최대로2
    
        