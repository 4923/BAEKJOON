# 살펴보기
# 조건 1. 겹치지 않는 2개의 원소가 하나의 그룹을 이루어야 함.
#   ㄴ 그룹을 이루는 방법 : 모든 경우의 수를 고려해야 하나?
# 조건 2. 그룹의 개수 : N, 주어지는 수 : 2 * N개
# 조건 3. 그룹의 원소의 합 중 최댓값이 최소?
#   ㄴ 정렬해서 반으로 나뉘었을 때 큰 값 그룹의 최소값과 작은 값 그룹의 최댓값의 합?


import sys

N = int(sys.stdin.readline().strip())  # 만들어야 하는 그룹의 수
numbers = list(map(int, sys.stdin.readline().strip().split()))  # 2*N의 숫자
