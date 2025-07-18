import math


def solution(numbers):
    n = len(numbers)         # 숫자 문자열 길이
    visited = [False] * n    # 방문 여부 배열
    nums = set()             # 가능한 숫자 집합

    print(visited)
    # 주어진 문자열로 숫자 집합 생성
    def backtrack(curr):

        if len(curr) == len(numbers):  # 최대 깊이에서 한번 더 불필요한 재귀 방지 (이미 visited가 모두 True일때 재귀해서 if 체크 방지)
            return

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
    def is_good(x):
        if x < 2:   # 2보다 작은 수 필터링(0, 1, 음수는 소수에서 제외)
            return False
        limit = int(math.isqrt(x))  # math.isqrt -> x의 제곱근을 내림 정수로 돌려주는 함수
        for k in range(2, limit + 1): # 2보다 작은 건 소수가 아니므로 2부터 시작, 약수 쌍의 작은 쪽의 가장 큰 수는 반드시 제곱근 이하이므로 제곱근까지 반복
            if x % k == 0: # x를 k로 나누었을 때 나머지가 0이면, k가 x의 약수이므로 소수가 아님
                return False
        return True

    count = 0
    for num in nums:
        if is_good(num):
            count += 1

    return count


numbers = "17" # "011"
print(solution(numbers))