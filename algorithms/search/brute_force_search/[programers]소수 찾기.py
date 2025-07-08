import math


def solution(numbers):
    n = len(numbers)         # 숫자 문자열 길이
    visited = [False] * n    # 방문 여부 배열
    nums = set()             # 가능한 숫자 집합

    print(visited)
    # 주어진 문자열로 숫자 집합 생성
    def backtrack(curr):
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                new_curr = curr + numbers[i]
                nums.add(int(new_curr))
                backtrack(new_curr)
                visited[i] = False

    backtrack("") # 빈 문자열 파라미터
    print(nums)

    # 소수인지 체크
    def is_prime(x):
        if x < 2:   # 2보다 작은 수 필터링(0, 1, 음수는 소수에서 제외)
            return False
        limit = int(math.isqrt(x))  # math.isqrt -> x의 제곱근을 내림 정수로 돌려주는 함수
        for k in range(2, limit + 1):
            if x % k == 0:
                return False
        return True

    count = 0
    for num in nums:
        if is_prime(num):
            count += 1

    return count


numbers = "17"
print(solution(numbers))