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
    heapq.heappush(pq, (0, start))  # 시작 노드를 우선 순위 큐에 enqueue

    while pq:
        cur_cost, cur_v = heapq.heappop(pq)  # 우선 순우가 가장 높은 노드 추출 (처음 이후엔 넘겨받은 next_cost)

        if cur_v not in costs:  # 추출한 노드 방문 여부 확인
            costs[cur_v] = cur_cost  # 방문하지 않았다면 현재 비용 업데이트
            for cost, next_v in graph[cur_v]:  # 현재 노드와 연결된 노드 우선 순위 큐에 추가
                next_cost = cur_cost + cost  # 비용 계산 후
                heapq.heappush(pq, (next_cost, next_v))  # 우선 순위 큐에 추가

    return costs[final]