from math import inf

# главная функция
def dynamic_time_warping (time_seq1=[], time_seq2=[]):
    try:
        result = best_way(time_seq1, time_seq2)
        return result
    except:
        raise Exception


# функция, считающая расстояние между координатами

def distance(x, y):
    return abs(x - y)

# функция, строящая матрицу расстояний

def matrix_distance (time_seq1=[], time_seq2=[]):
    matr = [[0] * (len(time_seq2) + 1) for s in range(len(time_seq1) + 1)]  # заполняем матрицы нулями
    for i in range(len(time_seq1) + 1):
        matr[i][0] = inf
    for j in range(len(time_seq2) + 1):
        matr[0][j] = inf
    for i in range(len(time_seq1)):
        for j in range(len(time_seq2)):
            matr[i + 1][j + 1] = distance(time_seq1[i], time_seq2[j])
    return matr

# функция, строящая матрицу деформаций

def matrix_deformation (time_seq1=[], time_seq2=[]):
    matr = matrix_distance(time_seq1, time_seq2)
    for i in range(2, len(time_seq2) + 1):
        matr[1][i] = matr[1][i] + matr[1][i - 1]  # считаем деформацию для 1 строчки
    for i in range(2, len(time_seq1) + 1):
        matr[i][1] = matr[i][1] + matr[i - 1][1]  # считаем деформацию для 1 столбца
    for i in range(2, len(time_seq1) + 1):  # считаем деформацию для остальных элементов
        for j in range(2, len(time_seq2) + 1):
            matr[i][j] = matr[i][j] + min(matr[i - 1][j - 1], matr[i - 1][j], matr[i][j - 1])
    return matr

# функция, строящая лучший путь деформации

def best_way (time_seq1=[], time_seq2=[]):
    if not len(time_seq1) or not len(time_seq2):
        raise Exception
    matr = matrix_deformation(time_seq1, time_seq2)
    print(matr)
    way = list()
    elem_way = list()
    n = len(time_seq1)
    m = len(time_seq2)

    while (n != 0 or m != 0):
        elem_way.append(matr[n][m])
        way.append([n - 1, m - 1])  #создаем массив с координатами лучшего пути
        prev = min(matr[n][m - 1], matr[n - 1][m], matr[n - 1][m - 1])
        if matr[n - 1][m - 1] == prev:
            n, m = n - 1, m - 1
        elif matr[n - 1][m] == prev:
            n, m = n - 1, m
        else:
            n, m = n, m - 1
    if len(way) > 0:
        cost_dtw = sum(elem_way) // len(way)  #считаем накопленную деформацию
        return (way [::-1], cost_dtw)
    
