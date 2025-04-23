
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

        for i in range(start, len(nums)): # 시작범위에 start를 지정해서 증가된 i를 넘겨받아서 start로 사용해서 재귀호출된 함수에서 매번 0부터 시작하는 것 방지
            print(f'현재 i: {i}')
            curr.append(nums[i]) # 1. 선택
            print('curr에 추가된 num: ', curr)
            backtrack(i + 1, curr)  # 2. 탐색, nums에서 현재 인덱스번째 뒤쪽의 원소들만 선택하게 해서 중복 없이, 순서대로 조합을 만들기 위함 (예: [1, 2]와 [2, 1])
            curr.pop() # 3. 되돌리기
            print('backtrack 후 pop: ', curr)

    for k in range(len(nums) + 1):  # 집합을 0(공집합) 부터 전체집합(1,2,3,4)까지 처리하기 위함 len(num) = 4 + 1 = (0, 1, 2, 3, 4)
        print('현재 k 반복: ', k)
        print('============================')
        backtrack(start = 0, curr = [])

    return result


nums = [1, 2, 3, 4]


print(subset(nums))