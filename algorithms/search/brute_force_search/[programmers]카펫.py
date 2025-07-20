
def main():

    total = brown + yellow  # 전체 격자 수
    print(total)

    # height는 3 이상이어야 한다. (테두리 때문에 최소 3x3)
    for height in range(3, total + 1):
        print('total % height', total % height)
        if total % height == 0: # total을 현재 height로 나누었을 때 나머지가 0이면 그 height는 카펫의 세로 길이가 될 수 있음
            width = total // height  # height가 결정되면 가로(width)는 total을 height로 나눈 값
            print('width', width)
            print('height', height)
            print('노랑 칸 개수: ', (width - 2) * (height - 2))
            if (width -2) * (height -2) == yellow: # 테두리(Brown)를 제외한 내부 영역이 yellow와 같은지 확인
                return [width, height]

brown = 24
yellow = 24
print(main())