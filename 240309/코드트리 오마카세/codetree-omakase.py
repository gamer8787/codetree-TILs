from collections import defaultdict

L, Q = map(int,input().split())

name_chobab =defaultdict(list)
name_info = {}
for _ in range(Q):
    command = input().split()
    if command[0] == "100":
        name = command[3]
        t,x = int(command[1]),int(command[2])
        name_chobab[name].append([t,x])
    elif command[0] =="200":
        name = command[3]
        t, x = int(command[1]), int(command[2])
        n = int(command[4])
        name_info[name] = [t,x,n]
    elif command[0] == "300":
        time = int(command[1])
        peo_count =0
        cho_count = 0
        for name, info in name_info.items():
            chobab = name_chobab[name]
            arrival_time = info[0]
            place = info[1]
            remain_chobab = chobab[:]
            for i,(t,x) in enumerate(chobab):
                t = int(t)
                x = int(x)
                if arrival_time < t: #초밥이 늦게 나옴
                    next_x = x + (time-t)
                    other_place = place + L
                    if x<=place<=next_x or x<=other_place<=next_x: #초밥 먹음
                        info[2]-=1
                        remain_chobab.remove(chobab[i])
                        # print(time, name,chobab[i])
                else: #초밥이 먼저 나와 있음 #arrivalt_time에서의 위치를 구해야함
                    x = (x + (arrival_time-t))%L
                    next_x = x + (time-arrival_time)
                    other_place = place + L
                    if x<=place<=next_x or x<=other_place<=next_x: #초밥 먹음
                        info[2]-=1
                        remain_chobab.remove(chobab[i])
                        # print(time, name,chobab[i])
            name_chobab[name] = remain_chobab
            if info[2] > 0:
                peo_count +=1
        for name,cho in name_chobab.items():
            cho_count+= len(cho)
        print(peo_count,cho_count)