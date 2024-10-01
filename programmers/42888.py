def solution(record):
    ans = []
    members = dict()
    records =[]
    for member in record :
        records.append(member.split(" "))
    for r in records:
    
        if r[0] == "Enter" or r[0] == "Change":
            if r[1] not in members:
                members[r[1]] = r[2]
            else:
               members[r[1]] = r[2]
    for r in records:
        if r[0] == "Enter":
            ans.append(members[r[1]]+ "님이 들어왔습니다.")
        elif r[0] =="Leave":
            ans.append(members[r[1]] +"님이 나갔습니다.")
    return ans 


    
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))	#["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

# https://school.programmers.co.kr/learn/courses/30/lessons/42888 오픈채팅방 level2
