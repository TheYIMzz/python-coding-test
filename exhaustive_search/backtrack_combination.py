
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

        for i in range(start, len(nums)): # 시작범위에 start를 지정해서 증가된 i를 넘겨받아서 start로 사용해서 재귀호출된 함수에서 매번 0부터 시작하는 것 방지
            curr.append(nums[i])
            print('curr에 추가된 num: ', curr)
            backtrack(i + 1, curr) # nums에서 현재 인덱스번째 뒤쪽의 원소들만 선택하게 해서 중복 없이, 순서대로 조합을 만들기 위함 (예: [1, 2]와 [2, 1])
            curr.pop()
            print('backtrack 후 pop: ', curr)

    backtrack(start = 0, curr = [])
    return result


nums = [1, 2, 3, 4]
k = 2  # 선택할 원소의 수 (조합의 크기)

print(combination(nums, k))