from collections import deque, defaultdict

dy = [-1,0,1,0]
dx = [0,1,0,-1]

n = int(input())
color_graph = [list(map(int,input().split())) for _ in range(n)]

number_graph = [[0 for _ in range(n)] for _ in range(n)]
group_count = {}
number_color = {}
edges = defaultdict(int)

P = True

def print_color_graph():
    if P:
        print("color_graph")
        for n in color_graph:
            print(*n)
        print()

def print_number_graph():
    if P:
        print("number graph")
        for n in number_graph:
            print(*n)
        print()

def print_group_count():
    if P:
        print("group count")
        print(group_count)
        print()

def print_edges():
    if P:
        print("edges")
        print(edges)
        print()

#r,c에 속한 그룹 num번으로 정함
def bfs(r,c,num,visited):
    global number_graph
    color = color_graph[r][c]
    number_color[num] = color
    q = deque()
    q.append((r,c))
    count=1
    number_graph[r][c] = num
    visited[r][c] = True
    while q:
        r,c = q.popleft()
        for k in range(4):
            nr = r + dy[k]
            nc = c + dx[k]
            if 0<=nr<n and 0<=nc < n and visited[nr][nc] == False and color_graph[nr][nc] == color:
                visited[nr][nc] = True
                number_graph[nr][nc] = num
                count+=1
                q.append((nr,nc))
    group_count[num] = count

def numbering():
    visited = [[False for _ in range(n)] for _ in range(n)]
    num = 1
    for r in range(n):
        for c in range(n):
            if visited[r][c] == False:
                bfs(r,c,num,visited)
                num+=1

def bfs_edge(r,c,visited):
    number = number_graph[r][c]
    visited[r][c] = True
    q = deque()
    q.append((r,c))
    while q:
        r,c = q.popleft()

        for k in range(4):
            nr = r + dy[k]
            nc = c + dx[k]
            if 0 <= nr < n and 0 <= nc < n:
                if number_graph[nr][nc] < number:
                    number2 = number_graph[nr][nc]
                    edges[(number2,number)] +=1
        for k in range(4):
            nr = r + dy[k]
            nc = c + dx[k]
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == False and number_graph[nr][nc] == number:
                visited[nr][nc] = True
                q.append((nr,nc))
def count_edge():
    visited = [[False for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if visited[r][c] == False:
                bfs_edge(r,c,visited)
def calculate():
    ret = 0
    for (n1,n2) in edges:
        edge = edges[(n1,n2)]
        g1 = group_count[n1]
        g2 = group_count[n2]
        c1 = number_color[n1]
        c2 = number_color[n2]
        ret += (g1+g2)*c1*c2*edge
    return ret

def rotate1():
    global color_graph
    copy_graph = [i[:] for i in color_graph]

    #세로 라인 (r,n//2) = > (n-1-n//2,r)
    for r in range(n):
        copy_graph[n-1-n//2][r] = color_graph[r][n//2]
    #가로 라인 (n//2,c) => (n-1-c,n//2)
    for c in range(n):
        copy_graph[n-1-c][n//2] = color_graph[n//2][c]
    color_graph = copy_graph

def rotate2():
    global color_graph
    copy_graph = [i[:] for i in color_graph]

    for y in range(n//2):
        for x in range(n//2):
            copy_graph[x][n//2-1-y] = color_graph[y][x]

    for y in range(n//2):
        for x in range(n//2+1,n):
            oy = y
            ox = x-(n//2+1)
            ry = ox
            rx = n//2-1-oy
            ny = ry
            nx = rx + (n//2+1)
            copy_graph[ny][nx] = color_graph[y][x]

    for y in range(n//2+1,n):
        for x in range(n//2):
            oy = y-(n//2+1)
            ox = x
            ry = ox
            rx = n//2-1-oy
            ny = ry + (n//2+1)
            nx = rx
            copy_graph[ny][nx] = color_graph[y][x]

    for y in range(n//2+1,n):
        for x in range(n//2+1,n):
            oy = y-(n//2+1)
            ox = x-(n//2+1)
            ry = ox
            rx = n//2-1-oy
            ny = ry + (n//2+1)
            nx = rx + (n//2+1)
            copy_graph[ny][nx] = color_graph[y][x]
    color_graph = copy_graph

def init():
    global number_graph,group_count,number_color,edges
    number_graph = [[0 for _ in range(n)] for _ in range(n)]
    group_count = {}
    number_color = {}
    edges = defaultdict(int)

ans = 0
for _ in range(4):
    init()
    numbering()
    count_edge()
    score = calculate()
    rotate1()
    rotate2()
    ans+=score
print(ans)