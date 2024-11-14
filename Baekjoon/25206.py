gradeMap = {"A+" :4.5 , "A0":4.0 , "B+":3.5, "B0":3.0, "C+" : 2.5 ,"C0":2.0 , "D+":1.5, "D0":1.0, "F":0}
ans =0
creditSum =0

for _ in range(20):
    info = input()
    subject,credit,grade = info.split(" ")
    credit = float(credit)
    if grade == "P":
        continue
    creditSum+=credit
    ans += credit * gradeMap[grade]
    
    
ans =ans/creditSum
print(ans)

    
#https://www.acmicpc.net/problem/25206 너의 평점은

    
