"""
#    O(n^2)
"""
def two_sum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            print(nums[i], 'i')
            print(nums[j], 'j')
            print('==================')
            if nums[i] + nums[j] == target:
                return True
    return False # 모든 반복문 끝나고도 target 과 같은게 없다면 False 리턴
print(two_sum(nums=[4, 1, 9, 7, 5, 3, 16], target=14))
