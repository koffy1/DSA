# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

# Solution

import os

def countingValleys(steps, path):
    # Write your code here
    up = 0
    down = 0
    start = 0
    mountain = 0
    valley = 0

    for x in range(0, steps):
        if start >= steps:
            break
        
        if path[x] == 'U':
            up += 1
        else:
            down += 1
            
        if path[start] == 'U' and up == down:
            mountain += 1
            start = x + 1
            up = 0
            down = 0
        elif path[start] == 'D' and up == down:
            valley += 1
            start = x + 1
            up = 0
            down = 0
    return valley
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
