
def main():

    total = brown + yellow  # 전체 격자 수

    # height는 3 이상이어야 한다. (테두리 때문에 최소 3x3)
    for height in range(3, total + 1):
        if total % height == 0: # total을 현재 height로 나누었을 때 나머지가 0이면 그 height는 카펫의 세로 길이가 될 수 있음
            width = total // height  # height가 결정되면 가로(width)는 total을 height로 나눈 값
            if (width -2) * (height -2) == yellow:
                return [width, height]

brown = 10
yellow = 2
print(main())