"""
 피보나치 수열을 구할 때 메모이제이션(memoization)을 사용하여 중복 계산을 피하기
"""

memo = {}  # 계산한 피보나치 값을 저장(메모이제이션)하여 같은 계산을 다시 하지 않도록 하기 위한 변수


def fibonacci(n):

    if n == 1 or n == 2:
        return 1

    if n not in memo:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
        print('memo: ', memo)
    return memo[n]


print(fibonacci(150))