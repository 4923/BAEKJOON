"""
https://www.acmicpc.net/problem/2869

문제
땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.
달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 
또, 정상에 올라간 후에는 미끄러지지 않는다.

달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다.
(1 ≤ B < A ≤ V ≤ 1,000,000,000)

출력
첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.
"""

import sys
import math  # ceil

# 입력
up, down, height = map(int, sys.stdin.readline().strip().split())

# 미끄러져 내려가는 높이를 포함하여 하루에 올라가는 총 높이
only_up = up - down

# 마지막 날을 제외한 날에 올라가야하는 높이
day_height = height - up

# 결과
days = math.ceil(day_height / only_up) + 1
print(days)
