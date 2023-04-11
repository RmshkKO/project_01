# Задача 3.1.  
# Создайте класс матрицы (или таблицы).  
# Требования к классу:  
# - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)  
# - в каждой ячейке содержится либо число, либо None  
# - доступы следующие методы матрицы:  
# * принимать новые значения,  
# * заменять существующие значения,  
# * выводить число строк и колонок.  
 
class Matrix: 
    def init(self, rows, columns):  #Конструктор класса.. на вход количество строк и столбцов матрицы для матрицы, которую мы хотим сгенерировать и  устанавливаем по умолчанию None для всех элементов матрицы. 
        self.matrix = [[None for _ in range(columns)] for _ in range(rows)] 
        self.rows = rows 
        self.columns = columns 
     
    def set_value(self, row, column, value): # метод класса который устанавливает значение (value) в конкретной ячейке, заданной строкой и столбцом (row, column) 
        self.matrix[row][column] = value 
   
   
     
    def replace_value(self, row, column, new_value): # метод класса который меняет значение в конкретной ячейке, заданной строкой и столбцом (row, column) 
      if column >= self.columns or row >= self.rows:   print("Выход за диапазон") 
      elif self.matrix[row][column] is not None:       self.matrix[row][column] = new_value 
      else: 
        print("Невозможно заменить переменную в ячейке ({}, {}) - она еще не устанавливалась.".format(row, column)) 
 
    def get_rows(self): # метод класса, который выводит число строк 
        return self.rows 
     
    def get_columns(self):# метод класса, который выводит число столбцов 
        return self.columns 
 
# Пример работы 
# создаем новую матрицу 4x8 
matrix = Matrix(4, 8) 
 
# устанавливаем значение 555 в ячейку (2,3) 
matrix.set_value(2, 3, 555) 
 
# заменяем значение в ячейке (2,3) на 666 
matrix.replace_value(2, 3, 666) 
 
# заменяем значение в ячейке, в которой еще не устанавливали значение 
matrix.replace_value(2, 4, 666) 
 
# заменяем значение в несуществующей ячейке  
matrix.replace_value(2, 9, 666) 
 
 
# выводим количество строк и столбцов матрицы 
print("строк", matrix.get_rows()) 
print("столбцов:", matrix.get_columns())
