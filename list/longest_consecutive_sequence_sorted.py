"""
    정렬되어 있지 않은 정수형 배열 nums가 주어졌다.
    nums 원소를 가지고 만들 수 있는 가장 긴 연속된 수의 갯수는 몇개인지 반환하시오.
"""
# 정렬 방식 사용
def longest_consecutive_sequence_sorted(nums):
    nums.sort()

    cur_num = 1
    out_put = 0

    for i in nums:
        if cur_num == i:
            out_put += 1

        cur_num += 1

    return out_put


print(longest_consecutive_sequence_sorted(nums=[100, 4, 200, 1, 3, 2]))