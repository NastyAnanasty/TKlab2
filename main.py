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
    
def X_matrix_fill(x, n, k, d):
    while(x.shape[0] != k+1):
            string = np.random.randint(0, 2, (1, n-k))
            if(np.sum(string) >= d-1):
                x = np.vstack((x, string))
    return x


def X_matrix(n, k, d):
    if(k >= 3 and n-k > d):
        result = np.random.randint(0, 1, (1, n-k))
        count = 0
        while(result.shape[0] != k+1):
            if(result.shape[0] != k+1):
                result = X_matrix_fill(result, n, k, d)
                
            for d_i in range(2, d-1):
                combinations = set(itertools.permutations(range(1, result.shape[0]), d_i))
                strings = np.zeros(n-k)
                delete_indexes = []
                for i in combinations:
                    for u in range(d_i):
                        strings += result[i[u]] 
                    strings = strings % 2
                    if(np.sum(strings) < d - d_i):
                        for u in range(d_i):
                            delete_indexes.append(i[u])
                    strings = np.zeros(n-k)
                delete_indexes = list( dict.fromkeys(delete_indexes))
                result = np.delete(result, delete_indexes, axis=0)
                if(result.shape[0] != k+1):
                    continue
            count += 1
            if(count > 10000):
                return "too complicated task: maybe incorrect values, please change n or k values"
        return np.delete(result, 0, axis=0)
    else: 
        return "incorrect values"
    
def gen_matrix(n, k, d):
    gen_matrix = np.eye(k)
    Xmatr = X_matrix_nkd(n, k, d)
    try: 
        gen_matrix = np.hstack((gen_matrix, Xmatr))
    except ValueError:
        return "incorrect values"
    return gen_matrix

def check_matrix(n, k, d):
    check_matrix = np.eye(n-k)
    Xmatr = X_matrix_nkd(n, k, d)
    try:
        check_matrix = np.vstack((Xmatr, check_matrix))
    except ValueError:
        return "incorrect values"
    return check_matrix


if __name__ == '__main__':
    word = number_errors_and_fix()
