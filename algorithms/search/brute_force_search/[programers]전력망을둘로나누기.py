def main(n, wires):

    # 1) 인접 리스트 구성
    graph = [[] for _ in range(n + 1)]
    for u, v in wires:
        graph[u].append(v)
        graph[v].append(u)

    # 2) 방문 처리 및 서브트리 크기 저장용 배열
    visited = [False] * (n + 1)
    subtree_size = [0] * (n + 1)

    for i in graph:
        print(i)

    # 3) DFS로 subtree_size 계산
    def dfs(u):
        visited[u] = True  # 1) 방문 처리
        size = 1  # 2) 자기 자신 카운트
        for next_v in graph[u]:  # 3) 이웃 순회
            if not visited[next_v]:  # 4) 아직 방문하지 않은 자식만
                size += dfs(next_v)  # 서브트리 크기 누적
        subtree_size[u] = size  # 5) 결과 저장
        return size

    dfs(1)  # 1번 노드를 루트로 삼고 탐색, 루트는 부모 노드가 없으므로 가상의 번호 0
    print(subtree_size)

    # 4) 최소 차이 계산
    answer = n                    # n개 노드 중 최대 차이는 n이므로, 초기값을 n으로 설정
    for node in range(2, n + 1):  # node=2부터 n까지: 1번(루트) 노드는 잘라낼 수 없으므로 제외
        k = subtree_size[node]    # node를 자른 쪽 서브트리의 크기
        diff = abs((n - k) - k)   # 전체 노드 n에서 서브트리 크기 k를 빼서 반대쪽 크기 n-k를 구한 뒤 거기서 다시 k를 빼 두 서브트리 크기 차이를 계산
        if diff < answer:         # 이전까지 구한 최소 차이보다 작으면
            answer = diff         # 갱신

    return answer      # answer에 모든 간선 제거 시 생기는 두 트리 크기 차이의 최소 값이 저장됨


n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(main(n, wires))


"""
    1 -> [2]
    2 -> [1, 3]
    3 -> [2, 4]
    4 -> [3]
"""