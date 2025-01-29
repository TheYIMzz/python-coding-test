"""
    정렬되어 있지 않은 정수형 배열 nums가 주어졌다.
    nums 원소를 가지고 만들 수 있는 가장 긴 연속된 수의 갯수는 몇개인지 반환하시오.
"""
# dict 사용
def longest_consecutive_sequence_dict(nums):
    out_put = 0
    num_dict = {}

    for num in nums:
        num_dict[num] = True

    for num in num_dict:
        if num - 1 not in num_dict:  # 현재 수보다 작은 수가 없는지 확인 (가장 작은 수부터 연속된 수 찾기 위함)
            cnt = 1  # if문을 통과했다면 연속 수 최소 1번
            target = num + 1  # 다음 연속되는 수를 찾기 위한 값 설정

            while target in num_dict:
                cnt += 1 # 다음 연속되는 수가 있으므로 1증가
                target += 1  # 다음 연속되는 수를 찾기 위해 1증가

            out_put = max(out_put, cnt) # 지금까지 발견된 가장 긴 연속 시퀀스의 길이를 유지하기 위한 max 함수 사용

    return out_put

print(longest_consecutive_sequence_dict(nums=[6, 7, 4, 100, 5, 4, 4]))



# hash set 사용
def longest_consecutive_sequence_set(nums):
    out_put = 0
    num_dict = set(nums)

    for num in num_dict:
        if num - 1 not in num_dict:  # 현재 수보다 작은 수가 없는지 확인 (가장 작은 수부터 연속된 수 찾기 위함)
            cnt = 1  # if문을 통과했다면 연속 수 최소 1번
            target = num + 1  # 다음 연속되는 수를 찾기 위한 값 설정

            while target in num_dict:
                cnt += 1 # 다음 연속되는 수가 있으므로 1증가
                target += 1  # 다음 연속되는 수를 찾기 위해 1증가

            out_put = max(out_put, cnt) # 지금까지 발견된 가장 긴 연속 시퀀스의 길이를 유지하기 위한 max 함수 사용

    return out_put

print(longest_consecutive_sequence_dict(nums=[6, 7, 4, 100, 5, 4, 4]))