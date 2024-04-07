n,m,h,k = map(int,input().split())

dy = [-1,0,1,0]
dx = [0,1,0,-1]

runner = []
for _ in range(m):
    y,x,d = map(int,input().split())
    y-=1
    x-=1
    runner.append([y,x,d,True])
tree = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(h):
    y,x = map(int,input().split())
    y-=1
    x-=1
    tree[y][x] = 1
#술래 위치
y = n//2
x = n//2
d = 0

sullae_place_direction = [] # n = 5 ,1,1,2,2,3,3,4,4,4, 4,4,4,3,3,2,2,1,1
length = 1
l = 0
repeat = 0
while length < n-1:
    sullae_place_direction.append([y, x, d])
    y = y + dy[d]
    x = x + dx[d]
    l+=1
    if length==l:
        if repeat ==0:
            d = (d+1)%4
            l = 0
            repeat+=1
        else:
            repeat = 0
            d = (d + 1) % 4
            length+=1
            l = 0
for _ in range(3):
    for _ in range(n-1):
        sullae_place_direction.append([y, x, d])
        y = y + dy[d]
        x = x + dx[d]
    d = (d+1) %4
d = 2

for _ in range(3):
    for _ in range(n-1):
        sullae_place_direction.append([y, x, d])
        y = y + dy[d]
        x = x + dx[d]
    d = (d-1) %4

length = n-2
l = 0
repeat = 0


while length >0 :
    sullae_place_direction.append([y, x, d])
    y = y + dy[d]
    x = x + dx[d]
    l += 1
    if length == l:
        if repeat == 0:
            d = (d - 1) % 4
            l = 0
            repeat += 1
        else:
            repeat = 0
            d = (d - 1) % 4
            length -= 1
            l = 0

ey, ex, ed = sullae_place_direction[0]
ans = 0

for turn in range(1,k+1):
    #도망자 움직임
    for i,(y,x,d,is_live) in enumerate(runner):
        if is_live==False:
            continue
        distance = abs(ey-y) + abs(ex-x)
        if distance > 3:
            continue
        ny = y + dy[d]
        nx = x + dx[d]
        if 0<=ny <n and 0<=nx<n:
            if ny == ey and nx == ex:
                continue
            else:
                runner[i][0] = ny
                runner[i][1] = nx
        else:
            d = (d+2)%4
            runner[i][2] = d
            ny = y +dy[d]
            nx = x +dx[d]
            if ny == ey and nx == ex:
                continue
            else:
                runner[i][0] = ny
                runner[i][1] = nx
    #술래 이동
    r = turn % (2 * (n ** 2 - 1))
    ey, ex, ed = sullae_place_direction[r]

    #도망자 잡기
    for i, (y, x, d, is_live) in enumerate(runner):
        ey2 = ey + dy[ed]
        ex2 = ex + dx[ed]
        ey3 = ey2 + dy[ed]
        ex3 = ex2 + dx[ed]
        if [y,x] in [[ey,ex],[ey2,ex2],[ey3,ex3]] and tree[y][x]==0 and is_live==True:
            runner[i][3] = False
            ans+=turn
print(ans)