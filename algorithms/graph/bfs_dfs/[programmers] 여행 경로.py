def main():

    tickets.sort()
    for idx, x in enumerate(tickets):
        print(idx, x)

    visited = [False] * len(tickets)
    answer = []

    def back_track(path, depth):
        if depth == len(tickets):
            answer.append(path[:])
            return

        for i in range(len(tickets)):
            if not visited[i] and tickets[i][0] == path[-1]:  # 티켓의 출발지와 경로의 마지막 위치
                visited[i] = True
                if back_track(path + [tickets[i][1]], depth + 1):
                    return True
                visited[i] = False

    start = "ICN"
    back_track([start], 0)
    return answer[0]

# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
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