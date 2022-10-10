import sys

def print_help():
    print("""Для ориентированного взвешенного графа
эта программа может найти вес кратчайшего пути из любой вершины в любую другую

Использование программы в командной строке:

[1]              [2]
07_Floyd_Warshall.py [filename]

[1] - вызов самой программы
[2] - аргумент программы - имя файла с входными данными [filename]

Пример вызова:
07_Floyd_Warshall.py orgraph_matrix.csv

Формат [filename] формат соответствует стандартному csv-файлу.

В [filename] должны быть следующие данные
(пример для графа из 5 вершин, и 7 рёбер), :

5;A;B;C;D;E
A;0;2;0;8;4
B;2;0;3;0;0
C;0;3;0;5;1
D;8;0;5;0;7
E;4;0;1;7;0

В левом верхнем углу указывается количество вершин в графе (в примере 5).

Разделитель данных - ; - точка с запятой

Далее, по первой горизонтали и вертикали, указываются имена вершин.
Остальные места заполнены матрицей смежности для взвешенного
графа.

Вывод программы:
Матрица D, которая содержит вес пути из вершины i в вершину j (i,j - индексы
элемента матрицы D)
""")

def check_and_prepare_data(data):
    # Convertation to numbers
    try:
        data[0][0] = int(data[0][0])
    except ValueError:
        print("""ОШИБКА!

В ячейке матрицы данные которые не получается конвертировать в число!\n\nИндексы:""", i, j, "\nДанные:", data[i][j], "\n")
        exit()
    
    for i in range(1, len(data)):
        for j in range(1, len(data[i])):
            try:
                data[i][j] = int(data[i][j])
            except ValueError:
                print("""ОШИБКА!
        
В ячейке матрицы данные которые не получается конвертировать в число!\n\nИндексы:""", i, j, "\nДанные:", data[i][j], "\n")
                exit()
        
def check_number_of_arguments():
    if 2 != len(sys.argv): return False

def load_matrix_from_file():
    data_file = open(sys.argv[1])
    data = [] 
    for i in data_file:
        data.append(i.strip().split(";"))
        
    data_file.close()
    check_and_prepare_data(data)
    return data
    
def output_matrix_to_stdout(matrix):
    file = sys.stdout
    for i in range(matrix[0][0] + 1):
        for j in range(matrix[0][0] + 1):
            if i == 0 and j == 0:
                print(matrix[0][0], file=file, end="")
            elif i == 0 or j == 0:
                print(";", file=file, end="")
                if j == matrix[0][0]:
                    print(file=file)
            elif j != matrix[0][0]:
                print(str(matrix[i][j]) + ";", file=file, end="")
            else:
                print(matrix[i][j], file=file)

def give_answer():
    pass
    
if __name__ == "__main__":
    if(check_number_of_arguments() == False):
        print_help()
        exit()
    data = load_matrix_from_file()
    output_matrix_to_stdout(data)
    