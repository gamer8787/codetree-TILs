#산타 우선순위 상우하좌 4방향
N,M,P,C,D = map(int,input().split())
Rr,Rc = map(int,input().split())
santas = [list(map(int,input().split())) for _ in range(P)]
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
santa_info = {}
rudol_info ={}

def live(r,c):
    if 1<=r<=N and 1<=c<=N:
        return True
    else :
        return False
def crush(r,c,drk,dck,santa):
    if not live(r,c):
        return
    if graph[r][c] == 0 :
        graph[r][c] = santa
        santa_info[santa][0] = r
        santa_info[santa][1] = c
        return
    other_santa = graph[r][c]
    graph[r][c] = santa
    santa_info[santa][0] = r
    santa_info[santa][1] = c
    new_r,new_c = r+drk,c+dck
    crush(new_r,new_c,drk,dck,other_santa)

def pp():
    for g in graph[1:]:
        print(*g[1:])
    print()
for n,r,c in santas:
    graph[r][c] = n
    santa_info[n] = [r,c,0,0]
graph[Rr][Rc] = -1

dr = [-1,0,1,0,-1,-1,1,1]
dc = [0,1,0,-1,-1,1,1,-1]
# pp()

# M=1
live_santa = set([i for i in range(1,P+1)])
for turn in range(1,M+1):
    if not live_santa:
        break
    distance_r_c = []
    for k in range(8):
        nr = Rr+dr[k]
        nc = Rc+dc[k]
        for san in range(1,P+1):
            sr,sc,bo,score = santa_info[san]
            if san not in live_santa:
                continue
            distance = (sr-nr)**2 + (sc-nc)**2
            distance_r_c.append([distance,sr,sc,nr,nc,dr[k],dc[k]])
    distance_r_c.sort(key= lambda x:(x[0],-x[1],-x[2]))
    dis,sr,sc,nr,nc,drk,dck = distance_r_c[0]
    graph[Rr][Rc] = 0
    Rr = nr
    Rc = nc
    if graph[Rr][Rc] > 0: #산타 루돌프 충돌 (4)
        santa = graph[Rr][Rc]
        graph[Rr][Rc] = -1
        santa_info[santa][3] += C #점수 올림
        santa_info[santa][2] = turn+1 #기절함       (6)
        new_r,new_c = C*drk + Rr, C*dck + Rc #산타 새 위치
        crush(new_r,new_c, drk,dck,santa)
    else:
        graph[Rr][Rc] = -1
    # print(santa_info)
    # pp()
    for santa in range(1,P+1):
        san_r,san_c,stun,score = santa_info[santa] # (3)

        if santa in live_santa and stun < turn :
            distance_d = []
            distance = (san_r-Rr)**2 + (san_c-Rc)**2
            distance_d.append([distance,0,san_r,san_c,0,0])
            graph[san_r][san_c] = 0
            for k in range(4):
                new_r = san_r+ dr[k]
                new_c = san_c+ dc[k]
                if not live(new_r,new_c) or graph[new_r][new_c] > 0:
                    continue
                distance = (new_r-Rr)**2 + (new_c-Rc)**2
                distance_d.append([distance,k,new_r,new_c,dr[k],dc[k]])
            distance_d.sort(key = lambda x:(x[0],x[1]))
            _,_,new_r,new_c,drk,dck = distance_d[0]
            if graph[new_r][new_c] == -1: # 루돌프 충돌(4)
                santa_info[santa][3] += D
                santa_info[santa][2] = turn + 1
                new_r = new_r - D*drk
                new_c = new_c - D*dck
                crush(new_r,new_c,-drk,-dck,santa)
            else:
                graph[new_r][new_c] = santa
    live_santa = set()
    for i in range(1,N+1):
        for j in range(1,N+1):
            if graph[i][j] >0 :
                santa = graph[i][j]
                live_santa.add(santa)
                santa_info[santa][0] = i
                santa_info[santa][1] = j
                santa_info[santa][3] +=1
    # print(santa_info)
    # pp()
for san in range(1,P+1):
    print(santa_info[san][3], end=" ")