king, stone, n  = input().split()
n = int(n)
CMD = []
for _ in range(n):
    CMD.append(input())
change = {"A": 1, "B" : 2, "C" :3, "D": 4, "E":5, "F": 6, "G" : 7, "H":8}
changeIntegerToString = {v:k for k,v in change.items()}

king_dot = change[king[0]],int(king[1])
stone_dot = change[stone[0]],int(stone[1])

move = {"R" : (1,0) , "L" : (-1,0) , "B":(0,-1), "T":(0,1), "RT" : (1,1) , "LT":(-1,1) , "RB":(1,-1), "LB": (-1,-1)}
nsx,nsy = 0,0
x,y = king_dot
sx,sy = stone_dot
for cmd in CMD:
    nx = x + move[cmd][0]
    ny = y + move[cmd][1]
    if 1<=nx<=8 and 1<=ny<=8 :
        x,y =nx,ny
    else:
        continue

    if (x,y) == (sx,sy):
        nsx = sx+ move[cmd][0]
        nsy=  sy + move[cmd][1]
        if  1<=nsx<=8 and 1<=nsy<=8 :
            sx, sy =nsx,nsy
        else :
            x -=move[cmd][0]
            y -=move[cmd][1]
          
      


print(f"{changeIntegerToString[x]}{y}")
print(f"{changeIntegerToString[sx]}{sy}")


#https://www.acmicpc.net/problem/1063 킹