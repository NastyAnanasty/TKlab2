import numpy as np


def X_matrix43():
    xmatr43 = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 0], [0, 1, 1]])
    return xmatr43


def gen_matrix(n, k, d):
    gen_matrix = np.eye(k)
    Xmatr = X_matrix43()
    gen_matrix = np.hstack((gen_matrix, Xmatr))
    return gen_matrix


if __name__ == '__main__':
    mat = gen_matrix(7, 4, 3)
    print(mat)
