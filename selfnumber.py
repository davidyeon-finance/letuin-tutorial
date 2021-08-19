def myfunction(num : int):

    N = len(str(num))
    print(N)
    sum = 0
    for n in range(N):
        sum += int(str(num)[n])
    return sum + num

print(myfunction(123))