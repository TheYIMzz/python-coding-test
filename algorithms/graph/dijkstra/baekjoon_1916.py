import sys, io, heapq

def dijkstra():


    n = int(sys.stdin.readline().strip())  # 도시 개수
    m = int(sys.stdin.readline().strip())  # 버스 개수

    # 출발도시번호, 도착도시번호, 버스비용

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v, cost = map(int, sys.stdin.readline().strip().split())
        graph[u].append((cost, v))

    start, final = map(int, sys.stdin.readline().strip().split())

    pq = []
    costs = {}
    heapq.heappush(pq, (0, start))
    while pq:
        cur_cost, cur_v = heapq.heappop(pq)

        if cur_v not in costs:
            costs[cur_v] = cur_cost

            for cost, next_v in graph[cur_v]:
                next_cost = cost + cur_cost
                heapq.heappush(pq, (next_cost, next_v))

    return costs[final]



sys.stdin = io.StringIO("""5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
""")


print(dijkstra())