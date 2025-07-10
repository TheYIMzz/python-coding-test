
"""
최소 피로도 -> 최소한 가지고 있어야함
소모 피로도 -> 던전 탐험 후 소모되는 피로도

던전은 하루에 1회만 탐색 가능 -> visited
최대한 많이 탐험
k = 현재 피로도
dungeons = [최소필요피로도, 소모피로도]
"""


def solution(k, dungeons):
    size = len(dungeons)
    visited = [False] * size

    def is_good(idx, cur_k):
        if cur_k >= dungeons[idx][0] and cur_k >= dungeons[idx][1]:
            return True
        else:
            return False

    max_count = 0

    def back_track(cur_k, count):
        nonlocal max_count
        max_count = max(max_count, count)

        for i in range(size):
            if not visited[i]:
                visited[i] = True
                if is_good(i, cur_k):
                    new_k = cur_k - dungeons[i][1]
                    back_track(new_k, count + 1)
                visited[i] = False

    back_track(k, 0)
    print(max_count)

    return max_count

k = 80
dungeons = [[80,20],[50,40],[30,10]]
solution(k, dungeons)

