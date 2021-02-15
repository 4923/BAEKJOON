'''
문제
상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.
상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)

출력
상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.
'''

# 중요한건 개수
# 5kg 봉지로 채울 수 있을 만큼 채우고 나머지는 3kg로 해결
# -1이 출력되는 조건: N이 5와 3으로 분할되지 않을 때 (공배수 문제 아님)

# [입력]
n = int(input())

# [풀이]
# 사용하는 봉지의 개수
result = 0 
while n > 0 :

    # [if] 남은 무게를 5kg봉지로 해결할 수 있는지 확인
    # 위 조건을 1순위로 확인하고 3kg 봉지를 사용해야 함
    if n % 5 == 0:
        result += n//5
        # print(f'\t[break] n == {n}, n//5 == {n//5}')
        break

    # 3kg 봉지를 최소한으로 사용한다.
    n -= 3
    result += 1
    # print(f'n: {n} result: {result}')

    # [exception] 3과 5로 분할할 수 없을 때
    if n < 0 :
        result = -1
        # print(f'\n\t[exception] n == {n} result == {result}')
        break

# [출력]
print(result)

# -----------------
# 반례 확인
# 1) 입력값 100 / 출력 22 -> 정답 20