def pascal_triangle(x):     #функция треугольника Паскаля
    if x == 1:              #если количество рядов 1 то вывести [[1]]
        return [[1]]
    elif x == 2:                        #Если количество рядов 2, то вывести [[1], [1,1]]
        return [[1], [1,1]]
    else:
        proshli_treug = pascal_triangle(x-1)            #переменная для рассмотрения треугольника без последнего ряда
        last_elem = proshli_treug[-1]                   #последний элемент нового треугольника
        first_elem = [1]                                #первый элемент в треугольнике всегда единица
        for a in range(1, len(last_elem)):          #рассматриваем сумму смежных элементов
            first_elem.append(last_elem[a-1] + last_elem[a])        #добавляем к единице сумму смежных элементов из верхнего ряда
        first_elem.append(1)
        return proshli_treug + [first_elem]     #возвращаем треугольник с новыми рядами

def main():                 #общий запуск функции
    rows = int(input("Введите Ваше количество рядов : "))       #вводим количество рядов
    treug = pascal_triangle(rows) 
    for rows in treug:                  #выводим треугольник паскаля
        print(rows)

if __name__ == '__main__':  #инструкция для запуска, для импорта в другие файлы

    main()