#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for r in range(len(matrix)):
            for i in range(len(matrix[r])):
                if i != len(matrix[r])-1:
                    end_space = ' '
                else:
                    end_space = ''
                print("{:d}".format(matrix[r][i]), end=end_space)
            print()
