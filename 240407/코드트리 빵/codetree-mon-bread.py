from collections import deque

n,m = map(int,input().split())
basecamp = [list(map(int,input().split())) for _ in range(n)]
store = [[0,0]]
for _ in range(m):
    y,x = map(int,input().split())
    store.append([y-1,x-1])

people = [[-1,-1] for _ in range(m+1)]

dy = [-1,0,0,1]
dx = [0,-1,1,0]

distance = [[-1 for _ in range(n)] for _ in range(n)]

def bfs(y,x):
    for i in range(n):
        for j in range(n):
            distance[i][j] = -1
    distance[y][x] = 0
    q = deque()
    q.append((y,x))
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<n and basecamp[ny][nx]!=2 and distance[ny][nx]==-1:
                distance[ny][nx] = distance[y][x] +1
                q.append((ny,nx))

def simulate(t): #t시간에 행해지는 시뮬
    for i in range(1,min(m+1,t)): #1,2번 과정을 수행
        if store[i] == people[i]:
            continue
        sy,sx = store[i]
        bfs(sy,sx)
        y,x = people[i]
        avail = []
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0<=ny<n and 0<=nx<n and distance[ny][nx]!=-1:
                dis = distance[ny][nx]
                avail.append([dis,k,ny,nx])
        avail.sort()
        _,_,ny,nx = avail[0]
        people[i] = [ny,nx]

    if t<=m:
        min_dis = 10**9
        min_y,min_x = -1,-1
        sy,sx = store[t]

        bfs(sy,sx)

        for i in range(n):
            for j in range(n):
                if distance[i][j] >= 0 and basecamp[i][j] == 1:
                    if distance[i][j] < min_dis:
                        min_dis = distance[i][j]
                        min_y,min_x = i,j
        people[t] = [min_y,min_x]
        basecamp[min_y][min_x] = 2
    for i in range(1,m+1):
        if people[i] == store[i]:
            sy,sx = store[i]
            basecamp[sy][sx] = 2
t = 1
while True:
    all_complete = True
    simulate(t)
    for i in range(1,m+1):
        if people[i] != store[i]:
            all_complete= False
    if all_complete:
        break
    t+=1
print(t)