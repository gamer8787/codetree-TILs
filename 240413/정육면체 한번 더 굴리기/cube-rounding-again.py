from collections import deque

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

row = deque([1,3,6,5])
col = deque([1,2,6,5])

dy = [0,1,0,-1]
dx = [1,0,-1,0]

y,x,d = 0,0,0
score = 0
def move():
    global y,x,d,row,col
    if t ==0:
        d = 0
        y = y+ dy[d]
        x = x +dx[d]

        row.rotate(1)
        col[0] = row[0]
        col[2] = row[2]
    else:
        bottom = row[2]
        if bottom > graph[y][x]:
            d = (d+1)%4
        elif bottom < graph[y][x]:
            d = (d-1)%4
        else:
            pass
        ny = y +dy[d]
        nx = x +dx[d]
        if not (0<=ny<n and 0<=nx<n) :
            d = (d+2)%4
        y = y +dy[d]
        x = x +dx[d]

        if d ==0:
            row.rotate(1)
            col[0] = row[0]
            col[2] = row[2]
        elif d==2:
            row.rotate(-1)
            col[0] = row[0]
            col[2] = row[2]
        elif d==1:
            col.rotate(1)
            row[0] = col[0]
            row[2] = col[2]
        else:
            col.rotate(-1)
            row[0] = col[0]
            row[2] = col[2]
def scoring():
    global score
    count = 0
    s = graph[y][x]
    q = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[y][x] = True
    q.append((y,x))
    while q:
        r,c = q.popleft()
        count+=1
        for k in range(4):
            nr = r +dy[k]
            nc = c +dx[k]
            if 0<=nr<n and 0<=nc<n and graph[nr][nc] == s and visited[nr][nc]==False:
                visited[nr][nc] = True
                q.append((nr,nc))
    score += (s*count)

for t in range(m):
    move()
    scoring()
print(score)