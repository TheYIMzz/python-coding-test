"""
 재귀 필수 구성요소
  1. base case (무조건 있어야 무한 루프 방지
        => 더 이상 재귀 호출을 하지 않아도 계산 값을 반환할 수 있는 상황
  2. 점화식 (recurrence relation)
        => 자신을 어떤식으로 다시 호출하는 것에 대한 관계식


  재귀 함수의 시간 복잡도
   => 재귀함수 전체 시간복잡도 = 재귀 함수 호출 수 x (재귀함수 하나당)시간 복잡도


"""

def factorial(n):
    if n == 1: # base case
        return 1

    return n * factorial(n - 1)  # 팩토리얼 점화식 =>  자기 자신을 n -1로 호출


print(factorial(5))

