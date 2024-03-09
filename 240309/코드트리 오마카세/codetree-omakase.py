import heapq
import sys
from collections import defaultdict

L, Q = map(int,sys.stdin.readline().rstrip().split())

name_chobab =defaultdict(list)
name_info = {}
q = []
for _ in range(Q):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == "100":
        name = command[3]
        t,x = int(command[1]),int(command[2])
        if name in name_info:
            arrival,place,n = name_info[name]
            if x>place:
                out = t + (place+L-x)
                heapq.heappush(q,(out,name))
            else:
                out = t + (place-x)
                heapq.heappush(q,(out,name))
        else:
            name_chobab[name].append([t,x])
    elif command[0] =="200":
        name = command[3]
        arrival, place = int(command[1]), int(command[2])
        n = int(command[4])
        name_info[name] = [arrival,place,n]
        chobabs = name_chobab[name]
        for t,x in chobabs:
            new_x = (x+(arrival-t))%L
            if new_x>place:
                out = arrival + (place+L-new_x)
                heapq.heappush(q,(out,name))
            else:
                out = arrival + (place-new_x)
                heapq.heappush(q, (out,name))
        name_chobab.pop(name)

    elif command[0] == "300":
        time = int(command[1])
        peo_count =0
        cho_count = 0
        while q and q[0][0] <= time:
            _,name = heapq.heappop(q)
            name_info[name][2]-=1
        for name, info in name_info.items():
            if info[2] >0:
                peo_count+=1
        for name in name_chobab:
            cho_count+=len(name_chobab[name])
        print(peo_count,len(q)+cho_count)