Q = int(input())

n,m =0,0 #벨트, 선물 개수
belt = []
front_behind = []
def p100(l):
    global n,m,belt,front_behind
    n, m = l[1],l[2]
    belt = [[] for  _ in range(n+1)]
    front_behind = [[-1, -1] for _ in range(m + 1)]
    for i in range(3,3+m):
        k = l[i]
        belt[k].append(i-2)
    for b in range(1,n+1):
        belt[b] = belt[b][::-1]

    for b in range(1,n+1):
        my_belt = belt[b]
        length = len(my_belt)
        if length <=1:
            continue
        for i in range(length):
            n = my_belt[i]
            if i ==0:
                front_behind[n] = [my_belt[i+1],-1]
            elif i == length-1:
                front_behind[n] = [-1,my_belt[i-1]]
            else:
                front_behind[n] = [my_belt[i + 1], my_belt[i-1]]

def p200(src,dst):
    if not belt[src]:
        print(len(belt[dst]))
        return
    src_first = belt[src][0]
    if belt[dst]:
        dst_last = belt[dst][-1]
        belt[dst].extend(belt[src])
        belt[src] = []
        front_behind[src_first][1] = dst_last
        front_behind[dst_last][0] = src_first
    else:
        belt[dst].extend(belt[src])
        belt[src] = []

    print(len(belt[dst]))
def p300(src,dst):
    belt_src = belt[src]
    belt_dst = belt[dst]
    if belt_src and belt_dst:
        src_last = belt_src[-1]
        dst_last = belt_dst[-1]
        if len(belt_src) == 1 and len(belt_dst) == 1:
            belt[src] = [dst_last]
            belt[dst] = [src_last]
        elif len(belt_src) == 1 and len(belt_dst) >= 1:
            belt[src] = [dst_last]
            belt[dst][-1] = src_last
            front_behind[dst_last] = [-1,-1]
            front_behind[src_last] = [-1, belt_dst[-2]]
            front_behind[belt_dst[-2]][0] = src_last
        elif len(belt_src) >= 1 and len(belt_dst) == 1:
            belt[src][-1] = dst_last
            belt[dst] = [src_last]
            front_behind[src_last] = [-1,-1]
            front_behind[dst_last] = [-1,belt_src[-2]]
            front_behind[belt_src[-2]][0] = dst_last
        else:
            belt[src][-1] = dst_last
            belt[dst][-1] = src_last
            front_behind[src_last] = [-1,belt_dst[-2]]
            front_behind[dst_last] = [-1,belt_src[-2]]
            front_behind[belt_src[-2]][0] = dst_last
            front_behind[belt_dst[-2]][0] = src_last
    elif belt_src and not belt_dst:
        if len(belt_src) ==1:
            belt[dst] = belt[src]
            belt[src] = []
        else:
            src_last = belt_src[-1]
            belt[dst] = [src_last]
            belt[src] = belt[src][:-1]
            front_behind[src_last] = [-1,-1]
            front_behind[belt_src[-1]][0] = -1
    elif not belt_src and belt_dst:
        if len(belt_dst) ==1:
            belt[src] = belt[dst]
            belt[dst] = []
        else:
            dst_last = belt_dst[-1]
            belt[src] = [dst_last]
            belt[dst] = belt[dst][:-1]
            front_behind[dst_last] = [-1,-1]
            front_behind[belt_dst[-1]][0] = -1
    else:
        pass
    print(len(belt[dst]))

def p400(src,dst):
    belt_src = belt[src]
    belt_dst = belt[dst]
    length = len(belt_src)
    if length <=1:
        pass
    elif belt_dst:
        dst_last = belt_dst[-1]
        src_mid1 = belt_src[(length-1)//2]
        src_mid2 = belt_src[(length-1)//2+1]

        front_src = belt_src[((length-1)//2+1):]
        belt[src] = belt_src[:((length-1)//2+1)]
        belt[dst].extend(front_src)

        front_behind[dst_last][0] = src_mid2
        front_behind[src_mid1][0] = -1
        front_behind[src_mid2][1] = dst_last
    else:
        src_mid1 = belt_src[(length-1) // 2]
        src_mid2 = belt_src[(length-1) // 2 + 1]

        front_src = belt_src[((length-1) // 2 + 1):]
        belt[src] = belt_src[:((length-1) // 2 + 1)]
        belt[dst].extend(front_src)

        front_behind[src_mid1][0] = -1
        front_behind[src_mid2][1] = -1
    print(len(belt[dst]))

def p500(p_num):
    a,b = front_behind[p_num]
    print(a+2*b)

def p600(b_num):
    my_belt = belt[b_num]
    c = len(my_belt)
    if c ==0:
        a,b = -1,-1
    else:
        a = my_belt[-1]
        b = my_belt[0]
    print(a+2*b+3*c)

for q in range(Q):
    c = list(map(int,input().split()))
    if c[0] == 100:
        p100(c)
    elif c[0] == 200:
        src,dst = c[1],c[2]
        p200(src,dst)
    elif c[0] == 300:
        src,dst = c[1],c[2]
        p300(src,dst)
    elif c[0] == 400:
        src,dst = c[1],c[2]
        p400(src,dst)
    elif c[0] == 500:
        p_num = c[1]
        p500(p_num)
    elif c[0] == 600:
        b_num = c[1]
        p600(b_num)