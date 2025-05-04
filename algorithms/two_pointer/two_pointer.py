def two_pointer(nums, target):
    nums.sort()  # -> O(n log n)

    n = len(nums)
    l = 0
    r = n -1

    # for i in range(n):
    while l < r: # l 와 r이 같아지면 반복 탈출해야함
        if nums[l] + nums[r] < target: # 타겟이 크면 왼쪽 + 1 (정렬 했기 떄문)
            l += 1
        elif nums[l] + nums[r] > target: # 타겟이 작으면 오른쪽 1 1 (정렬 했기 떄문)
            r -= 1
        elif nums[l] + nums[r] == target: # 같으면 True 반환
            return True
    return False

print(two_pointer(nums=[2, 1 ,5, 7], target=4))
print(two_pointer(nums=[4, 1, 9, 7, 5, 3, 16], target=14))
