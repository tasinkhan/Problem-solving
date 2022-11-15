def find_average():
    n = int(input())
    students_mark = {}
    for i in range(n):
        name, *line = input().split()
        students_mark[name.title()] = line
    query_name = input().title()

    marks_of_student = students_mark[query_name]
    total = 0
    for item in marks_of_student:
        total += float(item)

    average =  "{:.2f}".format(total / len(marks_of_student))
    return average

