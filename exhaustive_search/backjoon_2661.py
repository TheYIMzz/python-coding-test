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

import sys
import io
sys.setrecursionlimit(10**7)
test_input = """7
"""

sys.stdin = io.StringIO(test_input)
n = int(sys.stdin.readline().strip())
nums = [1, 2, 3]

# 뒤쪽을 검사해서 XX 패턴이 있는지 체크하는 함수
def is_good(seq):
    l = len(seq)

    print('반복전 seq: ', seq)
    # k 는 반복 블록의 길이
    for k in range(1, l//2 + 1):  # 좋은 수열을 판단하기 위해 블록은 2개가 필요하므로 2로 나누고 소수점은 필요없으니 버리고 range가 -1까지 가므로 +1 더해준다
        print(seq)
        print('k =', k)
        print(f'수열비교:  {seq[-k:]} == {seq[-2 * k:-k]}' )
        if seq[-k:] == seq[-2 * k:-k]: # 뒤에서 k개 요소(seq[-k:])와 그 앞 k개 요소(seq[-2*k:-k])를 잘라와 비교, 같다면 나쁜수열
            return False
    return True

def back_track(curr):
    # 목표 길이 도달하면 결과 출력 후 종료
    if len(curr) == n:
        print(''.join(map(str, curr)))
        sys.exit(0)

    for num in nums:
        curr.append(num)  # 1. 선택
        print('append 후 curr: ', curr)
        if is_good(curr):  # 2. 탐색
            back_track(curr)
        print(curr)
        curr.pop()  # 3. 되돌리기
        print('pop 후 curr: ', curr)

# 탐색 시작
back_track([])


