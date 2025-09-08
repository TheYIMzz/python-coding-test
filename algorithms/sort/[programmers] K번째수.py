array =  [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def main():

    answer = []

    for command in commands:
        i, j, k = command

        sliced = sorted(array[i-1:j])
        answer.append(sliced[k - 1])

    return answer



print(main())