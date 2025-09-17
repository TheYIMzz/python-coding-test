import io
import sys


def solution():
    K, N = map(int, sys.stdin.readline().strip().split())
    len_list = []
    for _ in range(K):
        len_list.append(int(sys.stdin.readline().strip().split()[0]))

    print(K, N, len_list)


    low = 1
    high = max(len_list)

    answer = 0

    while low <= high:
        mid = (low + high) // 2

        need = 0

        print(mid)

        for get_len in len_list:
            need += get_len // mid

        print(need)

        if need >= N:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1

    print(answer)

test_input = """4 11
802
743
457
539
"""
sys.stdin = io.StringIO(test_input)

print(solution())