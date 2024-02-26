def readcsv():
    '''Считывает данные из файла csv и возвращает список с полученными данными

    Описание возвращаемых данных: список с полученными данными (список)
    '''
    data = []
    with open('vacancy.csv', 'r') as readcsvfile:
        for row in readcsvfile.readlines():
            data.append(row.rstrip().split(';'))
    return data

def main():
    '''Основной код программы - обработка входных данных и подбор вакансий из заданной компании
    '''
    data = readcsv()[1:]
    companies = dict()

    for row in data:
        if row[-1] not in companies:
            companies[row[-1]] = list()
        companies[row[-1]].append(row)

    print("Введите название компании:")
    s = input()
    while s != "None":
        isValide = False
        for company in companies:
            if company == s:
                isValide = True
                break

        if isValide:
            for row in companies[s]:
                print(f'В {s} найдена вакансия: {row[-2]}. З/п составит: {row[0]}')
        else:
            print("К сожалению, ничего не удалось найти")

        print("Введите название компании:")
        s = input()

if __name__ == '__main__':
    main()
