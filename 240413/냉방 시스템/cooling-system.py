from collections import deque

n,m,k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
#2 3 4 5 왼위우아

dy = [0,-1,0,1]
dx  =[-1,0,1,0]

walls = [[set() for _ in range(n)] for _ in range(n)]
air = [[0 for _ in range(n)] for _ in range(n)]

P = True

def print_air():
    if P:
        print("공기")
        for a in air:
            print(*a)
        print()

for _ in range(m):
    y,x,s = map(int,input().split())
    y-=1
    x-=1
    if s==0:
        walls[y][x].add(1)
        if 0<=y-1<n:
            walls[y-1][x].add(3)
    if s==1:
        walls[y][x].add(0)
        if 0 <= x - 1 < n:
            walls[y][x-1].add(2)

def add_air(y,x):
    global air
    temp_air = [[0 for _ in range(n)] for _ in range(n)]
    d = graph[y][x]-2
    d1 = (d+1)%4
    d2 = (d-1)%4
    sy = y + dy[d]
    sx = x + dx[d]

    q = deque()
    q.append((sy,sx,5))
    while q:
        ky,kx,dis = q.popleft()
        if dis ==0:
            continue
        temp_air[ky][kx] = dis

        if d not in  walls[ky][kx]:
            ny = ky + dy[d]
            nx = kx + dx[d]
            if 0<=ny<n and 0<=nx<n:
                q.append((ny,nx,dis-1))

        if d1 not in walls[ky][kx]:
            ny = ky + dy[d1]
            nx = kx + dx[d1]
            if 0<=ny<n and 0<=nx<n:
                if d not in walls[ny][nx]:
                    ny = ny + dy[d]
                    nx = nx + dx[d]
                    if 0 <= ny < n and 0 <= nx < n:
                        q.append((ny, nx, dis - 1))
        if d2 not in walls[ky][kx]:
            ny = ky + dy[d2]
            nx = kx + dx[d2]
            if 0<=ny<n and 0<=nx<n:
                if d not in walls[ny][nx]:
                    ny = ny + dy[d]
                    nx = nx + dx[d]
                    if 0 <= ny < n and 0 <= nx < n:
                        q.append((ny, nx, dis - 1))
    for r in range(n):
        for c in range(n):
            air[r][c] += temp_air[r][c]

def process1():
    for y in range(n):
        for x in range(n):
            if graph[y][x] in [2,3,4,5]:
                add_air(y,x)

def process2():
    global air
    temp_air = [[0 for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            for k in range(4):
                nr = r + dy[k]
                nc = c + dx[k]
                if 0<=nr<n and 0<=nc<n:
                    if air[r][c] > air[nr][nc]:
                        temp_air[r][c] -= (air[r][c] - air[nr][nc])//4
                    elif air[r][c] < air[nr][nc]:
                        temp_air[r][c] += (air[nr][nc] - air[r][c]) // 4
    for r in range(n):
        for c in range(n):
            air[r][c] += temp_air[r][c]

def process3():
    for r in range(n):
        for c in range(n):
            if r in [0,n-1] or c in [0,n-1]:
                if air[r][c] > 0:
                    air[r][c]-=1

def check():
    for r in range(n):
        for c in range(n):
            if graph[r][c] == 1:
                if air[r][c] < k :
                    return False
    return True

for t in range(1,101):
    process1()
    process2()
    process3()
    if check():
        print(t)
        exit(0)
print(-1)