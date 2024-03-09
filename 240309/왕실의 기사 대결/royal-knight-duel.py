L,N,Q = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(L)]
knights = []
damage = {}
for n in range(N):
    r,c,h,w,k = map(int,input().split())
    knights.append([r-1,c-1,h,w,k])
    damage[n+1] = k
commands = [list(map(int,input().split())) for _ in range(Q)]
TRAP=1
WALL=2
dy = [-1,0,1,0]
dx = [0,1,0,-1]

knight_graph = [[0 for _ in range(L)] for _ in range(L)]
for n,(r,c,h,w,k) in enumerate(knights):
    knight = n+1
    for i in range(h):
        for j in range(w):
            knight_graph[r+i][c+j] = knight

def pp():
    for g in knight_graph:
        print(g)
    print()

def bound(r,c):
    if 0<=r <L and 0<=c<L:
        return True
    else:
        return False
def check(knight,d,command):
    r,c,h,w,k = knights[knight-1]
    if k <= 0:
        return
    ret = True
    neigh_knight = set()
    for i in range(r, r + h):
        for j in range(c, c + w):
            if not bound(i+dy[d],j+dx[d]): #밖이면 못 감
                return False
            if graph[i+dy[d]][j+dx[d]] ==WALL:
                return False
            other_knight = knight_graph[i+dy[d]][j+dx[d]]
            if other_knight!=knight and other_knight!=0:
                neigh_knight.add(other_knight)
    for neigh in neigh_knight:
        ret = ret & check(neigh,d,False)

    if ret:
        move = []
        knights[knight - 1][0] = r+dy[d]
        knights[knight - 1][1] = c + dx[d]
        for i in range(r,r+h):
            for j in range(c,c+w):
                move.append([i+dy[d], j+dx[d]])
                knight_graph[i][j] = 0
        for i,j in move:
            knight_graph[i][j] = knight
            if graph[i][j] == TRAP and (not command):
                knights[knight - 1][4]-=1
        if knights[knight - 1][4] <= 0:
            for i,j in move:
                knight_graph[i][j] = 0

    # print(knight,ret)
    return ret
# pp()
for knight, d in commands:
    check(knight,d,True)
    # pp()

sum_damage = 0
for i,(r,c,w,h,k) in enumerate(knights):
    if k >0:
        sum_damage += (damage[i+1] - k)
print(sum_damage)