N,M,K = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
participant = [[[] for _ in range(N)] for _ in range(N)]
dy = [-1,1,0,0]
dx = [0,0,1,-1]
for n in range(M):
    i,j = map(int,input().split())
    participant[i-1][j-1].append(n)

ey,ex = map(int,input().split())
ey-=1
ex-=1
moving_distance = 0
def move():
    global participant,moving_distance
    temp_participant = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if participant[i][j]:
                ret = []
                distance = abs(i-ey) + abs(j-ex)
                ret.append([distance,-1,i,j])
                for k in range(4):
                    ny = i +dy[k]
                    nx = j + dx[k]
                    if 0<=ny<N and 0<=nx<N and graph[ny][nx] == 0:
                        distance = abs(ny-ey) + abs(nx-ex)
                        ret.append([distance,k,ny,nx])
                ret.sort()
                _,k,ny,nx = ret[0]
                if k>=0:
                    moving_distance+=len(participant[i][j])
                if ny == ey and nx == ex: #나가게 됨
                    continue
                temp_participant[ny][nx].extend(participant[i][j])
    participant = temp_participant
def rotate_square(i,j,minimum): #회전하고 출구 좌표도 잡아줘야됨
    global ey,ex
    copy_graph =[i[:] for i in graph]
    copy_participant = [i[:] for i in participant]
    for y in range(minimum+1):
        for x in range(minimum+1):
            graph[i+y][j+x] = copy_graph[i+minimum-x][j+y]
            if graph[i+y][j+x] > 0 :
                graph[i + y][j + x]-=1
            participant[i + y][j + x] = copy_participant[i + minimum - x][j + y]
    y = ey - i
    x = ex - j
    ey = i +x
    ex = j+minimum - y
def rotate():
    minimum = 10**9
    for i in range(N):
        for j in range(N):
            if participant[i][j]:
                distance = max(abs(i-ey) , abs(j-ex))
                minimum = min(minimum,distance)
    if minimum == 10**9:
        return
    for i in range(N-minimum):
        for j in range(N-minimum):
            have_exit =False
            have_participant =False
            for i2 in range(minimum+1):
                for j2 in range(minimum+1):
                    if i+i2 == ey and j+j2 == ex:
                        have_exit = True
                    if participant[i+i2][j+j2]:
                        have_participant=True
            # print(minimum,have_exit,have_participant)
            if have_exit and have_participant:
                rotate_square(i, j, minimum)
                return
def pp():
    for g in graph:
        print(g)
    print()
    for g in participant:
        print(g)
    print()
# pp()
for i in range(K):
    # print(ey,ex)
    # print(i+1)
    move()
    # pp()
    rotate()
    # pp()
print(moving_distance)
print(ey+1,ex+1)