"""
    방문할 수 있는 노드중에 가장 비용이 작은 곳 방문 ( 우선순위가 높은 곳 방문 )

    1. 우선 순위 큐에 시작 노드 추가
        while priority_queue:
            2. 우선 순위가 가장 높은 노드 추출
            3. 방문 여부 확인
                4. 비용 업데이트
                5. 현재 노드와 연결된 노드 우선 순위 큐에 추가
    6. 목적지에 기록된 비용 반환
"""
import heapq

# 가중치 그래프 표현 1: [(비용, 노드)]
graph = {
    1: [(2, 2), (1, 4)],
    2: [(1, 3), (9, 5), (6, 6)],
    3: [(4, 6)],
    4: [(3, 3), (5, 7)],
    5: [(1, 8)],
    6: [(3, 5)],
    7: [(7, 6), (9, 8)],
    8: [],
}


def dijkstra(graph, start, final):
    costs = {}  # 비용 누적
    pq = []  # 우선 순위 큐 (Priority Queue)

    # 빈 리스트를 생성한 후에 heappush를 이용해 요소들을 하나씩 추가한다면, heappush가 호출될 때마다 힙 속성이 유지되므로 별도로 heapify를 호출할 필요는 없다.
    heapq.heappush(pq, (0, start))  # 시작 노드를 우선 순위 큐에 enqueue (우선순위 큐, (누적 비용, 값))

    while pq:
        cur_cost, cur_v = heapq.heappop(pq)  # 우선순위가 가장 높은 노드 추출 (처음 이후엔 넘겨받은 next_cost)

        print('cur_cost: ', cur_cost)
        print('cur_v: ', cur_v)
        print('costs: ', costs)
        print('===================== ')

        if cur_v not in costs:  # 추출한 노드(cur_v)가 costs에 기록되어 있는지 확인 (이미 기록된 노드의 비용보다 더 큰 비용으로 노드에 도착하는 경우 그 노드는 무시한다. (ex 나중에 비용 4로 노드 3이 나오면, 이미 더 작은 3의 비용으로 기록되어 있기 때문에 무시)
            costs[cur_v] = cur_cost  # 아직 방문하지 않은 노드 cur_v에 대해, 시작 노드로부터 도달한 누적 비용 cur_cost를 기록
            for cost, next_v in graph[cur_v]:  # 현재 노드와 연결된 노드 우선순위 큐에 추가
                next_cost = cur_cost + cost  # 비용 계산 후
                heapq.heappush(pq, (next_cost, next_v))  # 우선순위 큐에 추가

    return costs[final]

print(dijkstra(graph, 1, 8))