"""
    이 로봇은 m x n grid(격자) 위에 있다. 로봇은 처음에 좌측 상단 모서리 ( grid[0][0] ) 에 위치해 있다.
    로봇은 우측 하단 모서리 ( grid[m - 1][n - 1] )로 이동하려고 한다.
    로봇은 한 번에 오른쪽이나 아래쪽으로만 움직일 수 있다.

    두 정수 m과 n이 주어졌을 때, 로봇이 우측 하단 모서리에 도달할 수 있는 가능한 unique paths의 수를 반환하세요.

    테스트 케이스는 답이 2 * 10^9 이하가 되도록 생성됩니다.


    제약조건
        1 <= m, n <= 100

    input: m = 3, n = 7
    output: 28

    input: m = 3, n = 2
    output: 3
"""

def unique_paths_bottom_up(m, n):

    dp_table = [[-1] * n for _ in range(m)]
    print('dp table 생성:', dp_table)

    for r in range(m):
        dp_table[r][0] = 1  # 모든 행의 0번째 열은 1

    for c in range(n):
        dp_table[0][c] = 1  # 모든 열의 0번째 열은 1

    print('0행과 0열 모두 1로 채운 dp_table: ', dp_table)

    for i in range(1, m):  # 0번째 행과 0번째 열은 이미 1로 초기화 해뒀으니 1부터 시작
        for j in range(1, n):
            dp_table[i][j] = dp_table[i - 1][j] + dp_table[i][j - 1]

            print(dp_table)

    return dp_table[m - 1][n - 1]


print(unique_paths_bottom_up(3, 7))



# [
#  [1,  1,  1,  1,  1,  1,  1],
#  [1,  2,  3,  4,  5,  6,  7],
#  [1,  3,  6, 10, 15, 21, 28]
# ]

