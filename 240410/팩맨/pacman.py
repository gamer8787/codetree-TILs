m,t = map(int,input().split())
R,C = map(int,input().split())

dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,-1,-1,-1,0,1,1,1]

monster_graph = [[0 for _ in range(5)] for _ in range(5)]
dead_graph = [[0 for _ in range(5)] for _ in range(5)]

monster = []
for _ in range(m):
    r,c,d = map(int,input().split())
    monster.append([r,c,d-1])
egg = []

P = False

def print_monster_graph():
    if P:
        print("몬스터 그래프")
        temp = [[0 for _ in range(5)] for _ in range(5)]
        for r,c,d in monster:
            temp[r][c] +=1
        for m in temp:
            print(*m)
        print()

def print_pac():
    if P:
        print("팩맨 위치")
        temp = [[0 for _ in range(5)] for _ in range(5)]
        temp[R][C] = "*"
        for m in temp:
            print(*m)
        print()

def print_monster():
    if P:
        print("몬스터")
        print(monster)
        print()

def produce():
    global egg
    egg = monster[:]

def move_mon():
    global monster
    new_monster = []
    for r,c,d in monster:
        new_place = [[8,r,c,d]]
        for k in range(8):
            nr = r + dy[(d+k)%8]
            nc = c + dx[(d+k)%8]
            if 1<=nr <=4 and 1<=nc<=4 and not( nr== R and nc ==C) and dead_graph[nr][nc] < T:
                new_place.append([k,nr,nc,(d+k)%8])
        new_place.sort()
        k,nr,nc,nd = new_place[0]
        new_monster.append([nr,nc,nd])
    monster = new_monster
    for r,c,d in monster:
        monster_graph[r][c]+=1

def move_pac():
    global R,C,monster
    new_pac = []
    for i1 in [0,2,4,6]:
        for i2 in [0, 2, 4, 6]:
            for i3 in [0, 2, 4, 6]:
                new_pac.append([i1,i2,i3])
    new_place = []
    for i1,i2,i3 in new_pac:
        r1 = R + dy[i1]
        c1 = C + dx[i1]
        if not (1<=r1<=4 and 1<=c1<=4):
            continue
        r2 = r1 + dy[i2]
        c2 = c1 + dx[i2]
        if not (1 <= r2 <= 4 and 1 <= c2 <= 4):
            continue
        r3 = r2 + dy[i3]
        c3 = c2 + dx[i3]
        if not (1 <= r3 <= 4 and 1 <= c3 <= 4):
            continue
        avail = set()
        avail.add((r1,c1))
        avail.add((r2,c2))
        avail.add((r3, c3))
        count = 0
        for r,c in avail:
            count += monster_graph[r][c]
        new_place.append([count,i1,i2,i3])

    new_place.sort(key = lambda x:(-x[0],x[1],x[2],x[3]))
    count,i1,i2,i3 = new_place[0]
    r1 = R + dy[i1]
    c1 = C + dx[i1]
    r2 = r1 + dy[i2]
    c2 = c1 + dx[i2]
    r3 = r2 + dy[i3]
    c3 = c2 + dx[i3]
    R,C = r3,c3
    new_monster = []
    for r,c,d in monster:
        if [r,c] in [[r1,c1],[r2,c2],[r3,c3]]:
            dead_graph[r][c] = T+2
        else:
            new_monster.append([r,c,d])
    monster = new_monster

def come():
    monster.extend(egg)

def init():
    global monster_graph
    monster_graph = [[0 for _ in range(5)] for _ in range(5)]

print_monster_graph()
print_pac()
for T in range(1,t+1):
    if P:
        print(T,"턴")
    init()
    produce()
    move_mon()
    if P:
        print("몬스터 이동")
    print_monster_graph()
    move_pac()
    if P:
        print("팩맨 이동")
    print_pac()
    print_monster_graph()
    come()
    if P:
        print("알 부화")
    print_monster_graph()


print(len(monster))