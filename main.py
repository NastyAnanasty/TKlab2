import numpy as np


def X_matrix43():
    xmatr43 = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 0], [0, 1, 1]])
    return xmatr43


def gen_matrix47():
    gen_matrix = np.eye(4)
    Xmatr = X_matrix43()
    gen_matrix = np.hstack((gen_matrix, Xmatr))
    return gen_matrix


def check_matrix73(d):
    check_matrix = np.eye(d)
    Xmatr = X_matrix43()
    check_matrix = np.vstack((Xmatr, check_matrix))
    return check_matrix


def create_word():
    word = np.array([0, 1, 1, 1])
    return word


def sent_word():
    word = np.dot(create_word(), gen_matrix47())
    word = word % 2
    return word


def take_word():
    mistake = np.array([0, 0, 0, 0, 0, 0, 1])
    word = (sent_word() + mistake) % 2
    return word


def syndrome():
    syndrome = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
    return syndrome


def find_one_error():
    print("Отправленное сообщение:", sent_word())
    print("Полученное сообщение:", take_word())
    result = np.dot(take_word(), check_matrix73(3)) % 2
    print(result)
    if np.all(result == 0):
        print("Ошибок нет! Полученное сообщение:", take_word())
        return take_word()
    if np.any(result == 1):
        for i in range(0, 8):
            if np.all(result == check_matrix73(3)[i]):
                fix = np.zeros(7)
                fix[i] = 1
                result = (fix + take_word()) % 2
                print("Ошибка исправлена! Полученное сообщение:", result)
                return result


if __name__ == '__main__':
    word = find_one_error()
