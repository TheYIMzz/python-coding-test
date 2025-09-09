def solution(numbers):
    def func(x):
        return x * 10

    numbers = list(map(str, numbers))

    numbers.sort(key=func, reverse=True)

    answer = ''.join(numbers)
    return str(int(answer)) # "000", "0123" 같은 경우는 "0"으로 반환하기 위해 int -> str 변환
