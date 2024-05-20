import sys

input = sys.stdin.readline

T = int(input())



for t in range(T):
    N, M = map(int, input().split())
    answer = 1

    factorial = [1] * M

    for i in range(1, M):
        factorial[i] = factorial[i-1] * (i+1)

    tmp = M-N-1
    if tmp ==  -1:
        tmp = 0
    answer = int(factorial[M-1] / (factorial[N-1] * factorial[tmp]))

    print(answer)