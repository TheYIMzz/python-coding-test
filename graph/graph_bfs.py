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
                visited.append(v) # 방문 처리
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

