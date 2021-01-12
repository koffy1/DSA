# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

# Solution

import os

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    pair = 0
    x = 0
    while x < n:
        if x+1 == n:
            break
        if ar[x] == ar[x+1]:
            pair += 1
            x += 2
        else:
            x += 1
            
    return(pair)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
