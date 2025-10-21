# python 3
"""
"""


def lefthanders_and_righthanders(n_int, student_list) -> list:
    sitting_order = []
    for i in range(n_int//2):
        if student_list[i] == 'R' and student_list[i + n_int//2] == 'L':
            sitting_order.append((i + n_int//2 + 1, i + 1))
            print(i + n_int//2 + 1, i + 1)
        else:
            sitting_order.append((i + 1, i + n_int//2 + 1))
            print(i + 1, i + n_int//2 + 1)
    return sitting_order


def __starting_point():
    """
    Inside of this is the test. 
    Outside is the API
    """
    with open("input.txt", 'r') as f_input:
        n = int(f_input.readline())
        students = f_input.readline()
        # print(n, students)

    sitting = lefthanders_and_righthanders(n, students)
    with open("output.txt", 'w') as f_output:
        for each in sitting:
            f_output.write(str(each[0]) + ' ' + str(each[1]) + '\n')

__starting_point()