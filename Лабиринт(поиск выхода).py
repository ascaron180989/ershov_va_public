########################################################################################################################
#                                             Лабиринт (поиск выхода)                                                  #
########################################################################################################################
labyrinth = []


#  Функция поиска кратчаешего выхода
def found_way(labyrinth, finish):
    weight = 1
    for _ in range(len(labyrinth) * len(labyrinth[0])):
        for i in range(len(labyrinth)):
            for j in range(len(labyrinth[i])):
                if labyrinth[i][j] == weight:
                    #Вверх
                    if i > 0 and labyrinth[i - 1][j] == 0:
                        labyrinth[i - 1][j] = weight + 1
                    #Вниз
                    if i < (len(labyrinth) - 1) and labyrinth[i + 1][j] == 0:
                        labyrinth[i + 1][j] = weight + 1
                    #Лево
                    if j > 0 and labyrinth[i][j - 1] == 0:
                        labyrinth[i][j - 1] = weight + 1
                    #Право
                    if j < (len(labyrinth[0]) - 1) and labyrinth[i][j + 1] == 0:
                        labyrinth[i][j + 1] = weight + 1
                    if labyrinth[finish[0]][finish[1]]:
                        return True
        weight += 1
    return False


#  Функция построения пути (падписи вверх/вниз и влево/вправо добавляются в список наооборот т.к. идем от конца к началу)
def print_path(labyrinth, finish):
    i = finish[0]
    j = finish[1]
    w = labyrinth[i][j]
    result = []
    while w:
        w -= 1
        # Вверх
        if i > 0 and labyrinth[i - 1][j] == w:
            result.append('Вниз')
            i -= 1
        # Вниз
        elif i < (len(labyrinth) - 1) and labyrinth[i + 1][j] == w:
            result.append('Вверх')
            i += 1
        # Лево
        elif j > 0 and labyrinth[i][j - 1] == w:
            result.append('Вправо')
            j -= 1
        # Право
        elif j < (len(labyrinth[0]) - 1) and labyrinth[i][j + 1] == w:
            result.append('Влево')
            j += 1
    return result[::-1]



#  Читаем из файла конфигурацию лабиринта и записываем в виде матрицы.
with open('input_labyrinth.txt') as input_labyrinth:
    for line in input_labyrinth:
        labyrinth.append(line.replace('\n', '').split(' '))

#  Преобразуем лабиринт: Стены: 1 = -1, Проходы: 0 = 0, Вход: A = 1, Выход: B = 0. Так же запоминаем координаты входа/выхода
for i, row in enumerate(labyrinth):
    for j, char in enumerate(row):
        if char == '1':
            labyrinth[i][j] = -1
        elif char == 'A':
            labyrinth[i][j] = 1
            start = (i, j)
        elif char == 'B':
            labyrinth[i][j] = 0
            finish = (i, j)
        else:
            labyrinth[i][j] = 0

#  Вызываем функцию поиска кратчаешего выхода
if not found_way(labyrinth, finish):
    print('Путь не найден')
else:
    result = print_path(labyrinth, finish)
    for row in labyrinth:
        for item in row:
            print(f'{item:^3}', end=' ')
        print()
    print(result)
