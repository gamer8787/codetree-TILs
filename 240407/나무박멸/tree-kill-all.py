n,m,k,c = map(int,input().split())
#격자수 박멸년수 대각선 제초제 수명
tree = [list(map(int,input().split())) for _ in range(n)]
year = [[0 for _ in range(n)] for _ in range(n)] #제초제가 살아있는 년도

dy = [-1,0,1,0]
dx = [0,1,0,-1]

dy2 = [1,1,-1,-1]
dx2 = [1,-1,1,-1]

ans = 0
def grow(time):
    produce = [[0 for _ in range(n)] for _ in range(n)]


    for y in range(n):
        for x in range(n):
            if tree[y][x] > 0 :
                can =0
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if 0<=ny<n and 0<=nx<n and tree[ny][nx]==0 and year[ny][nx] < time:
                        can +=1
                    elif 0<=ny<n and 0<=nx<n and tree[ny][nx]>0:
                        tree[y][x]+=1
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if 0 <= ny < n and 0 <= nx < n and tree[ny][nx] == 0 and year[ny][nx] < time:
                        produce[ny][nx] += (tree[y][x]//can)

    for y in range(n):
        for x in range(n):
            tree[y][x] += produce[y][x]

def remove(y):
    global ans
    maximum = 0
    ry,rx = -1,-1
    for y in range(n):
        for x in range(n):
            if tree[y][x] > 0:
                can_remove = tree[y][x]
                for i in range(4): #대각선 방향
                    ny = y
                    nx = x
                    for _ in range(k): #k번 이동
                        ny = ny + dy2[i]
                        nx = nx + dx2[i]
                        if 0<=ny <n and 0<=nx<n and tree[ny][nx]>0:
                            can_remove += tree[ny][nx]
                        else:
                            break
                if can_remove > maximum:
                    maximum = can_remove
                    ry = y
                    rx = x
    ans += maximum
    tree[ry][rx] = 0
    year[ry][rx] = y + c
    for i in range(4):
        ny = ry
        nx = rx
        for _ in range(k):  # k번 이동
            ny = ny + dy2[i]
            nx = nx + dx2[i]
            if 0 <= ny < n and 0 <= nx < n and tree[ny][nx] > 0:
                tree[ny][nx] = 0
                year[ny][nx] = y + c
            else:
                break
for y in range(1,m+1):
    grow(y)
    remove(y)
print(ans)