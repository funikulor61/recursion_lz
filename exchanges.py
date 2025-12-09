def permutations(elements):         #функция перестановок
    result = []                     #создаем список итоговой перестановки
    if len(elements) == 0:              #(базовый случай) если длинна списка 0, то выводим пустой список
        return [[]]
    else:
        for i in range(len(elements)):          #для элементов списка
            taken = elements[i]             # i-тый элемент списка
            remaining = elements[:i] + elements[i+1:]         #убираем из списка i-тый элемент
            for j in permutations(remaining):       #рекурсивный случай, разбиваем на случаи дальше
                result.append([taken] + j)              #в списке итоговой перестановки записыаем взятый элемент(taken) к случаям
        
        return result           #возвращаем результат
    


def main():    #общий запуск функций
    spisok = (input("Введите Ваши элементы : ")).split()        #создаем список наших элементов
    print("Вот Ваши все перестановки : \n")
    for b in permutations(spisok):          #вызываем нашу функию
        print(b)

if __name__ == '__main__':  #инструкция для запуска, для импорта в другие файлы
    main()
