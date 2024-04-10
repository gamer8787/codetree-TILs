n,k = map(int,input().split())
graph = [[0 for _ in range(n)] for _ in range(n)]
graph[n-1]= list(map(int,input().split()))

dy = [-1,0,1,0]
dx = [0,1,0,-1]

PRINT = False

def print_graph():
    if PRINT:
        for g in graph:
            print(*g)
        print()

def p1():
    global graph
    dow = graph[n-1]
    minimum = min(dow)
    dow = [i+1 if i==minimum else i for i in dow]
    graph[n - 1] = dow
def p2():
    global graph

    c_graph = [i[:] for i in graph]

    index = graph[n - 2].index(0)
    if index==0:
        index=1
    #기준점: (n-1, index)에 대하여 (a,b)가 회전
    for a in range(n):
        for b in range(index):
            if graph[a][b] == 0:
                continue
            c_graph[n-1-index+b][index+n-1-a] = graph[a][b]
    for a in range(n):
        c_graph[a] = c_graph[a][index:] + [0] * index
    index1 = c_graph[n - 2].index(0)
    index2 = c_graph[n - 1].index(0)
    if index1 > index2:
        return
    else:
        graph = c_graph
        p2()

def p3():
    global graph
    c_graph = [[0 for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if graph[r][c] == 0:
                continue
            for k in range(4):
                nr = r +dy[k]
                nc = c +dx[k]
                if 0<=nr<n and 0<=nc<n and graph[nr][nc]!=0:
                    if graph[nr][nc] > graph[r][c]:
                        c_graph[r][c] += ((graph[nr][nc] - graph[r][c]) //5)
                    else:
                        c_graph[r][c] -= ((graph[r][c] - graph[nr][nc]) // 5)
    for r in range(n):
        for c in range(n):
            graph[r][c] += c_graph[r][c]
    last_line = []
    for c in range(n):
        for r in range(n-1,-1,-1):
            if graph[r][c] !=0:
                last_line.append(graph[r][c])
    graph = [[0 for _ in range(n)] for _ in range(n)]
    graph[n-1] = last_line

def p4():
    a1 = graph[n-1][:n//2]
    a1 = a1[::-1]
    graph[n-2][:n//2] = a1
    graph[n-1][:n//2] = graph[n-1][n//2:]
    graph[n-1][n//2:] = [0] * (n//2)

    f1 = graph[n-2][:n//4]
    f2 = graph[n-1][:n//4]
    f1 = f1[::-1]
    f2 = f2[::-1]

    graph[n-4][:n//4] = f2
    graph[n-3][:n//4] = f1
    graph[n-2][:n//4] = graph[n-2][n//4:n//2]
    graph[n-2][n//4:] = [0] * (n-n//4)
    graph[n - 1][:n // 4] = graph[n - 1][n // 4:n // 2]
    graph[n - 1][n // 4:] = [0] * (n - n // 4)

def p5():
    p3()

def check():
    minimum = min(graph[n-1])
    maximum = max(graph[n-1])
    if maximum-minimum <= k :
        return True
    else:
        return False

round =1
while True:
    if PRINT:
        print(round,"라운드")
    p1()
    print_graph()
    p2()
    print_graph()
    p3()
    print_graph()
    p4()
    print_graph()
    p5()
    print_graph()
    if check():
        print(round)
        break
    round+=1