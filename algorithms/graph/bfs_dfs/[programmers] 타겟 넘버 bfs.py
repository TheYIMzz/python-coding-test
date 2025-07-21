from collections import deque


def main():


    queue = deque()
    queue.append(0)

    for num in numbers:
        print('====================현재 num: ', num)
        for _ in range(len(queue)):
            print('현재 큐 길이: ', len(queue))

            curr = queue.popleft()
            print(f'curr값: {curr}')
            queue.append(curr + num)
            queue.append(curr - num)

    return queue.count(target)


# numbers = [1, 1, 1, 1, 1]
# target = 3

numbers = [4, 1, 2, 1]
target = 4

print(main())