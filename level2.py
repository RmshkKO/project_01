#!c:\Users\1\AppData\Local\Programs\Python\Python310\python.exe

# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

def minimum(arr):
    min = arr[0]
    for val in arr[1:]:
        if val < min:
            min = val
    return min

def maximum(arr):
    max = arr[0]
    for val in arr[1:]:
        if val > max:
            max = val
    return max
	
	
arr_test = [-12, 34, 2,331, 7633,235,587,55]
print("Minimum: ", minimum(arr_test)) 
print("Maximum: ", maximum(arr_test)) 

# Быстрая сортировка
def quicksort(arr):
    if len(arr) < 2:
        # базовый случай, массив с 0 или 1 элементом уже отсортирован
        return arr
    else:
        # рекурсивный случай. выберем опорный элемент pivot
        pivot = arr[0]
        # подмассив всех элементов, меньших, чем опорный элемент pivot
        less = [i for i in arr[1:] if i <= pivot]
        # подмассив всех элементов, превышающих опорный элемент pivot
        greater = [i for i in arr[1:] if i > pivot]
        # обединяем в порядке "сортировка для меньшего подмассива – опорный элемент – сортировка для большего подмассив"
        return quicksort(less) + [pivot] + quicksort(greater)

# Максимум - это последний элемент отсортированного списка
def maximum(arr):
    return quicksort(arr)[-1]

 # Минимум - это первый элемент отсортированного списка
def minimum(arr):
    return quicksort(arr)[0]
print('\nБыстрая сортировка')
print('min =', minimum([4,6,2,1,9,63,-134,566]))
print('max =', maximum([4,6,2,1,9,63,-134,566]))


# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

def quarter_of(num_mes):
    if num_mes in range(1, 4):
        return ' является частью первого квартала'
    elif num_mes in range(4, 7):
        return ' является частью второго квартала'
    elif num_mes in range(7, 10):
        return ' является частью третьего квартала'
    else:
        return ' является частью четвертого квартала'

mes=4

mes_names = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
print('месяц ',mes, '(',mes_names[mes-1], ')',quarter_of(mes))

# покороче
def quarter_of(month):
    q = {1: (1,3), 2:(4,6), 3:(7,9), 4:(10,12)}
    return [k for k,v in q.items() if v[0] <= month <= v[1]][0]


# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

def switch_it_up(number):
     words = ['zero','one','two','three','four','five','six','seven','eight','nine']
     if number in range(0, 9):
        return words[number]
     else:
        return 'None'
		
print (switch_it_up(1))

# через словари
def switch_it_up(number):
    return {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}.get(number)

# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    return s.replace('!', '')

print (remove_exclamation_marks('kjnsdfkj!!!! kjkj !11'));



# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    if s.endswith('!'):
        return s[:-1]
    else:
        return s

print (remove_last_em('lkdsfsfdkn !!lklkj !-!'))
# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    words = s.split()
    result = []
    for word in words:
        if word.count('!') != 1:
            result.append(word)
    return ' '.join(result)

print (remove_word_with_one_em('QQ!! W! RR'))

# однострочник
def remove_word_with_one_em(s):
    return ' '.join([w for w in s.split(' ') if w.count('!')!=1])

print(remove_word_with_one_em("Hi! Hi!! Hi!"))
