def main():


    result = []
    def back_track(curr):

        if len(curr) > 5:
            return

        if curr:
            result.append(''.join(curr))

        for v in vowels:
            curr.append(v)
            back_track(curr)
            curr.pop()

    back_track([])
    print(result)
    return result.index(word) + 1

word = "AAAAE"
vowels = ['A', 'E', 'I', 'O', 'U']
print(main())