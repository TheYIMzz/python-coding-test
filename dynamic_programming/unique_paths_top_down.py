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

# grid의 시작 위치부터 하는 방식 (완전 탐색)
def unique_path_brute_force(r, c):

    if r == 2 and c == 6:  # Base Case
        return 1

    unuque_paths = 0

    if r + 1 < 3:  # 행 0, 1, 2
        unuque_paths += unique_path_brute_force(r + 1, c)
    if c + 1 < 7:  # 열 0, 1, 2, 3, 4, 5, 6
        unuque_paths += unique_path_brute_force(r, c + 1)

    return unuque_paths

print('시작 위치부터 완전 탐색: ', unique_path_brute_force(0, 0))


# grid의 끝 위치부터 하는 방식 (완전 탐색)
def unique_path_brute_force(r, c):

    if r == 0 and c == 0:  # Base Case
        return 1

    unuque_paths = 0

    if r - 1 >= 0:  # 행 0, 1, 2
        unuque_paths += unique_path_brute_force(r - 1, c)
    if c - 1 >= 0:  # 열 0, 1, 2, 3, 4, 5, 6
        unuque_paths += unique_path_brute_force(r, c - 1)

    return unuque_paths

print('끝 위치부터 완전 탐색: ', unique_path_brute_force(2, 6))


############################################################################################
############################################################################################

# grid의 끝 위치부터 하는 방식 (메모이제이션 사용)
memo = {}
def unique_path_memo(r, c):

    if r == 0 and c == 0:  # Base Case
        memo[(r, c)] = 1
        return memo[(r, c)]  # (r, c)라는 key에 저장된 값 반환 => 1

    unuque_paths = 0

    # r -1, c -1 체크하여 0이 들어왔을 땐 불필요한 재귀 호출 방지 (0, 1 이렇게 들어오는 경우 Base Case가 아니기에 재귀 호출됨)
    if r - 1 >= 0 :  # 행 0, 1, 2
        unuque_paths += unique_path_memo(r - 1, c)
    if c - 1 >= 0:  # 열 0, 1, 2, 3, 4, 5, 6
        unuque_paths += unique_path_memo(r, c - 1)

    memo[(r, c)] = unuque_paths
    return memo[(r, c)]

print('메모이제이션 결과: ', unique_path_memo(2, 6))

############################################################################################
############################################################################################

# grid의 끝 위치부터 하는 방식 (list로 만든 dp table 사용)
def unique_path_dp_table(m, n):
    dp_table = [[-1] * n for _ in range(m)]

    def dfs(r, c):

        if r == 0 and c == 0:  # Base Case
            dp_table[r][c] = 1
            return dp_table[r][c]

        unuque_paths = 0

        if dp_table[r][c] == -1:
            # r -1, c -1 체크하여 0이 들어왔을 땐 불필요한 재귀 호출 방지 (0, 1 이렇게 들어오는 경우 Base Case가 아니기에 재귀 호출됨)
            if r - 1 >= 0 :  # 행 0, 1, 2
                unuque_paths += dfs(r - 1, c)
            if c - 1 >= 0:  # 열 0, 1, 2, 3, 4, 5, 6
                unuque_paths += dfs(r, c - 1)

            dp_table[r][c] = unuque_paths
        return dp_table[r][c]
    return dfs(m - 1, n - 1)

print('list dp table 결과: ', unique_path_dp_table(3, 7))
