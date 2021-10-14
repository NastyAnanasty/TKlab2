import numpy as np


def gen_matrix(n, k, d):
    gen_matrix = np.zeros((k, n))
    for i in range(0, gen_matrix.shape[0]):
        for j in range(0, k):
            if i == j:
                gen_matrix[i][j] = 1
    return gen_matrix


if __name__ == '__main__':
    mat = gen_matrix(7, 3, 4)
    print(mat)
