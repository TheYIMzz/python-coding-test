"""
    계단을 올라가고 있다. 한 번 올라갈 대마다 1 setp 또는 2 step 올라갈 수 있따.
    문제에서 정수형 배열 cost가 주어지는데, cost[i]는 i번째 계단을 밟았을 때 지불해야 하는 비용이다.

    처음 시작은 index 0 또는 index 1 중 한 곳에서 시작할 수 있다.

    이 계단의 꼭대기에 도착하기 위해 지불해야하는 비용의 최소 값을 반환하라.


    제약조건
        2 <= cost.length <= 1000
        0 <= cost[i] <= 999


    input: cost = [10, 15, 20]
    output: 15

    input: cost = [1, 100, 1, 1, 1, 1, 100, 1, 1, 100,1]
    output: 6

"""

# bottom up 방식
cost = [10, 15, 20, 17, 1]

def dp(n):

    memo = [0] * (n + 1)
    print('memo 생성: ', memo)

    memo[0] = 0
    memo[1] = 0

    for i in range(2, n + 1):
        memo[i] = min(memo[i - 1] + cost[i - 1], memo[i - 2] + cost[i - 2])
        print(f'{i} {memo}')
    return memo[n]

print(dp(5))


"""
    memo[0] = 0
    memo[1] = 0
    memo[2] = min(memo[1] + cost[1], memo[0] + cost[0])
        => memo[2] = min(15, 10) = 10
    
    memo[3] = min(memo[2] + cost[2], memo[1] + cost[1])
        => memo[3] = min(30, 15) = 15

    memo[4] = min(memo[3] + cost[3], memo[2] + cost[2])
        => memo[4] = min(32, 30) = 30
        
    memo[5] = min(memo[4] + cost[4], memo[3] + cost[3])
        => memo[5] = min(31, 32) = 31

"""