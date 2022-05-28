if __name__ == '__main__':
    n = int(5)
    arr = list(map(int, input("Numbers: ").split()))

    a = max(arr)

    c = arr.count(a)
    # print(c)

    for i in range(c):
        arr.remove(a)
        a = max(arr)

    print(a)
