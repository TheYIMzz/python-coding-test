def main():


    result = []
    def back_track(start, curr):

        print(curr)

        if len(curr) == 5:
            if curr[0] == 'U' and curr[:-1] == 'U':
                return
            curr.clear()

        result.append(''.join(curr))

        for i in range(start, 5):
            curr.append(vowels[i])
            back_track(i + 1, curr)
            curr.pop()

    back_track(0, [])
    print(result)


word = "AAAAE"
vowels = ['A', 'E', 'I', 'O', 'U']
print(main())