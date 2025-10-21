"""

    연속된 알파벳이 등장할 때, 해당 알파벳과 알파벳이 연속 몇 개 등장하는지 표현하려고 한다.
    만약 연속된 알파벳의 길이가 1이리면 1은 생략한다.
    예를 들어, 압축해야 할 어떤 문자열이 "aaabbcde"일 때, 구현한 문자열 압축기는 "a3b2cde"를 출력한다.


    이 후 문자열 복원기도 구현한다.
    문자열 복원기는 "a3b2cde"를 입력으로 넣으면 원래 문자열이였던 "aaabbcde"를 출력한다.

    입력
      O: 길이가 100,000 이하인 문자열로, 알파벳은 소문자로만 구성된다.
        - 압축되기 전 문자열의 길이가 10,000 이하인 입력만 주어진다. 또한, "aaab3"과 같은 잘못 압축된 입력은 주어지지 않는다

    출력
      - 문자열 압축기, 복원기가 출력하는 결과를 반환한다.

"""


## 압축
def main():

    result = []
    count = 1
    cur_str = O[0]
    for i in range(1, len(O)):
        # print('cur_str', cur_str, count)
        if cur_str == O[i]:
            count += 1
            # print(f'O[i] = {O[i]}, cur_str = {cur_str}, count = {count}')
            cur_str = O[i]
        else:
            # print('cur_str', cur_str, count)
            # print(result)
            if count > 1:
                print(cur_str, O[i], count)

                result.append(cur_str + str(count))
            else:
                result.append(cur_str)

            count = 1
            cur_str = O[i]

    print(cur_str, count)
    # for 루프에서는 문자(cur_str)가 다음 문자(O[i])와 달라질 때만 결과에 추가되므로,
    # 루프가 종료된 뒤 마지막 문자 구간은 별도로 한 번 더 추가해준다. 
    # 루프 종료 직전에 count 증가만 되고 다음 문자가 없어서 result에 append는 안되었다.
    if count > 1:
        result.append(cur_str + str(count))
    else:
        result.append(cur_str)


    return "".join(result)

O = "aaabbcdee"
# X = "a3b2cde"
print(main())
