'''
https://www.acmicpc.net/problem/1193

문제
무한히 큰 배열에 다음과 같이 분수들이 적혀있다.

1/1	1/2	1/3	1/4	1/5	…
2/1	2/2	2/3	2/4	…	…
3/1	3/2	3/3	…	…	…
4/1	4/2	…	…	…	…
5/1	…	…	…	…	…
…	…	…	…	…	…
이와 같이 나열된 분수들을 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.

X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.

출력
첫째 줄에 분수를 출력한다.

# 지그재그라는게 이해가 안가서 검색함 : https://nhs0912.tistory.com/56, https://jaimemin.tistory.com/1037
'''


import sys


def main():


if __name__ == '__main__':
    main()


# 반례 목록
# [1] 입력값 10
# 10에서 출력값 0/5가 나옴
# 해결: if x <= cnt를 if x <= denominator_numerator로 변경. cnt는 변하는 값이라 비교대상으로 적합하지 않다.
