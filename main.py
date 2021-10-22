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
    word = np.array([1, 0, 0, 1])
    return word


def sent_word():
    word = np.dot(create_word(), gen_matrix47())
    word = word % 2
    return word


def take_word():
    mistake = np.array([0, 1, 0, 0, 0, 1, 0])
    word = (sent_word() + mistake) % 2
    return word


def syndrome():
    syndrome = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
    return syndrome


def find_one_error(take_word):
    print("Отправленное сообщение:", sent_word())
    print("Полученное сообщение:", take_word)
    result = np.dot(take_word, check_matrix73(3)) % 2
    if np.all(result == 0):
        print("Исправленное сообщение:", take_word)
        return take_word
    if np.any(result == 1):
        for i in range(0, 7):
            if np.all(result == check_matrix73(3)[i]):
                fix = np.zeros(7)
                fix[i] = 1
                result = (fix + take_word) % 2
                print("Исправленное сообщение:", result)
                return result


def find_two_error():
    result = find_one_error(take_word())
    return result


def number_errors_and_fix():
    number_mistake = abs(sent_word() - take_word())
    k = 0
    for i in range(0, 7):
        if number_mistake[i] == 1:
            k = k + 1
    if k == 0:
        print("Отправленное сообщение:", sent_word())
        print("Полученное сообщение:", take_word())
        print("Ошибок нет!")
        return 0
    if k == 1:
        print("Одна ошибка")
        find_one_error(take_word())
        return 0
    if k == 2:
        print("Две ошибки")
        find_two_error()
        return 0
    if k > 2:
        print("Ошибок больше, чем две")
        return 0


if __name__ == '__main__':
    word = number_errors_and_fix()
