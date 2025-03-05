
"""
    nums = [1, 2, 3, 4]에서 두 개의 원소를 선택해 만들 수 있는 모든 조합을 반환하시오
"""
# 조합
def combination(nums, k):
    result = []

    def backtrack(start, curr):
        if len(curr) == k:  # base case
            result.append(curr[:])
            return

        for i in range(start, len(nums)):
            curr.append(nums[i])
            print('curr에 추가된 num: ', curr)
            backtrack(i + 1, curr)
            curr.pop()
            print('backtrack 후 pop: ', curr)

    backtrack(start = 0, curr = [])
    return result


nums = [1, 2, 3, 4]
k = 2  # 선택할 원소의 수 (조합의 크기)

print(combination(nums, k))