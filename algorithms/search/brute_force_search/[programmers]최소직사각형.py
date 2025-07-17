
def main():

    sizes = [ [60, 50], [30, 70], [60, 30], [80, 40]]

    max_w = 0
    max_h = 0

    for w, h in sizes:
        w, h = min(w, h), max(w, h)  # 작은쪽을 가로, 큰 쪽을 세로로 명함을 회전시켜서 한쪽 방향 기준으로 통일
        max_w = max(max_w, w)
        max_h = max(max_h, h)

    return max_w * max_h
print(main())