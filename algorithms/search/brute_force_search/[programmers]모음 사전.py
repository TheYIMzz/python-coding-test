def main():
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    def back_track(curr):

        if len(curr) > 5:
            return
        print(curr)
        if curr:
            result.append(''.join(curr))

        for v in vowels:
            curr.append(v)
            back_track(curr)
            curr.pop()

    back_track([])

    return result.index(word) + 1

word = "AAAAE"
print(main())