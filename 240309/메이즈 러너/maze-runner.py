import sys
input = sys.stdin.readline

def move(sr, sc, er, ec):
    dist = abs(sr-er)+abs(sc-ec)
    distance = dist
    rr, cc = sr, sc
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx, ny = sr+dx, sc+dy
        if 0 <= nx < N and 0 <= ny < N and not A[nx][ny]:
            dd = abs(nx-er)+abs(ny-ec)
            if dd < dist:
                dist, rr, cc, = dd, nx, ny
    return rr, cc, distance-dist

def find_square():
    for l in range(1, N):
        for r in range(N):
            for c in range(N):
                if r <= er <= r+l and c <= ec <= c+l:
                    for i in range(l+1):
                        for j in range(l+1):
                            if r+i < N and c+j < N and P[r+i][c+j]:
                                return r, c, l+1

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
P = [[[] for _ in range(N)] for _ in range(N)]
player = dict()
for idx in range(M):
    r, c = map(lambda x: int(x)-1, input().split())
    P[r][c].append(idx)
    player[idx] = [r, c]
er, ec = map(lambda x: int(x)-1, input().split())

answer = 0
for _ in range(K):
    if player:
        delete = []
        for idx, (sr, sc) in player.items():
            nx, ny, result = move(sr, sc, er, ec)
            answer += result
            P[sr][sc].remove(idx)
            if (nx, ny) == (er, ec):
                delete.append(idx)
            else:
                player[idx] = [nx, ny]
                P[nx][ny].append(idx)
        for idx in delete:
            del player[idx]
        if not player: break

    rr, cc, l = find_square()
    rotate = dict()
    for r in range(l):
        for c in range(l):
            rotate[(rr+r, cc+c)] = (rr+c, cc+l-r-1)

    NP = [[e[:] for e in row] for row in P]
    B = [row[:] for row in A]
    er, ec = rotate[(er, ec)]
    for (r, c), (nx, ny) in rotate.items():
        if P[r][c]:
            for idx in P[r][c]:
                player[idx] = [nx, ny]
        NP[nx][ny] = P[r][c]
        B[nx][ny] = max(0, A[r][c]-1)
    A, P = B, NP

print(answer)
print(er+1, ec+1)