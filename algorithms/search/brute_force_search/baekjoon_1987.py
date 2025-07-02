"""
문제
세로
$R$칸, 가로
$C$칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (
$1$행
$1$열) 에는 말이 놓여 있다.

말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

입력
첫째 줄에
$R$과
$C$가 빈칸을 사이에 두고 주어진다. (
$1 ≤ R,C ≤ 20$) 둘째 줄부터
$R$개의 줄에 걸쳐서 보드에 적혀 있는
$C$개의 대문자 알파벳들이 빈칸 없이 주어진다.

출력
첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.

예제 입력 1
2 4
CAAB
ADCB
예제 출력 1
3
예제 입력 2
3 6
HFDFFB
AJHGDH
DGAGEH
예제 출력 2
6
예제 입력 3
5 5
IEFCJ
FHFKC
FFALF
HFGCF
HMCHH
예제 출력 3
10
"""

import sys, io


def main():
    R, C = map(int, sys.stdin.readline().strip().split())
    char_list = [list(sys.stdin.readline().strip()) for _ in range(R)]

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_len = 0
    visited = set()

    def back_track(r, c, count):
        nonlocal max_len
        max_len = max(max_len, count)

        for dr, dc in delta:
            next_r = dr + r
            next_c = dc + c

            if 0 <= next_r < R and 0 <= next_c < C:
                next_char = char_list[next_r][next_c]
                if next_char not in visited:
                    visited.add(next_char)
                    back_track(next_r, next_c, count + 1)
                    visited.remove(next_char)

    visited.add(char_list[0][0])
    back_track(0, 0, 1)

    print(max_len)

sys.stdin = io.StringIO("""2 4
CAAB
ADCB""")
main()