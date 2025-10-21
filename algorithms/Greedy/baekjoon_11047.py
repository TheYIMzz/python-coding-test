import io, sys


def solution():

    N, K = map(int, sys.stdin.readline().strip().split())

    coins = []
    for _ in range(N):
        coins.append(int(sys.stdin.readline().strip().split()[0]))

    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if coin <= K:
            print(K // coin, coin)
            count += K // coin  # K를 K 보다 작은 동전으로 나눠서 몫을 추출하여 몇개 필요한지 체크
            K = K % coin # 몫을 뺀 나머지를 계산해서 K를 갱신

    return count

sys.stdin = io.StringIO("""10 4200
1
5
10
50
100
500
1000
5000
10000
50000
""")

print(solution())
