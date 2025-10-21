import io, sys


def solution():


    S = int(sys.stdin.readline().strip().split()[0])

    total = 0
    n = 0
    while total + (n + 1) <= S: #  (n + 1) 로 체크해서 total + n == S 일때 한번 더 누적 방지
        n += 1
        total += n

    return n

sys.stdin = io.StringIO("""200
""")

print(solution())
