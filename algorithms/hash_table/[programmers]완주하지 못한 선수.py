participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

#### 정렬 사용
def main():

    participant.sort()
    completion.sort()
    # print(participant)
    # print(completion)
    for p, c in zip(participant, completion):
        if p != c:
            return p

    return participant[-1]  # completion의 길이는 participant의 길이보다 1 작은 제약조건에 의해 완주 리스트에 없으면 마지막 선수가 미완주
# print(main())





#### 해시 사용
from collections import Counter

def main_2():

    # 리스트의 각 요소를 키로, 등장 횟수를 값으로 저장한 뒤, 두 Counter를 빼면 동일한 키의 값이 서로 차감
    part_counter = Counter(participant)
    comp_counter = Counter(completion)
    print(part_counter)
    print(comp_counter)
    diff = part_counter - comp_counter  # 남은 사람
    print(diff.keys())
    print(list(diff.keys()))
    print(list(diff.keys())[0])
    return list(diff.keys())[0]

print(main_2())
