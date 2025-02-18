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


# top down 방식

memo = {}
cost = [10, 15, 20, 17, 1]

def dp(n):

    if n == 0 or n == 1:
        return 0

    if n not in memo:
        memo[n] = min(dp(n - 1) + cost[n - 1], dp(n - 2) + cost[n - 2])  # 현재 계단 cost[n-1] 더하기

    return memo[n]


print(dp(5))


"""
    dp(0) = 0
    dp(1) = 0
        
    dp(2) = min( dp(1) + cost[1],  dp(0) + cost[0] )
          = min( 0 + 15,              0 + 10 ) 
          = 10
     memo = {2: 10}
    
    dp(3) = min( dp(2) + cost[2],  dp(1) + cost[1] )
          = min( 10 + 20,             0 + 15 )
          = min( 30,                  15 )
          = 15
     memo = {2: 10, 3: 15}
        
    dp(4) = min( dp(3) + cost[3],  dp(2) + cost[2] )
          = min( 15 + 17,             10 + 20 )
          = min( 32,                  30 )
          = 30
     memo = {2: 10, 3: 15, 4: 30}
    
    dp(5) = min( dp(4) + cost[4],  dp(3) + cost[3] )
          = min( 30 + 1,              15 + 17 )
          = min( 31,                  32 )
          = 31
     memo = {2: 10, 3: 15, 4: 30, 5: 31}

"""
