import heapq
from collections import defaultdict

Q = int(input())

c = list(map(int,input().split()))
N,M,P = c[1],c[2],c[3]
rabbit_distance = {}
rabbit_score={}
for i in range(4,len(c),2):
    rabbit_distance[c[i]] = c[i+1]
    rabbit_score[c[i]] = 0
rabbit = []
for key in rabbit_distance:
    heapq.heappush(rabbit,(0,2,1,1,key))
for _ in range(Q-2):
    c = list(map(int,input().split()))
    if c[0] == 200:
        K,S = c[1],c[2]
        # turn_rabbit = []
        turn_rabbit = set()
        for stage in range(1,K+1):
            # print(stage)
            avail = []

            jump,sij,i,j,pid = heapq.heappop(rabbit)
            # print(i,j,pid)
            d = rabbit_distance[pid]
            ############################
            #1 오른쪽
            nj = (j + d)%(2*M-2)
            if nj >M:
                nj = 2*M - nj
            avail.append([nj+i,i,nj])
            #2 아래
            ni = (i + d) % (2 * N - 2)
            if ni > N:
                ni = 2 * N - ni
            avail.append([ni + j, ni, j])
            #3 왼쪽
            nj = (j - d)%(2*M-2)
            if nj >M:
                nj = 2*M - nj
            avail.append([nj + i, i, nj])
            #4 위
            ni = (i - d) % (2 * N - 2)
            if ni > N:
                ni = 2 * N - ni
            avail.append([ni + j, ni, j])
            #############################
            avail.sort(key = lambda x:(-x[0],-x[1],-x[2]))
            _,new_i,new_j = avail[0]
            heapq.heappush(rabbit,(jump+1,new_i+new_j,new_i,new_j,pid))
            turn_rabbit.add(pid)
            # print(new_i, new_j, pid)
            # heapq.heappush(turn_rabbit,(-(new_i+new_j),-new_i,-new_j,-pid))
            for p in rabbit_score:
                if p==pid:
                    continue
                rabbit_score[p] += new_i+new_j
        rabbit.sort(key = lambda x:(-x[1],-x[2],-x[3],-x[4]))
        for _,_,i,j,pid in rabbit:
            if pid in turn_rabbit:
                rabbit_score[pid] += S
                break
    elif c[0] == 300:
        pid,L = c[1],c[2]
        rabbit_distance[pid] *=L
maximum = 0
for p in rabbit_score:
    maximum = max(rabbit_score[p],maximum)
print(maximum)