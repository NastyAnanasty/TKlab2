import numpy as np


def gen_matrix(n, k, d):
    gen_matrix = np.zeros((k, n))
    return gen_matrix


if __name__ == '__main__':
    mat = gen_matrix(7, 3, 4)
    print(mat)
