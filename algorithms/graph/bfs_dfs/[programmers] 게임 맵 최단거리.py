from collections import deque
def main():

    for i in maps:
        print(i)

    row = len(maps)
    col = len(maps[0])

    visited = [[False] * col for _ in range(row)]
    queue = deque()

    visited[0][0] = True
    queue.append((0, 0, 1))

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        cur_r, cur_c, cur_cnt = queue.popleft()

        if cur_r == row-1 and cur_c == col-1:
            return cur_cnt

        for dr, dc in delta:
            nr = dr + cur_r
            nc = dc + cur_c

            if 0 <= nr < row and 0 <= nc < col:
                if not visited[nr][nc] and maps[nr][nc] == 1:
                    visited[nr][nc] = True
                    queue.append((nr, nc, cur_cnt + 1))

    return -1

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(main())