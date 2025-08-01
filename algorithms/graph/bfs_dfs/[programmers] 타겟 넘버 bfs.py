from collections import deque

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