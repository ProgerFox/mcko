def readcsv():
    '''Считывает данные из файла csv и возвращает список с полученными данными

    Описание возвращаемых данных: список с полученными данными (список)
    '''
    data = []
    with open('vacancy.csv', 'r') as readcsvfile:
        for row in readcsvfile.readlines():
            data.append(row.rstrip().split(';'))
    return data

def writecsv(data: list()):
    '''Записывает переданные данные в файл csv

    Описание аргументов: данные для записи в файл (список списков)
    '''
    with open('vacancy_new.csv', 'w') as writecsvfile:
        for row in data:
            writecsvfile.write(';'.join(row) + '\n')
def main():
    '''Основной код программы - обработка данных и определение трех самых высооплачиваемых вакансий
    '''
    data = readcsv()[1:]
    new_data = [['company', 'role', 'Salary']]
    companies = dict()

    for row in data:
        if row[-1] not in companies:
            companies[row[-1]] = list()
        companies[row[-1]].append(row)

    biggestSalaries = []
    for company in companies:
        companies[company] = sorted(companies[company], key=lambda row: int(row[0]))
        biggestSalaries.append(companies[company][-1])

    biggestSalaries = sorted(biggestSalaries, key=lambda row: int(row[0]))
    print(biggestSalaries)
    for i in range(-3, 0):
        new_data.append([biggestSalaries[i][-1], biggestSalaries[i][-2], biggestSalaries[i][0]])

    writecsv(new_data)

if __name__ == '__main__':
    main()
