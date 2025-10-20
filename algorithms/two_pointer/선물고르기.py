"""
    입력
      - N = 선물개수, N은 3 이상 5000이하의 정수
      - W = 21억 이하의 양의 정수
      - G = 길이 N의 배열로, N 개의 선물들의 무게가 저장됨. 모든 원소는 7억 이하의 양의 정수

    출력
      - 무게의 합이 W인 선물 세 개를 고를 수 있다면 YES 그렇지 않으면 NO 반환

            N = 5000
            log 10 당 약 3.3, 10의 자리수 증가마다 3.3 증가
            log(5000) 약 12.3

            log N = 2500 1250 625 310 . . .
            N^2 = 25,000,000
            N^3 = 125,000,000,000,000
"""


def solution():

    # 완전탐색
    """
    N이 최대 5000이므로 완전탐색은 N^3 = 125,000,000,000,000로 약 (1.25 * 10^14) 시간초과
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if G[i] + G[j] + G[k] == W:
                    return "YES"
    return "NO"
    """

    # 투포인터
    G.sort()
    for i in range(N -2): # i는 고정, left, right는 i +1, N-1 이므로 for loop 범위 N-2로 지정
        left = i + 1
        right = N - 1

        while left < right:

            total = G[i] + G[left] + G[right]

            if total < W:
                left += 1

            elif total > W:
                right -= 1

            else:
                return "YES"

    return "NO"


N = 5
W = 10
G = [5, 2, 3, 4, 1]
print(solution())
