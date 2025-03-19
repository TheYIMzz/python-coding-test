"""
    문제 설명
        n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다.
        1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다.
        가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.
        노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.

    제한사항
        노드의 개수 n은 2 이상 20,000 이하입니다.
        간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
        vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다

    입력 값
    	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
"""

from collections import deque

vertext = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
def bfs(n, vertext):

    # 주어진 vertext(연결 정보)를 가지고 그래프 생성
    graph = [[] for _ in range(n + 1)]
    for a, b in vertext:
        graph[a].append(b)
        graph[b].append(a)

    print(graph) # [[], [3, 2], [3, 1, 4, 5], [6, 4, 2, 1], [3, 2], [2], [3]]

    visited = [-1] * (n + 1)
    visited[1] = 0
    print(visited)

    queue = deque([1])  # 문제에서 1번 노드에서 가장 멀리 떨어진 노드 갯수이므로 1 인큐

    while queue:
        cur_node = queue.popleft()
        print('큐에서 꺼낸 현재 노드', cur_node)
        for next_node in graph[cur_node]:

            if visited[next_node] == -1:
                visited[next_node] = visited[cur_node] + 1  # 이동거리 1증가
                queue.append(next_node)
                print('큐에 추가한 노드', next_node)


    print('visited: ', visited)
    max_move = max(visited)

    print('최대 이동한 거리:', max_move)
    farthest_node_num = visited.count(max_move)

    print('가징 멀리 떨어진 노드 개수:', farthest_node_num)
    return farthest_node_num


print(bfs(6, vertext))