

citations = [3, 0, 6, 1, 5]
def main(citations):
    answer = 0

    citations.sort(reverse=True)
    print(citations)
    for i, c in enumerate(citations):

        if c >= i + 1:
            answer += 1
        else:
            break

    return answer


print(main(citations))