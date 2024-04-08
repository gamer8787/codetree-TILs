from collections import deque

n,m,k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dy = [-1,0,1,0]
dx = [0,1,0,-1]

ans = 0

P = False

def print_graph():
    if P:
        for g in graph:
            print(*g)
        print()


def move(): #1=>4, 2=>2 or 1 3=>2
    global graph
    copy_graph = [i[:] for i in graph]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                for k in range(4):
                    ni = i + dy[k]
                    nj = j + dx[k]
                    if 0<=ni<n and 0<=nj<n and graph[ni][nj] in [3,4]:
                        copy_graph[ni][nj] = 1
                copy_graph[i][j] = 2
            elif graph[i][j] ==3:
                tail_head = False
                for k in range(4):
                    ni = i + dy[k]
                    nj = j + dx[k]
                    if 0 <= ni < n and 0 <= nj < n and graph[ni][nj] == 2:
                        copy_graph[ni][nj] = 3
                    elif 0 <= ni < n and 0 <= nj < n and graph[ni][nj] == 1:
                        tail_head = True
                if tail_head:
                    pass
                else:
                    copy_graph[i][j] = 4
    graph = copy_graph
def find(r,c):
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[r][c] = 0
    q = deque()
    q.append((r,c))
    while q:
        r,c = q.popleft()
        if graph[r][c] == 1:
            return visited[r][c] + 1
        for k in range(4):
            nr = r + dy[k]
            nc = c + dx[k]
            if 0<=nr<n and 0<=nc<n and graph[nr][nc] in [1,2] and visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c]+1
                q.append((nr,nc))
def change_tail_head(r,c):
    hr,hc = -1,-1
    tr,tc = -1,-1

    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[r][c] = 0
    q = deque()
    q.append((r, c))
    while q:
        r, c = q.popleft()
        if graph[r][c] == 1:
           hr,hc = r,c
        elif graph[r][c] ==3:
            tr,tc = r,c
        for k in range(4):
            nr = r + dy[k]
            nc = c + dx[k]
            if 0 <= nr < n and 0 <= nc < n and graph[nr][nc] in [1, 2, 3, 4] and visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))
    graph[hr][hc] = 3
    graph[tr][tc] = 1

def ball(round):
    global ans
    round = round%(4*n)
    if round ==0:
        round = 4*n
    if 1<=round<=n:
        line = round-1
        for c in range(n):
            if graph[line][c] in [1,2,3]: #ball이 맞춤
                k = find(line,c)
                ans += k**2
                change_tail_head(line,c)
                break
    elif n<round<=2*n:
        line = round -(n+1)
        for r in range(n-1,-1,-1):
            if graph[r][line] in [1,2,3]:
                k = find(r, line)
                ans += k**2
                change_tail_head(r, line)
                break
    elif 2*n<round<=3*n:
        line = 3*n - round
        for c in range(n-1,-1,-1):
            if graph[line][c] in [1,2,3]: #ball이 맞춤
                k = find(line,c)
                ans += k**2
                change_tail_head(line,c)
                break
    elif 3*n<round<=4*n:
        line = 4*n - round
        for r in range(n):
            if graph[r][line] in [1,2,3]:
                k = find(r, line)
                ans += k**2
                change_tail_head(r, line)
                break
if P:
    print("처음")
print_graph()
for R in range(1,k+1):
    if P:
        print(R,"라운드")
    move()
    if P:
        print("이동 후")
        print_graph()
    ball(R)
    if P:
        print("공 처리")
        print_graph()
    if P:
        print(ans,"점")
print(ans)