data = [13, 29, 37, 49, 29, 7, 25, 5, 50, 2, 18, 0, 14, 16, 14, 4, 6, 14, 2, 5, 41, 27, 10, 11, 33, 6, 7, 47, 35, 35, 48, 0, 38, 1, 41, 15, 26, 46, 4, 23, 5, 32, 45, 37, 2, 33, 20, 30, 46, 20, 10, 14, 44, 25, 3, 27, 6, 22, 9, 20, 18, 43, 5, 33, 27, 41, 38, 20, 6, 2, 18, 29, 34, 40, 41, 8, 44, 30, 21, 10, 6, 1, 12, 0, 22, 28, 47, 4, 5, 1, 11, 21, 1, 44, 24, 42, 42, 41, 14, 24]
#data = [5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 2, 2, 1]
#data = [1, 5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2]
#data = [0]
#data = ["a", "b", "c"]
#data = [2, 3, 4, 7, 9]

n1 = len(data) # длина списка
print("Начальный список = ")
print(data, ". Длина", n1)
print()


print("Задание 1.1. Найдем уникальные числа")

uni_data = []
for uni_elem in data:
    if uni_elem not in uni_data:
        uni_data.append(uni_elem)
n2 = len(uni_data)
print("Список уникальных чисел = ")
print(uni_data, "Длина", n2)
#print("количество повторяющихся чисел = ", n1-n2)


print("Задание 1.2. Найдем числа, которых нет в списке до 40")

not_in_data = []
for temp_num in range(n1):
    does_not = 0
    for i in range(n1):
        #print("сравниваем число", temp_num, "с числом в списке", data[i])
        if temp_num != data[i]:
            #print("числа нет в списке")
            does_not += 1
        #else: 
            #print("число есть в списке")
    #print("не соответсвующих чисел =", does_not, "из", n1)
    if does_not == n1:
        #print("число", temp_num, "мы занесем в новый список")
        not_in_data.append(temp_num)

lenght = 40 # До скольки чисел вывести по заданию
n3=len(not_in_data)
#print("длина списка =", n3, ", Удалим лишнее")
if n3 >= lenght:
    del not_in_data[40:n3]
n3 = len(not_in_data)
print("Вот таких чисел нету в списке до длины ", n3, "= ")
print(not_in_data, "Длина", n3)


print("Задание 1.3. Отсортируем по количеству символов")

num_count_list = []
recurring_list = []
for i in range (n1): #для каждого элемента
    search_count = data[i]
    if search_count not in recurring_list:
        #print("Проверяем сколько", data[i], "в списке")
        num_count = 0
        for i in range (n1): #сравниваем с каждым
            #Проверяем сколько num
            if data[i] == search_count:
                num_count +=1
        #print("Число", search_count, "встречается в списке =", num_count, "раз")
        num_count_list.append([search_count, num_count])
        recurring_list.append(search_count)

#print("Сортируем")
for run in range (len(num_count_list)-1):
    for i in range (len(num_count_list)-1):
        #print("Сравниваем (", num_count_list[i][0], " : ", num_count_list[i][1], ") с (", num_count_list[i][0], " : " , num_count_list[i+1][1], ")")
        if num_count_list[i][1] < num_count_list[i+1][1]:
            num_count_list[i][0], num_count_list[i][1], num_count_list[i+1][0], num_count_list[i+1][1] = num_count_list[i+1][0], num_count_list[i+1][1], num_count_list[i][0], num_count_list[i][1]

#Вывод на экран:
n4 = len(recurring_list)
#print("Список уникальных", recurring_list, "длина", n4)
print("Список количества символов по убыванию = ")
print("[", end = "")
for i in range(len(num_count_list)):
    print ("(", num_count_list[i][0], " : ", end = "", sep = "")
    if i == len(num_count_list)-1: #вывод для последнего числа без запятой
        print (num_count_list[i][1], ")", end = "", sep = "")
    else:
        print (num_count_list[i][1], ")", end = ", ", sep = "")
print("]")


print("Задание 1.4. Рассчитаем среднее квадратичное отклонение")
X = 0
for i in range (len(data)):
    X = X + data[i]
X = X / len(data)
#print("X =", X)

E = 0
S = 0
for i in range (len(data)):
    E = (data[i] - X) ** 2
    #print("E =", E)
    S = S + E
S = S / (len(data))
#print("S =", S)
S = S ** (0.5)
print("Среднее квадратичное отклонение списка =", S)