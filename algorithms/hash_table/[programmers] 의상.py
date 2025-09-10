from collections import Counter

# clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
def main():
    # 1. 각 의상 종류(kind)별 개수 세기
    kinds = []
    for _, kind in clothes:
        kinds.append(kind)
    print(kinds)
    counter = Counter(kinds)
    print(counter)

    answer = 1

    # 2. 각 종류마다 의상 개수 + 1 곱하기 (+1은 "그 종류를 안 입는 경우")
    for kind in counter:
        print('kind',kind)
        print('counter[kind]', counter[kind])
        answer *= (counter[kind] + 1)

    # 3. 모든 종류를 안 입는 경우(=1가지) 빼기
    return answer - 1

print(main())