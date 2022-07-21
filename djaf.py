def func(array):
    summable = 0
    array = sorted(array)
    for a in array:
        if a > summable + 1:
            break
        summable += a
    return summable + 1


print(func([5, 7, 1, 1, 2, 3, 22]))
