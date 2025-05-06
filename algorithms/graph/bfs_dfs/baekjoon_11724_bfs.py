"""
    방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

    입력
    첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.
    (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.
    (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

    출력
    첫째 줄에 연결 요소의 개수를 출력한다.

    입력 예제 1
    6 5
    1 2
    2 5
    5 1
    3 4
    4 6

    입력 예제 2
    6 8
    1 2
    2 5
    5 1
    3 4
    4 6
    5 4
    2 4
    2 3
"""
import io
import sys
from collections import deque


def main():
    input = sys.stdin.readline

    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)

    def bfs(start):
        visited[start] = True
        queue = deque([start])

        while queue:
            cur_node = queue.popleft()

            for next_node in graph[cur_node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)

    count = 0

    for i in range(1, n + 1):
        if not visited[i]:
            bfs(i)
            count += 1  # 새로운 연결 요소 발견

    print(count)

test_input = """6 5
1 2
2 5
5 1
3 4
4 6
"""

test_input_2 = """6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
"""

sys.stdin = io.StringIO(test_input)
main()

sys.stdin = io.StringIO(test_input_2)
main()