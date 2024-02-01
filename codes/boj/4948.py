import sys
import math

def build_primes(n):

    primes = [True] * (n+1)
    primes[0] = False
    primes[1] = False

    for i in range(2, int(math.ceil(n**0.5))+1):
        if primes[i]:
            for j in range(i*2, n+1, i):
                if primes[j]:
                    primes[j] = False

    return primes


primes = build_primes(123456*2)

while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break

    answer = 0
    for i in range(n+1, 2*n+1):
        if primes[i]:
            answer += 1

    print(answer)
