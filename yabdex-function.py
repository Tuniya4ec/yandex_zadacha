from logging import lastResort

mas = [1,1,0,1,1,1,0,1,1,0,1,0,1,1,1,1,0,1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,0,0,1,1,1,0,1,1,1,1,0,1,1,0,1,1,1,0,0,1,0,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,0,0,1,1,1,0,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,0,1,1,1,0,1,0,0,
       0,0,1,0,0,1,0,0,0,0,0,1,0,1,1,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,
       1,0,1,1,1,1,1,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,0,1,0,0,1,0,1,1,1,1,0,1,0,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,0,1,1,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,0,0,1,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,
       0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,1,1,0,0,0,0,1,1,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,1,1,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0]

counter_mas = []
new_mas = []
frst_index_mas = []
lst_index_mas = []
sum_mas = [0]
counter = 0
first_index = 0
zereo_index = 0



for i in range(len(mas)):
    if mas[i] == 1:
        if counter == 0:
            first_index = i  # Запоминаем начальный индекс новой последовательности единиц
        counter += 1
    else:
        if counter > 0:
            counter_mas.append(counter)
            lst_index_mas.append(i - 1)
            frst_index_mas.append(first_index)
            counter = 0  # Сбрасываем счетчик после окончания последовательности




# Проверяем, осталась ли незавершённая последовательность единиц после цикла
if counter > 0:
    counter_mas.append(counter)
    lst_index_mas.append(len(mas) - 1)
    frst_index_mas.append(first_index)



# Проверяем условия для нахождения индексов, где стоит только один ноль между единицами
for i in range(1, len(mas) - 1):
    if mas[i - 1] == 1 and mas[i] == 0 and mas[i + 1] == 1:
        new_mas.append(i)


sum_mas = sum_mas * (len(lst_index_mas))  # Инициализируем массив суммы с длиной как у lst_index_mas
for i in range(len(new_mas)):
    for g in range(len(lst_index_mas)):  # Ограничиваем диапазон до len(lst_index_mas) - 1
        if lst_index_mas[g] == (new_mas[i] - 1):
            sum_mas[g] = (lst_index_mas[g] - frst_index_mas[g] + 1) + (lst_index_mas[g + 1] - frst_index_mas[g + 1] + 1)
            print("Строка единиц, которая подходит под условие: " + "1 " * (lst_index_mas[g] - frst_index_mas[g] + 1) + "0 " + "1 " * (lst_index_mas[g + 1] - frst_index_mas[g + 1] + 1) + ", в сумме получается = " + str(sum_mas[g]))

sum_mas.sort()






# Выводим все результаты один раз
print("Массив индексов, где стоит только один ноль между единицами:", new_mas)
print("Счётчик единиц:", counter_mas)
print("Индексы начала строки единиц:", frst_index_mas)
print("Индекс конца строки единиц:", lst_index_mas)
print("Сумма всех строк, подходящих под условие = " + str(sum_mas))
print("Самая большая длина единиц поллучилась: " + str(max(sum_mas)))