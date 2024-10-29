"""Домашнее задание по теме "Многопроцессное программирование" """


import time
import multiprocessing


def read_info(name):
    all_data = []   # ???? длина списка получается 5000000 во всех случаях применения данной функции
    with open(name, 'r', encoding='utf8') as file:
        # # Вариант 1 с while, readline() и rstrip('\n')
        # f = False
        # while f is False:
        #     line_file = file.readline().rstrip('\n')
        #     all_data.append(line_file)
        #     if line_file == '':
        #         f = True

        # # Вариант 2 с for и rstrip('\n')
        # for line in file:
        #     all_data.append(line.rstrip('\n'))

        # Вариант 3 с for, самый быстрый!
        for line in file:
            all_data.append(line)

        # print(all_data[0:2]) # проверка корректности записи в список
        # print(all_data[9999997:9999999]) # проверка корректности записи в список
        print(f'В новый список добавлено {len(all_data)} строк из текстового файла: {name}') # проверка корректности записи в список

# read_info('file 1.txt') # проверка корректности записи в список

file_name = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

"""линейный подход"""
# time_0 = time.time()
# for i in file_name:
#     read_info(i)
# time_1 = time.time()
# result_time = time_1 - time_0
# print(f'Время выполнения при линейном подходе, с: {result_time}')


"""многопроцессорный подход"""

if __name__ == '__main__':
    time_0 = time.time()
    with multiprocessing.Pool(4) as p:
        p.map(read_info, file_name)
    time_1 = time.time()
    result_time = time_1 - time_0
    print(f'Время выполнения при многопроцессорном подходе, с: {result_time}')



