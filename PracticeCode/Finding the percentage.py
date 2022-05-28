if __name__ == '__main__':
    n = int(3)
    student_marks = {}
    for _ in range(n):
        name, *line = input("Name").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = student_marks[name]

    v = student_marks[query_name]
    v = sum(v) / 3
    print("%.2f" % v)
