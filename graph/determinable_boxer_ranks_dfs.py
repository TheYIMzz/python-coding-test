"""
    문제 설명
        n명의 권투선수가 권투 대회에 참여했고 각각 1번부터 n번까지 번호를 받았습니다.
        권투 경기는 1대1 방식으로 진행이 되고, 만약 A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이깁니다.
        심판은 주어진 경기 결과를 가지고 선수들의 순위를 매기려 합니다. 하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없습니다.
        선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때 정확하게 순위를 매길 수 있는 선수의 수를 return 하도록 solution 함수를 작성해주세요.

    제한사항
        선수의 수는 1명 이상 100명 이하입니다.
        경기 결과는 1개 이상 4,500개 이하입니다.
        results 배열 각 행 [A, B]는 A 선수가 B 선수를 이겼다는 의미입니다.
        모든 경기 결과에는 모순이 없습니다.
"""

results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

# dfs 풀이
def solution(n, results):

    win_graph = [[] for _ in range(n + 1)]
    loss_graph = [[] for _ in range(n + 1)]

    for a, b in results:
        win_graph[a].append(b)
        loss_graph[b].append(a)

    def dfs(i, graph, visited):
        visited.add(i) # 시작노드 방문처리

        for next_node in graph[i]:
            if next_node not in visited:
                visited.add(next_node)
                dfs(next_node, graph, visited)
        return visited

    answer = 0
    for i in range(1, n + 1):
        win_result = dfs(i, win_graph, set())
        loss_result = dfs(i, loss_graph, set())

        # DFS 함수 내에서 시작 노드를 set에 추가하기 때문에 각 DFS 결과(승리, 패배) 모두에 자기 자신이 포함
        # 이 두 set을 따로 계산하면 자기 자신이 각각 한 번씩 포함되어 총 2번 세어지게 되므로 결과에서 1개를 빼준다. (결과에 자기자신이 포함되어 있으므로 n에서는 빼지 않음)
        if len(win_result) + len(loss_result) - 1 == n:  # dfs에서 시작노드를 방문처리했기 win,loss에서 중복으로 추가된(+2) 자기자신 제외 -1 ( 여기선 n에 자기자신 포함되어있음 )
            answer += 1

    return answer

print(solution(5, results))