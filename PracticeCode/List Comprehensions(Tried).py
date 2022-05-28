if __name__ == '__main__':
    x = int(1)
    y = int(1)
    z = int(1)
    n = int(2)

    i = [i for i in range(x + 1) if i <= x]
    j = [j for j in range(y + 1) if j <= y]
    k = [k for k in range(z + 1) if k <= z]

    process = [[num for num in range(10) if (i+j+k) <= n] for process in range(2) if process ]

    print(process)