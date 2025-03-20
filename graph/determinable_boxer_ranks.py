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

from collections import deque

results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
def solution(n, results):

    # 선수별로 경기 결과 저장할 리스트
    win = [[] for _ in range(n + 1)]
    loss = [[] for _ in range(n + 1)]
    print('win: ', win)
    print('loss: ', loss)

    # 경기 결과를 그래프로 저장 (1번부터 n번 선수 사용)
    for a, b in results:
        win[a].append(b)  # a가 b에게 승리
        loss[b].append(a) # b가 a에게 패배
        print(f'{a} -> {b}: 승: {win}')
        print(f'{b} -> {a}: 패: {loss}')

    print('===== 경기 결과 저장 =====')
    print('win: ', win)
    print('loss: ', loss)

    def bfs(start, graph):
        visited = [False] * (n + 1)
        visited[start] = True
        queue = deque()
        queue.append(start)

        count = 0

        while queue:
            cur_node = queue.popleft()
            print('현재 선수: ', cur_node)
            for next_node in graph[cur_node]:

                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)
                    count += 1
                    print('다음 선수: ', cur_node)
        return count

    answer = 0

    for i in range(1, n + 1):
        win_count = bfs(i, win)
        loss_count = bfs(i, loss)

        # 모둔 선수와의 관계가 결정되었다면 ( 자기 자신 제외로 -1)
        if win_count + loss_count == n - 1:
            answer += 1

    return answer

print(solution(5, results))