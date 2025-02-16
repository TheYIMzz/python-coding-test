"""
 피보나치 수열을 구할 때 메모이제이션(memoization)을 사용하여 중복 계산을 피하기
"""


# top_down 방식
memo_td = {}  # 계산한 피보나치 값을 저장(메모이제이션)하여 같은 계산을 다시 하지 않도록 하기 위한 변수
def fibonacci_top_down(n):

    if n == 1 or n == 2:
        return 1

    if n not in memo_td:
        memo_td[n] = fibonacci_top_down(n - 1) + fibonacci_top_down(n - 2)
        # print('memo: ', memo_td)
    return memo_td[n]


print(fibonacci_top_down(150))



## bottom_up 방식
memo_bu = {1: 1, 2 : 1}
def fibonacci_bottom_up(n):

    for i in range(3, n + 1):  # 1, 2는 base case로 3번째(정수 3) ~ n +1 번째까지 반복 (끝 수는 미포함으로 +1)
        memo_bu[i] = memo_bu[i - 1] + memo_bu[i - 2]

    return memo_bu[n]


print(fibonacci_bottom_up(150))
