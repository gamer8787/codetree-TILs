import sys
from collections import defaultdict

L, Q = map(int,sys.stdin.readline().rstrip().split())
chobab_in = defaultdict(dict)
person_in = {}
person_out = defaultdict(int)
snapshot = []
name_set = set()

query = []

for _ in range(Q):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == "100":
        name = command[3]
        t,x = int(command[1]),int(command[2])
        chobab_in[name][t] = x
        query.append([t,100])
    elif command[0] =="200":
        name = command[3]
        name_set.add(name)
        t, x = int(command[1]), int(command[2])
        n = int(command[4])
        person_in[name] = (t,x)
        query.append([t, 200])
    elif command[0] == "300":
        t = int(command[1])
        query.append([t, 300])

for name in name_set:
    name_chobab = chobab_in[name]
    pt,px = person_in[name]
    for ct,cx in list(name_chobab.items()):
        if pt <= ct: #초밥이 늦게 들어옴
            if cx == px:
                nt = ct
                query.append([nt,150])
            elif cx > px:
                nt = ct + L-(cx-px)
                query.append([nt,150])
            else:
                nt = ct + (px-cx)
                query.append([nt,150])
        else:
            ncx = ((pt-ct) + cx)%L
            if ncx==px:
                nt = pt
                query.append([nt,150])
            elif ncx > px:
                nt = pt + L-(ncx-px)
                query.append([nt,150])
            else:
                nt = pt + (px-ncx)
                query.append([nt,150])
        if nt > person_out[name]:
            person_out[name] = nt

for name in person_out:
    t = person_out[name]
    query.append([t,250])

query.sort()
np,nc = 0,0
for t,q in query:
    if q == 100:
        nc+=1
    elif q==200:
        np+=1
    elif q==150:
        nc-=1
    elif q==250:
        np-=1
    elif q==300:
        print(np,nc)