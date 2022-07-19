s = '1,"2,3",4,"5,6"'


def wipe(s):
    arr = s.split(",")
    arr = "".join(arr).split('"')
    arr = [",".join(list(x)) if len(x) > 1 else x for x in arr]
    print(arr)


wipe(s)
