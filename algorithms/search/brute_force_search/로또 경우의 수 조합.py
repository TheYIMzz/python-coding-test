"""
    로또를 하려고 한다.
    로또는 1부터 N까지의 자연수 중에서 6개의 공을 뽑는다.

    유토는 수상한 사람이 주는 힌트를 보고, 가능한 당첨 번호를 분석하려고 한다.
    공의 개수 N(6 ≤ N ≤ 45)이 주어졌을 때,
    유토는 가능한 당첨 번호의 조합의 경우의 수를 구하려 한다.

"""

def main():

    result = []

    def back_track(start, curr):

        if len(curr) == 6:
            result.append(curr[:])
            return

        for i in range(start, N + 1):
            curr.append(i)
            back_track(i + 1, curr)
            curr.pop()


    back_track(1, [])
    print(result)
    return len(result)

N = 8
main()
