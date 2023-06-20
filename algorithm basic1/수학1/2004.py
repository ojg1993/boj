# 2004

n, m = map(int, input().split())

def exp_cnt(n,e):
    ans = 0
    while n:
        n //= e
        ans += n
    return ans

if not m:
    print(0)
else:
    print(min(exp_cnt(n, 5) - (exp_cnt(n-m, 5) + exp_cnt(m, 5)),
                exp_cnt(n, 2) - (exp_cnt(n-m, 2) + exp_cnt(m, 2))))

# 0의 개수는 주어진 수의 팩토리얼을 소인수 분해할 때, 10이 몇번 곱해졌는지를 의미한다.
# 10은 2와 5의 곱으로 나타낼 수 있기 때문에 0의 갯수는 2의 지수와 5의 지수중 작은값이다.
# 조합의 식이 n! / (n-m)! * m! 이다.
# 이때 2의 지수를 구하기 위해 n!을 2와 5로 나눠지는 횟수를 구하면 그 횟수가 지수와 같다.
# 지수의 계산에서는 곱하기를 +, 나누기를 -로 볼 수 있으므로,
# 아래중 작은 값을 출력하면 0의 갯수와 같다.
# 1. n을 5로 나눈 몫 - (n-m을 5로 나눈 몫 + m을 5로나눈 몫)
# 2. n을 2로 나눈 몫 - (n-m을 2로 나눈 몫 + m을 2로나눈 몫)