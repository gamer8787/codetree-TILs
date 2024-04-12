import heapq
from collections import defaultdict

Q = int(input())
N = 0

waiting_set = set() #url 저장
waiting_queue = defaultdict(list)
judging_domain_set = set()
judging_number = []
judging_domain = defaultdict(int)
domain_start = defaultdict(int)
domain_gap = defaultdict(int)

P = False


def print_wating():
    if P:
        print(waiting_set)
        # print("waiting queue")
        # print(waiting_queue)

def print_judging():
    if P:
        print(judging_domain_set)
        # print("judging_number")
        # print(judging_number)
        # print("judging_domain")
        # print(judging_domain)

def url_to(url):
    domain, ID = url.split("/")
    return domain, ID

def p100(u0):
    domain,ID = url_to(u0)
    waiting_set.add(u0)
    heapq.heappush(waiting_queue[domain],[1,0,ID])

def p200(t,p,u):
    domain, ID = url_to(u)
    if u in waiting_set:
        return
    waiting_set.add(u)
    heapq.heappush(waiting_queue[domain],[p,t,ID])

def p300(t): #gap 계산해야됨
    if not judging_number:
        return

    avail_domain = []
    for domain in waiting_queue:
        if domain in judging_domain_set:
            continue
        waiting_domain = waiting_queue[domain]
        if not waiting_domain:
            continue
        p,domain_t,ID = waiting_domain[0]
        start = domain_start[domain]
        gap = domain_gap[domain]
        if gap !=0:
            if t < start + 3*gap:
                continue
        avail_domain.append([p,domain_t,domain,ID])
    if not avail_domain:
        return
    avail_domain.sort()
    judging_n = heapq.heappop(judging_number)
    p,domain_t,domain,ID = avail_domain[0]
    waiting_domain = waiting_queue[domain]
    heapq.heappop(waiting_domain)
    url = domain+"/"+ID
    waiting_set.remove(url)
    judging_domain_set.add(domain)
    judging_domain[judging_n] = domain
    domain_start[domain] = t


def p400(t,J_id):
    if judging_domain[J_id] == 0:
        return
    domain = judging_domain[J_id]
    domain_gap[domain] = t - domain_start[domain]
    judging_domain_set.remove(domain)
    heapq.heappush(judging_number,J_id)
    judging_domain[J_id] = 0

def p500(t):
    print(len(waiting_set))

for r in range(Q):
    if P:
        print(r,"라운드")
    print_wating()
    print_judging()

    c = input().split()
    if c[0] == "100":
        N = int(c[1])
        judging_number = [i for i in range(1, N + 1)]
        u0 = c[2]
        p100(u0)
    elif c[0] =="200":
        t,p,u = int(c[1]) ,int(c[2]), c[3]
        p200(t,p,u)
    elif c[0] == "300":
        t = int(c[1])
        p300(t)
    elif c[0] == "400":
        t ,J_id = int(c[1]) ,int(c[2])
        p400(t,J_id)
    elif c[0] =="500":
        t = int(c[1])
        p500(t)