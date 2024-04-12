from collections import defaultdict, deque

q = int(input())
n,m = 0,0 #선물,벨트
ID_weight = {}
belt_set = defaultdict(set)
belt_deque = defaultdict(deque)

front = defaultdict(int)
back = defaultdict(int)
belt_first = {}
belt_last = {}
def p200(w_max):
    weight_sum = 0
    for b in range(1,m+1):
        if not belt_set[b]:
            continue
        first = belt_first[b]
        weight = ID_weight[first]
        if weight <= w_max:
            belt_set[b].remove(first)
            belt_first[b] = back[first]
            front[belt_first[b]] = 0

            weight_sum += weight
        else:
            if len(belt_set[b]) ==1:
                continue
            first = belt_first[b]
            second = back[first]
            last = belt_last[b]

            front[first] = last
            front[second] = 0

            belt_first[b] = second
            belt_last[b] = first

    print(weight_sum)
def p300(r_id):

    ret = -1
    for b in range(1,m+1):
        belt = belt_set[b]
        if r_id in belt:
            if len(belt) ==1:
                belt_first[b] = 0
                belt_last[b] = 0
            elif r_id == belt_last[b]:
                belt_last[b] = front[r_id]
            elif r_id == belt_first[b]:
                belt_first[b] = back[r_id]
            belt.remove(r_id)
            b1 = back[r_id]
            f1 = front[r_id]
            front[b1] = f1
            back[f1] = b1
            ret = r_id

    print(ret)

def p400(f_id):
    ret = -1

    for b in range(1,m+1):
        belt = belt_set[b]
        if f_id in belt:
            ret = b
            if f_id == belt_first[b]:
                continue
            first = belt_first[b]
            last = belt_last[b]
            front1 = front[f_id]
            back1 = back[f_id]

            front[first] = last
            back[last] = first
            back[front1] = 0
            back[back1] = first

            belt_last[b] = front1
            belt_first[b] = f_id
    print(ret)

def p500(b_num):
    if belt_destroy[b_num]:
        print(-1)
        return
    else:
        print(b_num)
        belt_destroy[b_num] = True
        bad_belt = b_num
        for good_belt in range(bad_belt+1,bad_belt+m+1):
            if good_belt > m:
                good_belt -=m
            if belt_destroy[good_belt] == False:
                if len(belt_set[bad_belt]) ==0:
                    break
                bad_first = belt_first[bad_belt]
                bad_last = belt_last[bad_belt]
                good_last = belt_last[good_belt]

                belt_set[good_belt] = belt_set[good_belt].union(belt_set[bad_belt])
                belt_set[bad_belt] = set()

                belt_first[bad_belt] = 0
                belt_last[bad_belt] = 0
                belt_last[good_belt] = bad_last

                front[bad_first] = good_last
                back[good_last] = bad_first

                break


for _ in range(q):
    c = list(map(int,input().split()))
    if c[0] == 100:
        n,m = c[1],c[2]
        ID = c[3:3+n]
        weight = c[3+n:]
        belt_destroy = [False for _ in range(m+1)]
        for id,w in zip(ID,weight):
            ID_weight[id] = w
        i = 3
        for b in range(1,m+1):
            for k in range(n//m):
                id = c[i]
                belt_set[b].add(id)
                belt_deque[b].append(id)
                i+=1

        for b in range(1,m+1):
            belt = belt_deque[b]
            for i,id in enumerate(belt):
                if i ==0:
                    continue
                else:
                    front[id] = belt[i - 1]
        for b in range(1,m+1):
            belt = belt_deque[b]
            for i,id in enumerate(belt):
                if i ==len(belt)-1:
                    continue
                else:
                    back[id] = belt[i + 1]

        for b in range(1, m + 1):
            belt = belt_deque[b]
            belt_first[b] = belt[0]
            belt_last[b] = belt[-1]

    elif c[0] == 200:
        w_max = c[1]
        p200(w_max)
    elif c[0] == 300:
        r_id  = c[1]
        p300(r_id)
    elif c[0] == 400:
        f_id = c[1]
        p400(f_id)
    elif c[0] == 500:
        b_num = c[1]
        p500(b_num)