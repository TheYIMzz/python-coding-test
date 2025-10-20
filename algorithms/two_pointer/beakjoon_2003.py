import io, sys


def solution():

    # 완전 탐색
    """
    answer = 0

    N, M = map(int, sys.stdin.readline().strip().split())
    nums = list(map(int, sys.stdin.readline().strip().split()))

    print(N, M,nums)

    for i in range(N):
        total = 0
        for j in range(i, N):

            total += nums[j]

            if total == M:
                answer += 1
            elif total > M:
                break

    return answer
    """

    # 투 포인터
    N, M = map(int, sys.stdin.readline().strip().split())
    nums = list(map(int, sys.stdin.readline().strip().split()))

    start = 0  # 왼쪽 포인터
    end = 0    # 오른쪽 포인터
    total = 0  # 현재 구간 [start ~ end-1]의 합
    count = 0  # 조건 만족하는 구간 수

    while True:
        # 1️⃣ 합이 아직 M보다 작을 때 → 오른쪽 확장
        if total < M:
            if end == N:  # 오른쪽 포인터가 끝까지 도달 → 확장 불가
                break  # 전체 while 종료
            total += nums[end]  # A[end] 값을 더해서 구간 확장
            end += 1   # 오른쪽 포인터 한 칸 이동

        # 2️⃣ 합이 딱 M일 때 → 카운트 +1, 왼쪽 줄이기
        elif total == M:
            count += 1            # 조건 만족하는 구간 발견
            total -= nums[start]  # 왼쪽 값을 빼서 다음 구간으로 이동 준비
            start += 1            # 왼쪽 포인터 한 칸 이동
        # 3️⃣ 합이 M보다 클 때 → 왼쪽 줄이기
        else:  # total > M
            total -= nums[start]   # 왼쪽 값을 빼서 합 줄이기
            start += 1          # 왼쪽 포인터 한 칸 이동

sys.stdin = io.StringIO("""4 2
1 1 1 1
""")

print(solution())
