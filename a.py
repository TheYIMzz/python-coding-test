


def solution():

    tickets.sort()
    visited = [False] * len(tickets)
    answer = []

    for idx, t in enumerate(tickets):
        print(idx, t)

    def back_track(curr):
        # print(curr, len(tickets), len(curr))
        if len(tickets) == len(curr):
            answer.append(curr[:])
            return

        for i in range(len(tickets)):
            if not visited[i]:

                if tickets[i][0] == curr[0]:
                    print('tickets[i][0] == curr: ', tickets[i][0], curr[0], i)
                    print('tickets[i][1]: ', tickets[i][1])
                    visited[i] = True
                    curr.append(tickets[i][1])
                    back_track(curr)
                    visited[i] = False
                    curr.pop()

    back_track([start])

    return answer

start = "ICN"
tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution())