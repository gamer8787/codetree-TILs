import heapq

n,m,k = map(int,input().split())
gun = []
for _ in range(n):
    line = list(map(int,input().split()))
    line = [[-i] if i!=0 else [] for i in line]
    gun.append(line)

dy = [-1,0,1,0]
dx = [0,1,0,-1]
player = []
player_map = [["X" for _ in range(n)] for _ in range(n)]
score = [0 for _ in range(m)]

PRINT = False


for _ in range(m):
    y,x,d,s = map(int,input().split())
    y-=1
    x-=1
    player.append([y,x,d,s,0])

def check(i,j):
    if 0<=i < n and 0<=j<n:
        return True
    else:
        return False

def round():
    global player_map
    player_map = [["X" for _ in range(n)] for _ in range(n)]
    for i,(y,x,d,s,g) in enumerate(player):
        player_map[y][x] = i

    for i in range(m):
        y,x,d,s,g = player[i]
        ny = y +dy[d]
        nx = x +dx[d]
        if check(ny,nx):
            player[i] = [ny,nx,d,s,g]
        else:
            d = (d+2)%4
            ny = y + dy[d]
            nx = x + dx[d]
            player[i] = [ny,nx,d,s,g]
        player_map[y][x] = "X"
        if player_map[ny][nx]=="X":
            player_map[ny][nx] = i
            if gun[ny][nx]:
                new_gun = -gun[ny][nx][0]
                if new_gun > g:
                    player[i][4] = new_gun
                    heapq.heappop(gun[ny][nx])
                    if g>0:
                        heapq.heappush(gun[ny][nx],-g)

        else:
            o = player_map[ny][nx]
            _,_,od,os,og = player[o]
            osum = os+og
            msum = s+g

            if osum > msum:
                lose(i)
                win(o)
                score[o] += (osum - msum)
            elif osum < msum:
                lose(o)
                win(i)
                score[i] += (msum - osum)
            else:
                if os>s:
                    lose(i)
                    win(o)
                else:
                    lose(o)
                    win(i)

def lose(i):
    y,x,d,s,g = player[i]
    if g > 0:
        player[i][4] = 0
        heapq.heappush(gun[y][x],-g)
    while True:
        ny = y + dy[d]
        nx = x + dx[d]
        if check(ny, nx) and player_map[ny][nx] == "X":
            player_map[ny][nx] = i
            player_map[y][x] = "X"
            player[i][0] = ny
            player[i][1] = nx
            break
        else:
            d = (d + 1) % 4
            player[i][2] = d
    if gun[ny][nx]:
        new_gun = -heapq.heappop(gun[ny][nx])
        player[i][4] = new_gun

def win(i):
    y, x, d, s, g = player[i]
    player_map[y][x] = i
    if gun[y][x]:
        new_gun = -gun[y][x][0]
        if new_gun > g:
            player[i][4] = new_gun
            heapq.heappop(gun[y][x])
            if g>0:
                heapq.heappush(gun[y][x],-g)

def print_gun():
    if PRINT:
        for g in gun:
            print(*g)
        print()

def print_player():
    if PRINT:
        for p in player_map:
            print(*p)
        print()

def print_score():
    if PRINT:
        print(score)
        print()
print_gun()
print_player()
for i in range(k):
    if PRINT:
        print(i+1,"라운드")
    round()
    print_gun()
    print_player()
    print_score()


print(*score)