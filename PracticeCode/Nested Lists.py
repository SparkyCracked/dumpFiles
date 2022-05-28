if __name__ == '__main__':

    dic = {}
    scolist = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        if score in dic:
            dic[score].append(name)
        else:
            dic[score] = [name]

        if score not in scolist:
            scolist.append(score)

    scolist.remove(min(scolist))
    m = min(scolist)
    dic[m].sort()
    # print(m)

    for i in dic[m]:
        print(i)

