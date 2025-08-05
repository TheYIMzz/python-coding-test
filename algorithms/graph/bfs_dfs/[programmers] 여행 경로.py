def main():
    tickets.sort()

    for i, idx in enumerate(tickets):
        print(i, idx)

    visited = [False] * len(tickets)
    answer = []

    def back_track(curr, depth):

        if depth == len(tickets):
            answer.append(curr[:])
            return True

        for i in range(len(tickets)):
            if not visited[i] and tickets[i][0] == curr[-1]:
                visited[i] = True
                curr.append(tickets[i][1])
                # print(curr)
                if back_track(curr, depth + 1):
                    return True  # 정답 경로를 찾은 경우 상위 호출도 종료하기 위해 True 반환
                visited[i] = False
                curr.pop()

    back_track(['ICN'], 0)
    return answer[0]

    # tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]


tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
print(main())

"""
ICN -> JFK -> HND -> IAD
ICN -> ATL -> ICN -> SFO -> ATL -> SFO

정렬 전
0 ['ICN', 'SFO']
1 ['ICN', 'ATL']
2 ['SFO', 'ATL']
3 ['ATL', 'ICN']
4 ['ATL', 'SFO']

정렬 후
0 ['ATL', 'ICN']
1 ['ATL', 'SFO']
2 ['ICN', 'ATL']
3 ['ICN', 'SFO']
4 ['SFO', 'ATL']

"""