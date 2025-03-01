"""
    주어진 네트워크에는 n개의 노드가 있으며, 이는 1부터 n까지 레이블이 붙어 있습니다. 또한 times[i] = (ui, vi, wi) 리스트가 주어집니다.
    이 때, ui 노드에서 신호를 보내서 vi 노드에 도달하는데 걸리는 시간을 wi라고 합니다.

    k 노드에서 신호를 보낼 때, 모든 노드에 신호가 도달하기 위한 최소 비용을 반환하시오. 하나의 노드라도 도달하지 못한다면 -1을 반환하시오.
    (한 노드에서 연결된 여러 개의 edge에 신호를 동시에 전달할 수 있습니다.)


    제약 조건
        1 <= k <= n <= 100
        1 <= times.length <= 6000  (간선(E)의 개수)
        times[i].length == 3
        1 <= ui, vi <= n
        ui != vi
        1 <= wi <= 100
        모든(ui, vi) 쌍은 unuque 합니다.

    input: times = [[2, 1, 2], [2, 3, 5], [2, 4, 1], [4, 3, 3]], n = 4, k = 2
    output: 4
    
    
    1. 그래프 구현
        O(times.length)
    
    2. 다익스트라 알고리즘
        O(E log E) => 우선 순위 큐에 간선(E)의 개수만큼 push와 pop을 할 때 logE의 시간 복잡도를 간선(E)의 개수만큼 반복
    
    3. 방문 못한 노드 찾기
        O(n)
    
    4. 최소 값중에서 최대 값 구하기
        O(N)
"""
import heapq
from collections import defaultdict



times = [
    [2, 1, 2],   # 2번 노드에서 1번 노드로 가는 경로의 비용이 2
    [2, 3, 5],   # 2번 노드에서 3번 노드로 가는 경로의 비용이 5
    [2, 4, 1],   # 2번 노드에서 4번 노드로 가는 경로의 비용이 1
    [4, 3, 3],   # 4번 노드에서 3번 노드로 가는 경로의 비용이 3
]



def network_delay_time(times, n, k):
    graph = defaultdict(list)  # 기본 값이 빈 리스트인 defaultdict 생성 (딕셔너리에 해당 키가 없으면 빈 리스트 생성 후 키값 할당)

    for time in times:  # 주어진 2차원 배열의 times를 graph로 변환
        graph[time[0]].append((time[2], time[1]))   # time[0] => u,  time[2] => w,  time[1] => v

    costs = {}
    pq = []

    heapq.heappush(pq, (0, k))

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if cur_node not in costs:  # 방문 여부 확인
            costs[cur_node] = cur_cost  # 비용 업데이트

            for cost, next_node in graph[cur_node]:
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_cost, next_node))  # 현재 노드와 인접한 노드 푸시

    # 모든 노드 방문했는지 체크
    for node in range(1, n + 1): # 제약 조건에 따라 노드 번호 1부터 n + 1까지
        if node not in costs:
            return -1

    return max(costs.values()) # 각 노드까지 도달하는 데 드는 최소 비용 중 가장 큰 값이 모든 노드가 신호를 받는 데 필요한 전체 시간


print(network_delay_time(times, 4, 2))