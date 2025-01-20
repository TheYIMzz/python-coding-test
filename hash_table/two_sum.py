"""
    1. 해시테이블의 내부는 리스트 혹은 배열 구조 (하나의 인덱스에 해시값, key, value가 저장된다.)
    2. 데이터 검색 방식은 입력받은 키를 해시 함수를 통해 인덱스를 찾고 그 인덱스의 해시 값과 해시 함수를 통해 나온 해시 값을 비교하여 찾는다
        (해시 값까지 비교하는 이유는 이미 할당된 인덱스인 경우 충돌 방지로 이동된 인덱스에 저장하기 떄문에 해시 값까지 비교하여 찾는다.)
    3. 해시함수를 통해 반환된 인덱스로 리스트의 특정 인덱스로 직접 접근하는건 O(1)이니까 딕셔너리의 데이터를 key로 찾는건 결국 O(1)이다
"""

def two_sum(nums, target):
    memo = {}

    for v in nums:  # -> O(n)
        memo[v] = 1 # 값에는 아무 값이나 넣음

    for v in nums:
        needed_number = target - v
        if needed_number in memo:  # -> 딕셔너리 key in으로 시간복잡도 O(1)
            # nums의 같은 값은 제외하는 로직 추가하기
            return True

    return False

print(two_sum(nums = [4, 1, 9, 7, 5, 3, 16], target= 14))