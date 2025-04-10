
"""
    nums = [1, 2, 3, 4]로 만들 수 있는 부분집합을 모두 반환하시오.
"""
# 조합
def subset(nums):
    result = []

    def backtrack(start, curr):
        if len(curr) == k:  # base case
            print('base case 진입 후 result에 추가한 값:', curr)
            print('================')
            result.append(curr[:])
            return

        for i in range(start, len(nums)):
            print(f'현재 i: {i}')
            curr.append(nums[i])
            print('curr에 추가된 num: ', curr)
            backtrack(i + 1, curr)
            curr.pop()
            print('backtrack 후 pop: ', curr)

    for k in range(len(nums) + 1):  # 집합을 0(공집합) 부터 전체집합(1,2,3,4)까지 처리하기 위함 len(num) = 4 + 1 = (0, 1, 2, 3, 4)
        print('현재 k 반복: ', k)
        print('============================')
        backtrack(start = 0, curr = [])

    return result


nums = [1, 2, 3, 4]


print(subset(nums))