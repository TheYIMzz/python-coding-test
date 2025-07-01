"""
    문제
    숫자 1, 2, 3으로만 이루어지는 수열이 있다.
    임의의 길이의 인접한 두 개의 부분 수열이 동일한 것이 있으면, 그 수열을 나쁜 수열이라고 부른다.
    그렇지 않은 수열은 좋은 수열이다.

    다음은 나쁜 수열의 예이다.
    33
    32121323
    123123213

    다음은 좋은 수열의 예이다.
    2
    32
    32123
    1232123
        => 좋은 수열은 연속된 블록이 두 번 반복되는 패턴(XX)이 없는 것

    길이가 N인 좋은 수열들을 N자리의 정수로 보아 그중 가장 작은 수를 나타내는 수열을 구하는 프로그램을 작성하라.
    예를 들면, 1213121과 2123212는 모두 좋은 수열이지만 그 중에서 작은 수를 나타내는 수열은 1213121이다.

    입력
    입력은 숫자 N하나로 이루어진다. N은 1 이상 80 이하이다.

    출력
    첫 번째 줄에 1, 2, 3으로만 이루어져 있는 길이가 N인 좋은 수열들 중에서 가장 작은 수를 나타내는 수열만 출력한다.
    수열을 이루는 1, 2, 3들 사이에는 빈칸을 두지 않는다.

    입력 예제
    7

    출력 예제
    1213121
"""
import io, sys


def is_good(curr):
    l = len(curr)
    print('반복전 curr: ', curr)

    for i in range(1, l // 2 + 1): # 좋은 수열을 판단하려면 같은 길이의 블록 2개가 필요(2로 나눔). 길이 0부터 시작하면 [-0:]과 같은 잘못된 인덱싱이 발생하므로 range(1, ...)로 시작하고, range는 끝 값을 포함하지 않으므로 +1을 더해준다.
        print(curr)
        print('k =', i)
        print(f'수열비교:  {curr[-i:]} == {curr[-2 * i:-i]}')
        if curr[-i:] == curr[-2*i:-i]:  # 뒤에서 i개 요소(seq[-i:])와 그 앞 i개 요소(seq[-2*i:-i])를 잘라와 비교, 같다면 나쁜수열
            return False
    return True


def main():

    n = int(sys.stdin.readline().strip().split()[0])
    nums = [1, 2, 3]

    def back_track(curr):
        # 목표 길이 도달하면 결과 출력 후 종료
        if len(curr) == n:
            print("".join(map(str, curr)))
            # print(curr)
            sys.exit(0)

        for num in nums:
            curr.append(num)   # 1. 선택
            print('append 후 curr: ', curr)
            if is_good(curr):
                back_track(curr)   # 2. 탐색
            curr.pop()   # 3. 되돌리기
            print('pop 후 curr: ', curr)
    back_track([])



test_input = """7"""
sys.stdin = io.StringIO(test_input)

main()