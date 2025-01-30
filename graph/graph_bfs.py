from collections import deque


def bfs(graph, start_v):

    if graph is None:
        return

    visited = [start_v]  # 방문한 노드 리스트 (시작 노드 방문)
    q = deque([start_v])  # 탐색할 노드 q에 추가 ("ABC" 같은 문자열이면 큐에는 'A', 'B', 'C'가 각각 들어가게 되므로 list로 감싸준다.)

    while q:
        cur_v = q.popleft()  # 탐색을 위해 큐에서 꺼냄

        for v in graph[cur_v]:  # 현재 노드의 인접 노드들을 확인
            if v not in visited:  # 아직 방문하지 않았다면
                visited.append(v) # 방문 처리 (미리 방문처리 하는 이유는 다른 노드가 이 노드로 가는 경로를 갖고 있다면 “아직 visited에 없네? 그럼 큐에 넣어야지” 하면서 동일 노드를 여러 번 큐에 넣는 상황 발생할 수 있음)
                q.append(v)  # 방문한 노드 탐색 예정 q에 추가

    return visited

graph = {
    'AB':['B', 'D', 'E'],
    'B':['AB', 'C', 'D'],
    'C':['B'],
    'D':['AB', 'B'],
    'E':['AB']
}


print(bfs(graph, 'AB'))

