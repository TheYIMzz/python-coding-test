"""
    리스트 [4, 9, 7, 5, 1]에서 세 개의 숫자를 더해서 15가 될 수 있나요? (중복 x)
"""

nums = [4, 9, 7, 5, 1]
target = 15

def two_sum():

    def back_track(start, curr):

        if len(curr) == 3 and sum(nums[i] for i in curr) == target:
            return curr

        for i in range(start, len(nums)):
            curr.append(i)  # 인덱스 추가
            print('현재 i값:', i)
            backtrack_result = back_track(i + 1, curr)
            print('재귀 후 curr: ', curr)
            print('backtrack_result: ', backtrack_result, '/ i 값: ', i)

            if backtrack_result:  # 재귀 호출결과에서 두 수의 인덱스 리스트를 찾았다면
                print('두 수 합 찾은 결과: ', backtrack_result)
                return backtrack_result

            pop_num = curr.pop()
            print('pop_num: ', pop_num)

    return back_track(0, [])

print(two_sum())
