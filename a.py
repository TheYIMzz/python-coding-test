from collections import deque


def solution():

    answer = 0

    row = len(maps)
    col = len(maps[0])

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(r, c):
        visited = [[False] * col for _ in range(row)]
        visited[r][c] = True
        queue = deque()
        queue.append((r, c, 1))

        while queue:
            cur_r, cur_c, depth = queue.popleft()

            if cur_r == row - 1 and cur_c == col - 1:
                return depth

            for dr, dc in delta:
                nr = dr + cur_r
                nc = dc + cur_c

                if 0 <= nr < row and 0 <= nc < col:
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append((nr, nc, depth + 1))


    answer += bfs(0, 0)

    return answer

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution())
