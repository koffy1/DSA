# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

# solution

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    array = list(arr)
    array.sort()
    highest = array[n-1]
    runner = 0
    count = n-2
    while count >= 0:
        if array[count] < highest:
            runner = array[count]
            break
        count -= 1
    print(runner)
