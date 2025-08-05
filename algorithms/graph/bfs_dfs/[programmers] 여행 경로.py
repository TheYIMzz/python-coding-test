def main():
    tickets.sort()

    for i, idx in enumerate(tickets):
        print(i, idx)

    visited = [False] * len(tickets)
    answer = []

    def back_track(curr, depth):

        if depth == len(tickets):
            answer.append(curr[:])
            return

        for i in range(len(tickets)):
            if not visited[i] and tickets[i][0] == curr[-1]:
                visited[i] = True
                curr.append(tickets[i][1])
                back_track(curr, depth + 1)
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