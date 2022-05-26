
if __name__ == '__main__':
    n = int(input("num"))
    i = 1
    t = 2

    while t < n + 1:

        if t == 9:
            i = (i*1000) + 900 + t
            t = t +1
        elif t == 99:
            i = (i * 100000) + t
            t = t + 1
        elif t < 12:
            i = (i*10) + t
            t = t + 1
        else:
            i = (i * 100) + t
            t = t + 1

    print(i)
