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

def main():

    # 압축
    def func_1(word):
        if not word:
            return ""

        cur_str = word[0]
        count = 1
        result = []
        for i in range(1, len(word)):

            if cur_str == word[i]:
                count += 1

            else:
                if count > 1:
                    result.append(cur_str + str(count))

                else:
                    result.append(cur_str)

                cur_str = word[i]
                count = 1

        # for 루프에서는 문자(cur_str)가 다음 문자(O[i])와 달라질 때만 결과에 추가되므로,
        # 루프가 종료된 뒤 마지막 문자 구간은 별도로 한 번 더 추가해준다.
        # 루프 종료 직전에 count 증가만 되고 다음 문자가 없어서 result에 append는 안되었다.
        if count > 1:
            result.append(cur_str + str(count))
        else:
            result.append(cur_str)

        return "".join(result)



    # 복원
    def func_2(word):

        if not word:
            return ""

        result = []

        N = len(word)
        i = 0
        while i < N:
            if word[i].isalpha():
                j = i + 1
                count = ""

                while j < N and word[j].isdigit():
                    count += word[j]
                    j += 1

                print(word[i], count)
                if count:
                    result.append(word[i] * int(count))
                else:
                    result.append(word[i])

                i = j  # i를 j로 갱신해서 숫자인건 건너뛰기
        print("".join(result))


    print(f'압축 결과: {func_1(O)}')
    print("===============")
    print(f'복원 결과: {func_2(O_1)}')


O = "aaabbcdee"
O_1 = "a3b2cde123"
main()
