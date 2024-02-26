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


def main():
    '''Основной код программы - обработка данных из файла и определение компании с самым большим количеством вакансий
    '''

    data = readcsv('vacancy.csv')
    companies = dict()
    company_sizes = dict()

    for row in data:
        if row[-1] not in companies:
            companies[row[-1]] = list()
            company_sizes[row[-1]] = 0
        companies[row[-1]].append([row[-2], row[0], row[1]])
        company_sizes[row[-1]] += 1

    company_sizes = sorted(company_sizes.items())
    for row in companies[company_sizes[-1][0]]:
        print(row)

if __name__ == '__main__':
    main()
