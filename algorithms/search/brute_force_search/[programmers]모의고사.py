



# answers = [1, 2, 3, 4, 5]
answers = [1, 3, 2, 4, 2]


def main(answers):

    pattens = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    count = [0, 0, 0]
    result = []
    for idx, ans in enumerate(answers):

        for i in range(3):

            if ans == pattens[i][idx % len(pattens[i])]:
               count[i] += 1


    for i, c in enumerate(count):
        if max(count) == c:
            result.append(i + 1)

    return result



print(main(answers))