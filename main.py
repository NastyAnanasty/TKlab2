import numpy as np


def X_matrix43():
    xmatr43 = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 0], [0, 1, 1]])
    return xmatr43


def gen_matrix47(row):
    gen_matrix = np.eye(row)
    Xmatr = X_matrix43()
    gen_matrix = np.hstack((gen_matrix, Xmatr))
    return gen_matrix


def check_matrix73(d):
    check_matrix = np.eye(d)
    Xmatr = X_matrix43()
    check_matrix = np.vstack(( Xmatr, check_matrix))
    return check_matrix


if __name__ == '__main__':
    gen = gen_matrix47(4)
    check = check_matrix73(3)
    print(gen)
    print(check)
