"""
    0번방부터 n-1번방까지 총 n개의 방이 있다. 0번 방을 제외한 모든 방은 잠겨있다. 우리의 목표는 모든 방에 방문하는 것이다.
    하지만 잠겨있는 방은 key가 없으면 방문할 수 없다. 각 방에 방문할 때, 별개의 열쇠 뭉치(a set of distict keys)를 찾을 수 있따.
    각각의 열쇠에는 number가 쓰여져 있고, 번호에 해당하는 방을 잠금 해제할 수 있다.
    열쇠 뭉치는 모두 가져갈 수 있고, 언제든 문을 열기 위해 사용할 수 있다.

    문제에서 rooms 배열이 주어지고, rooms[i]는 해당 방에서 얻을 수 있는 열쇠뭉치 목록을 표현한다.
    모든 방을 방문할 수 있다면 True, 그렇지 않다면 False를 반환

    제약조건
        n == rooms.length                  ->  방의 개수를 의미
        2 <= n <= 1000                     -> 방의 개수가 최소 2개 이상, 최대 1000개 이하
        0 <= rooms[i].length <= 1000       -> 각 방(rooms[i])에 들어있는 키의 개수가 0개 이상 1000개 이하
        1 <= sum(rooms[i].length) <= 3000  -> 모든 방에 있는 키의 총 개수가 최소 1개 이상, 최대 3000개 이하
        0 <= rooms[i][j] < n               -> 키가 항상 존재하는 방(rooms 배열 내의 방)만을 가리zla
"""

# set 사용
def can_visit_all_rooms_set(rooms):

    visited = set()

    def dfs(cur_v):
        visited.add(cur_v)   # -> set 사용

        for next_v in rooms[cur_v]:
            if next_v not in visited:     # -> set 사용
                dfs(next_v)


    dfs(0)  # 시작 값 0
    if len(visited) == len(rooms):
        print('(set) 방문한 노드: ', visited)
        return True
    else:
        print('(set) 방문한 노드: ', visited)
        return False


# list 사용
def can_visit_all_rooms_list(rooms):

    visited = [False] * len(rooms)


    def dfs(cur_v):
        visited[cur_v] = True  # -> list 사용

        for next_v in rooms[cur_v]:
            if not visited[next_v]:  # -> list 사용
                dfs(next_v)

    dfs(0)
    print('(list) 방문한 노드: ', visited)
    return all(visited)  # 모든 요소가 True일 때만 True 반환


rooms_1 = [[1], [2], [3], []]
rooms_2 = [[1, 3], [2, 4], [0], [4], [], [3, 4]]



print(can_visit_all_rooms_set(rooms_1))
print(can_visit_all_rooms_set(rooms_2))

print(can_visit_all_rooms_list(rooms_1))
print(can_visit_all_rooms_list(rooms_2))



