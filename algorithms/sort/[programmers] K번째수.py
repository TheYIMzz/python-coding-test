array =  [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def main():
    answer = []


    for command in commands:
        i, j, k = command
        new_array = []

        for t in range(i-1, j):
            new_array.append(array[t])

        new_array.sort()
        answer.append(new_array[k-1])


    return answer



print(main())