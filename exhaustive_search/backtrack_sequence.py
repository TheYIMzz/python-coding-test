"""
    백트랙킹(Back Tracking)
        solution이 될 가능성이 없는 candidate는 더 이상 탐색하지 않고
        candidate를 포기(backtrack)하면서 탐색

    nums = [1, 2, 3, 4]로 만들 수 있는 모든 순열을 반환하시오
"""

# 순열
def permute(nums):

    def backtrack(curr):
        if len(curr) == len(nums): # base case
            ans.append(curr[:])
            return

        for num in nums:
            if num not in curr:
                curr.append(num)
                print('curr에 추가된 num: ', curr)
                backtrack(curr)
                curr.pop()
                print('backtrack 후 pop: ', curr)

    ans = []
    backtrack([])
    return ans

nums = [1, 2, 3, 4]

print(permute(nums))
