import copy
from collections import deque
K,M = map(int,input().split())
treasure = [list(map(int,input().split())) for _ in range(5)]
numbers = list(map(int,input().split()))


dy = [-1,0,1,0]
dx = [0,1,0,-1]
ret =[]
turn_score = 0
index = 0
def p(graph):
    for i in range(5):
        print(*graph[i])
    print()


def bfs_score(sy,sx,graph,visited):
    visited[sy][sx] = True
    number = graph[sy][sx]
    score = 1
    q = deque()
    q.append((sy,sx))
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<5 and 0<=nx<5 and graph[ny][nx] == number and visited[ny][nx] == False:
                visited[ny][nx] = True
                score+=1
                q.append((ny,nx))
    return score

def get_score(graph):
    visited = [[False for _ in range(5)] for _ in range(5)]
    sum_score = 0
    for i in range(5):
        for j in range(5):
            if visited[i][j] == False:
                score = bfs_score(i,j,graph,visited)
                if score >=3:
                    sum_score+=score
    return sum_score

def rotate90(ry,rx,graph):
    copy_graph = copy.deepcopy(graph)
    for y in range(ry-1,ry+2):
        for x in range(rx-1,rx+2):
            oy = y - (ry-1)
            ox = x - (rx-1)
            ky = ox
            kx = 2- oy
            ny = ky + (ry-1)
            nx = kx + (rx-1)
            copy_graph[ny][nx] = graph[y][x]
    return copy_graph

def rotate180(ry,rx,graph):
    cop = rotate90(ry,rx,graph)
    cop2 = rotate90(ry,rx,cop)
    return cop2

def rotate270(ry,rx,graph):
    cop = rotate90(ry,rx,graph)
    cop2 = rotate90(ry,rx,cop)
    cop3= rotate90(ry, rx, cop2)
    return cop3


def make_zero(graph,sy,sx,visited):
    visited[sy][sx] = True
    number = graph[sy][sx]
    graph[sy][sx] = 0
    q = deque()
    q.append((sy, sx))
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < 5 and 0 <= nx < 5 and graph[ny][nx] == number and visited[ny][nx] == False:
                visited[ny][nx] = True
                graph[ny][nx] = 0
                q.append((ny, nx))

def fill(graph):
    global index
    visited = [[False for _ in range(5)] for _ in range(5)]
    visited2 = [[False for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if visited[i][j] == False:
                score = bfs_score(i, j, graph, visited)
                if score >= 3:
                    make_zero(graph,i,j,visited2)
    for j in range(5):
        for i in range(4,-1,-1):
            if graph[i][j] == 0:
                graph[i][j] =  numbers[index]
                index+=1

def process1():
    global treasure,turn_score
    turn_score = 0
    score_list = []
    for i in range(1,4):
        for j in range(1,4):
            c90 = rotate90(i,j,treasure)
            c180 = rotate180(i, j, treasure)
            c270 = rotate270(i, j, treasure)
            s90 = get_score(c90)
            s180 = get_score(c180)
            s270 = get_score(c270)
            score_list.append([s90,90,j,i])
            score_list.append([s180, 180, j, i])
            score_list.append([s270, 270, j, i])
    score_list.sort(key = lambda x:[-x[0],x[1],x[2],x[3]])
    score, angle, col, row = score_list[0]
    if angle == 90:
        treasure = rotate90(row,col,treasure)
        turn_score+=score
    elif angle == 180:
        treasure = rotate180(row,col,treasure)
        turn_score+=score
    elif angle == 270:
        treasure = rotate270(row,col,treasure)
        turn_score+=score

for _ in range(K):
    process1()
    fill(treasure)
    if turn_score==0:
        break
    while True:
        score = get_score(treasure)
        if score>0:
            turn_score+=score
        else:
            break
        fill(treasure)
    ret.append(turn_score)
print(*ret)