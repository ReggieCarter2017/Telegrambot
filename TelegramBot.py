def zeros(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    result = str(res)
    print(result)
    check = True
    count = 0
    temp = 0
    for i in result:
        if int(i) == 0:
            temp += 1
            if temp != 0 and temp > count:
                count = temp
        else:
            temp = 0
    return count

print(zeros(7))