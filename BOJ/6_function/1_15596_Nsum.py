"""
https://www.acmicpc.net/problem/15596

문제
정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.

작성해야 하는 함수는 다음과 같다.

(중략)
Python 2, Python 3, PyPy, PyPy3: def solve(a: list) -> int
    - a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
    - 리턴값: a에 포함되어 있는 정수 n개의 합 (정수)
(후략)
"""


def solve(numbers):  # type(numbers==a): list
    sum = 0
    for number in numbers:
        sum += number
    return sum


def main():
    # INPUT
    numbers = map(int, input().split())
    # OUTPUT
    print(solve(numbers))


if __name__ == "__main__":
    main()

# 주어진 소스코드를 사용하면
# def solve(a):
#     ans = 0
#     for e in a:
#         ans += e
#     return ans
