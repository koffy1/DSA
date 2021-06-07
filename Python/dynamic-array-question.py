def dynamicArray(n, queries):
    arr = []
    lastAnswer = 0
    answers = []
    for i in range(n):
        arr.append([])
    for j in range(q):
        query = queries[j]
        qType = query[0]
        x = query[1]
        y = query[2]
        index = ((x ^ lastAnswer) % n)
        if qType == 1:
            arr[index].append(y)
        else:
            value = y % len(arr[index])
            lastAnswer = arr[index][value]
            answers.append(lastAnswer)
    return (answers)