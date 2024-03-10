#우하좌상
from collections import deque

dy = [0,1,0,-1,-1,-1,1,1]
dx = [1,0,-1,0,-1,1,-1,1]
#가장 최근에 공격을 한 것, 방금 공격 에서 공격을 받으면 그 시간이 기록됨
N,M,K = map(int,input().split())
AD = [list(map(int, input().split())) for _ in range(N)]
turret = [[[0,0] for _ in range(M)] for _ in range(N)]

def pp():
    for a in AD:
        print(*a)
    print()

for stage in range(1,K+1):
    #1 공격자 선정
    attackers = []
    for i in range(N):
        for j in range(M):
            if AD[i][j] > 0:
                turret_info = [AD[i][j],turret[i][j][0],i+j,j,i]
                attackers.append(turret_info)
    if len(attackers) == 0:
        break
    attackers.sort(key = lambda x:(x[0],-x[1],-x[2],-x[3]))
    first = attackers[0]
    _,_,_,ac,ar = first
    AD[ar][ac] += (N+M)
    turret[ar][ac][0] = stage
    ad = AD[ar][ac]

    #2 공격자의 공격
    victims = []
    for i in range(N):
        for j in range(M):
            if i == ar and j == ac:
                continue
            if AD[i][j] > 0:
                turret_info = [AD[i][j], turret[i][j][0], i + j, j, i]
                victims.append(turret_info)
    if len(victims) == 0:
        break
    victims.sort(key=lambda x: (-x[0], x[1], x[2], x[3]))
    second = victims[0]
    _, _, _, vc, vr = second
    turret[vr][vc][1] = stage

    #2-1 레이저 공격 #ar,ac 에서 vr,vc로
    visited = [["" for _ in range(N)] for _ in range(N)]
    q = deque()
    q.append((ar,ac))
    while q:
        r,c = q.popleft()
        for k in range(4):
            nr = (r + dy[k])%N
            nc = (c + dx[k])%M
            if (not (nr==ar and nc==ac)
                    and visited[nr][nc] == "" and AD[nr][nc] > 0):
                visited[nr][nc] = visited[r][c] + str(k)
                q.append((nr,nc))
    direction = visited[vr][vc]
    # print(direction)
    nr,nc = ar,ac
    if direction!="": #레이저 공격
        AD[vr][vc] -= ad
        for d in direction[:-1]:
            d = int(d)
            nr = (nr + dy[d])%N
            nc = (nc + dx[d])%M
            AD[nr][nc] -= ad//2
            turret[nr][nc][1] = stage
    # for a in AD:
    #     print(a)
    else:  #포탄 공격
        AD[vr][vc] -= ad
        for k in range(8):
            nr = (vr + dy[k])%N
            nc = (vc + dx[k])%M
            if not (nr==ar and nc==ac):
                AD[nr][nc] -= ad//2
                turret[nr][nc][1] = stage
    #3 포탑 부서짐
    for i in range(N):
        for j in range(M):
            AD[i][j] = max(AD[i][j],0)

    #4 포탑 정비
    for i in range(N):
        for j in range(M):
            if ar==i and ac==j:
                continue
            if vr==i and vc==j:
                continue
            if turret[i][j][1] == stage:
                continue
            if AD[i][j] > 0:
                AD[i][j]+=1
    # pp()
maximum_ad = max(map(max , AD))
print(maximum_ad)