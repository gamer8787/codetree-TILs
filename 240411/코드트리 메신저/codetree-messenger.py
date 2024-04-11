N,Q = map(int,input().split())
powers = [-1]
parents = [-1]
alarm = [True for _ in range(N+1)]
children = [[] for _ in range(N+1)]

def count(n,d):
    child = children[n]
    if len(child) ==0:
        return 0
    elif len(child) == 1:
        c = child[0]
        if powers[c] >=d and alarm[c] ==True:
            return 1 + count(c,d+1)
        elif powers[c] <d and alarm[c] == True:
            return count(c,d+1)
        else:
            return 0
    elif len(child) ==2:
        c1,c2 = child[0],child[1]
        ret = 0
        if powers[c1] >=d and alarm[c1] ==True:
            ret += (1 + count(c1,d+1))
        elif powers[c1] <d and alarm[c1] ==True:
            ret += count(c1,d+1)
        if powers[c2] >= d and alarm[c2] == True:
            ret += (1 + count(c2, d + 1))
        elif powers[c2] < d and alarm[c2] == True:
            ret += count(c2, d + 1)
        return ret

for _ in range(Q):
    c = list(map(int,input().split()))
    if c[0] == 100:
        parent = c[1:N+1]
        power = c[N+1:]
        parents.extend(parent)
        powers.extend(power)
        for i,parent in enumerate(parents):
            if i ==0:
                continue
            children[parent].append(i)
    elif c[0] == 200:
        n = c[1]
        alarm[n] = not alarm[n]
    elif c[0] == 300:
        n = c[1]
        p = c[2]
        powers[n] = p
    elif c[0] == 400:
        c1 = c[1]
        c2 = c[2]
        p1 = parents[c1]
        p2 = parents[c2]
        parents[c1] = p2
        parents[c2] = p1
        children[p1].remove(c1)
        children[p2].remove(c2)
        children[p1].append(c2)
        children[p2].append(c1)
    elif c[0] == 500:
        n = c[1]
        print(count(n,1))
    # print(children)
    # print(powers)