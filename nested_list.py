def nested_list():
    python_students = []
   
    n = int(input())
    for i in range(n):
        name = input()
        mark = float(input())
        python_students.append([name, mark])
    # python_students = []
    lowest = 100
    # print(lowest)
    second_lowest = 100
    for item in python_students:
        if lowest > item[1]:
            lowest = item[1]

        for j in python_students:
            if j[1] > lowest and j[1] < second_lowest:
                second_lowest = j[1]

    second_lowest_students = []
    for student in python_students:
        name = student[0]
        mark = student[1]
        if mark == second_lowest:
            second_lowest_students.append(name)
        
    names = sorted(second_lowest_students)
    response = ''''''
    for x in names:
        response = response + x + '\n'
    
    return response

print(nested_list())