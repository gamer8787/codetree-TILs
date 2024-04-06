N,M,K = map(int,input().split())
miro = [list(map(int,input().split())) for _ in range(N)]
next_miro = [[0 for _ in range(N)] for _ in range(N)]
people = []
for _ in range(M):
    y,x = map(int,input().split())
    people.append([y-1,x-1])
ey,ex = map(int,input().split())
ey,ex = ey-1,ex-1

dy = [1,-1,0,0]
dx = [0,0,1,-1]

ans = 0

sl,sr,sc = 0,0,0

PRINT = False

def print_people_exit():
    if PRINT:
        graph = [[0 for _ in range(N)] for _ in range(N)]
        for y,x in people:
            graph[y][x] +=1
        graph[ey][ex] +=1000
        print("사람 위치")
        for g in graph:
            print(*g)
        print()

def print_miro():
    if PRINT:
        print("미로 벽")
        for m in miro:
            print(*m)
        print()
def move():
    global ans
    for i,(y,x) in enumerate(people):
        avail = []
        distance = abs(ey-y) + abs(ex-x)
        direction = 0
        avail.append([distance,direction,y,x])
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0<=ny<N and 0<=nx<N and miro[ny][nx]==0:
                distance = abs(ey-ny) + abs(ex-nx)
                direction = k
                avail.append([distance,direction,ny,nx])
        avail.sort()
        _,_,y2,x2 = avail[0]
        ans += abs(y2-y)
        ans += abs(x2-x)
        people[i] = [y2,x2]

def find_square():
    global sl,sr,sc
    for l in range(2,N+1):
        for r in range(N+1-l):
            for c in range(N+1-l):
                if not (r<= ey <r+l and c<=ex<c+l):
                    continue
                find_rectangle = False
                for y,x in people:
                    if r<= y <r+l and c<=x<c+l:
                        if y==ey and x==ex:
                            continue
                        sl = l
                        sr = r
                        sc = c
                        return

def rotate_miro():
    for r in range(sr,sr+sl):
        for c in range(sc,sc+sl):
            if miro[r][c] > 0:
                miro[r][c] -=1

    for r in range(sr,sr+sl):
        for c in range(sc,sc+sl):
            oy, ox = r-sr,c-sc
            ry,rx = ox, sl -1 - oy
            ny,nx = ry+sr,rx+sc
            next_miro[ny][nx] = miro[r][c]

    for r in range(sr,sr+sl):
        for c in range(sc,sc+sl):
            miro[r][c] = next_miro[r][c]

def rotate_exit_people():
    global ey,ex
    for i, (y,x) in enumerate(people):
        if sr<=y<sr+sl and sc<=x<sc+sl:
            oy, ox = y - sr, x - sc
            ry, rx = ox, sl - 1 - oy
            ny, nx = ry + sr, rx + sc
            people[i] = [ny,nx]
    oy, ox = ey - sr, ex - sc
    ry, rx = ox, sl - 1 - oy
    ny, nx = ry + sr, rx + sc
    ey,ex = ny,nx

for k in range(K):
    if PRINT:
        print(k+1, "단계")
    move()

    is_all_escaped = True
    for y,x in people:
        if not (y==ey and x==ex):
            is_all_escaped = False

    if is_all_escaped:
        break
    find_square()
    rotate_miro()
    rotate_exit_people()
    print_miro()
    print_people_exit()
print(ans)
print(ey+1,ex+1)