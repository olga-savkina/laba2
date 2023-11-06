#Написать функцию для определения всех чисел, на которые безостатка делится указанное число.
print("\n 1 задание\n")
def fun():
    number = int(input("введите число"))
    for i in range(1, int(number / 2 + 1)):
        if number % i == 0:
            print(i)


fun()
print("\n------------------------------------------------------------\n")
print("\n 2 задание\n")
#Напишите функцию, которая будет принимать один аргумент.
# Если в функцию передаётся список, Найдите сумму элементов между двумя первыми нулями.
#Если кортеж, найти максимальный и минимальный элементы.Поменять их местами.
#Число – найти сумму четных цифр.
#Строка – каждый символ перевести в соответствующий ему код из таблицы символов Unicode.
#Сделать проверку со всеми этими случаями.
def fun2(x):
    if (isinstance(x, list)):
        first_zero_index = x.index(0)
        second_zero_index = x.index(0, first_zero_index + 1)
        list2 = x[first_zero_index + 1:second_zero_index]
        result=sum(list2)
        return result
    elif(type(x)==tuple):
        min_num = min(x)
        max_num = max(x)
        min_index = x.index(min_num)
        max_index = x.index(max_num)
        new_tup = list(x)
        new_tup[min_index] = max_num
        new_tup[max_index] = min_num
        return tuple(new_tup)
    elif(type(x)==int):
     sum_num = 0
     while x >0:
         if x % 2 == 0:
             sum_num += x % 10
         x //= 10
     return sum_num
    elif(type(x)==str):
            unicode_list = []
            for i in x:
                unicode_list.append(ord(i))
            return unicode_list
    else:
        return "Unsupported data type"


print(fun2([1, 2, 0, 4, 5, 0, 6])) # Вывод: 9 (сумма элементов между первыми двумя нулями)
print(fun2((3, 1, 5, 2)))  # Вывод: (5, 1) (максимальный и минимальный элементы кортежа поменялись местами)
print(fun2(123456)) # Вывод: 12 (сумма четных цифр числа)
print(fun2("abc"))  # Вывод: [97, 98, 99] (коды символов Unicode)

print("\n------------------------------------------------------------\n")
print("\n 3 задание\n")
#Найти в матрице первую строку, все элементы которой упорядочены
#по возрастанию. Изменить упорядоченность элементов этой строки на
#обратную
def matrix(mat):
    for row in mat:
        if row == sorted(row):
            return row
    return None
my_mat = [
    [1, 4, 3],
    [4, 9, 6],
    [7, 8, 9]
]
result = matrix(my_mat)
if result:
    print(list(reversed(result)))
else:
    print("Нет упорядоченной строки")

print("\n------------------------------------------------------------\n")
print("\n 4 задание\n")
#Напишите программу, демонстрирующую работу try\except\finally
def division(a,b):
 try:
  res=a/b
  print("результат=",res)
 except:
  print("ошибка деления")
 finally:
     print("Выполнение блока finally")

division(10,2)
division(10,0)