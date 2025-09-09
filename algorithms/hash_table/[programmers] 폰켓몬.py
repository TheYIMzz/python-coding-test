
nums = [3,1,2,3]

def main():

    n = len(nums)

    kinds = len(set(nums))

    print('kinds: ', kinds)
    print('n // 2: ', n // 2, n)
    answer = min(kinds, n // 2)
    return answer


print(main())