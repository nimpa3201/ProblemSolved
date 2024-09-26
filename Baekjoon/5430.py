T = int(input())

for _ in range(T):
    cmd = list(input())
    n = int(input()) #배열 요소 개수
    

     
    arr = input()
    arr = arr[1:-1]
    
    if "D" in cmd and n ==0:
        print("error")
        continue
    
    if "R" in cmd and n ==0:
        print("[]")
        continue
    

  
    strArr = arr.split(",")
    
    intArr =[]
    for i in strArr:
        intArr.append(int(i))
        
    flag = False
    for m in cmd :
        
        if m == "R":
            flag = not flag
        
        else:
            if not intArr:
                    print("error")
                    break 
            if flag: # Reverse 일때 
                intArr.pop()
              
            else: #not Reverse 일때  
                intArr.pop(0)
                
              

    else:
        if flag:
            intArr.reverse()
            print("[" + ",".join(map(str, intArr)) + "]")
        else:
            print("[" + ",".join(map(str, intArr)) + "]")
        