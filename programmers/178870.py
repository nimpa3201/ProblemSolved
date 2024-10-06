def solution(sequence, k):
    L =0
    R =0
    n = len(sequence)
    arr = []
    while L <=R < len(sequence):
        sum_val =0
        for i in range(L,R+1):
            sum_val +=sequence[i]
        
        if sum_val < k :
            R+=1
        if sum_val > k :
            L+=1
        if sum_val == k:
            arr.append((L,R))
            R+=1

    curr_L =0
    curr_R =0
    for L,R in arr:
       if n > R-L:
           n = R-L
           curr_R = R
           curr_L = L
    print([curr_L,curr_R])
    
            
            
            
            
              
            
    
    
solution([1, 2, 3, 4, 5] ,7) #[2, 3]


solution([1, 1, 1, 2, 3, 4, 5],5)	#[6, 6]

solution([2, 2, 2, 2, 2],6) #	[0, 2]