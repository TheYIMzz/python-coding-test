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
# print(two_sum(nums=[4, 1, 9, 7, 5, 3, 16], target=14))

########################################################################


def two_pointer(nums, target):
    nums.sort()  # -> O(n log n)

    n = len(nums)
    l = 0
    r = n -1

    # for i in range(n):
    while l < r: # l 와 r이 같아지면 반복 탈출해야함
        if nums[l] + nums[r] < target:
            l += 1
        elif nums[l] + nums[r] > target:
            r -= 1
        elif nums[l] + nums[r] == target:
            # if l == r:
            #     return False
            # print(nums[l])
            # print(nums[r])
            return True
    return False

print(two_pointer(nums = [2, 1 ,5, 7], target=4))

















