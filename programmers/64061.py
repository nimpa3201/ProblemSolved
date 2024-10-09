def solution(board, moves):
    tmp =[]
    cnt=0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] !=0:
                tmp.append(board[j][i-1])
                cnt+=1 
                if len(tmp)>=2 and tmp[-1]==tmp[-2]:
                    tmp.pop()
                    tmp.pop()
                board[j][i-1]=0
                break

    return cnt-len(tmp)


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])) #4

#https://school.programmers.co.kr/learn/courses/30/lessons/64061 크레인 인형뽑기 게임 level1
