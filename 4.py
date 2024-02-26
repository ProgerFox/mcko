def readcsv(file: str):
    '''Считывает данные из файла csv и возвращает список с полученными данными

    Описание аргументов: файл, из которого будет производиться считывание данных
    Описание возвращаемых данных: список с полученными данными (список)
    '''
    data = []
    with open(file, 'r') as readcsvfile:
        for row in readcsvfile.readlines():
            data.append(row.rstrip().split(';'))
    return data

def writecsv(data: list()):
    '''Записывает переданные данные в файл csv

    Описание аргументов: данные для записи в файл (список списков)
    '''
    with open('vacancy_procent.csv', 'w') as writecsvfile:
        for row in data:
            writecsvfile.write(';'.join(row) + '\n')
def main():
    '''Основной код программы - обработка данных из файла и определение процентного отношения данной зарплаты к средней зарплате
    '''

    data = readcsv('vacancy.csv')
    work_Types = dict()

    for row in data[1:]:
        if row[1] not in work_Types:
            work_Types[row[1]] = [0, 0]
        work_Types[row[1]][0] += int(row[0])
        work_Types[row[1]][1] += 1

    new_data = [data[0] + ['percent']]
    for row in data[1:]:
        average = int(work_Types[row[1]][0]) / int(work_Types[row[1]][1])
        new_data.append(row + [str(int(int(row[0]) / average * 100 * 10 // 10)) + '%'])

    writecsv(new_data)

if __name__ == '__main__':
    main()
