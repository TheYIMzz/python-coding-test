

from collections import deque


def main():

    row = len(maps)
    col = len(maps[0])
    visited = [[-1] * col for _ in range(row)]

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in maps:
        print(i)

    visited[0][0] = 1
    queue = deque()
    queue.append((0, 0, 1))

    while queue:
        cur_r, cur_c, cur_cnt = queue.popleft()
        print('cur_r, cur_c, cur_cnt >> ',  cur_r, cur_c, cur_cnt)

        if cur_r == row-1 and cur_c == col-1:
            return cur_cnt

        for dr, dc in delta:
            next_r = cur_r + dr
            next_c = cur_c + dc

            if 0 <= next_r < row and 0 <= next_c < col:
                if visited[next_r][next_c] == -1 and maps[next_r][next_c] == 1:
                    visited[next_r][next_c] = cur_cnt + 1
                    queue.append((next_r, next_c, cur_cnt + 1))

    return -1


maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(main())


