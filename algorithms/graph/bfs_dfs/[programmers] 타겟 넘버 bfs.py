from collections import deque


# bfs
def solution(numbers, target):
    queue = deque()
    queue.append((0, 0))  # (index, 현재까지 합)

    count = 0

    while queue:
        idx, total = queue.popleft()
        print(f'idx, total: {idx}, {total}')
        if idx == len(numbers):
            if total == target:
                count += 1
        else:
            queue.append((idx + 1, total + numbers[idx]))
            queue.append((idx + 1, total - numbers[idx]))

    return count

# numbers = [1, 1, 1, 1, 1]
# target = 3

numbers = [4, 1, 2, 1]
target = 4

print(solution(numbers, target))

#######################################

# dfs
def solusuion_2(numbers, target):
    count = 0


    def dfs(idx, total):
        nonlocal count

        if idx == len(numbers):
            if total == target:
                count += 1

        else:
            dfs(idx + 1, total + numbers[idx])
            dfs(idx + 1, total - numbers[idx])


    dfs(0, 0)

    return count
numbers = [4, 1, 2, 1]
target = 4
print(solusuion_2(numbers, target))