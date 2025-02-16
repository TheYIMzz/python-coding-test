"""
    계단을 올라가고 있다. 이 계단의 꼭대기에 도착하려면 n개의 steps 만큼 올라가야 한다.
    한 번 올라갈 때 마다 1 step 또는 2 steps 올라갈 수 있다.
    꼭대기에 도달하는 방법의 개수는 총 몇가지 일까요?

        input: n = 2
        outputL: 2
            1. 1 step + 1 step
            2. 2 steps

        input: n = 3
        output: 3
            1. 1 step + 1 step + 1 step
            2. 2 steps + 1 step
            2. 1 step + 2 steps

    제약조건
        1 <= n <= 45


"""

memo_td = {}
def cs_td(n):
    if n == 1:
        return 1

    if n == 2:
        return 2

    return cs_td(n-1) + cs_td(n-2)

print(cs_td(5))



memo_bu = {1: 1, 2: 2}
def cs_bu(n):

    for i in range(3, n + 1):
        memo_bu[i] = memo_bu[i - 1] + memo_bu[i - 2]

    return memo_bu[n]

print(cs_bu(5))