import Euclid               #импорты
import exchanges
import pascal
import perfection

def main():
    x = int(input("Выберите файл : Euclid(1), exchanges(2) , pascal(3), perfection(4) "))       #вывод функций
    match x:
        case 1 :
            Euclid.main()
        case 2 :
            exchanges.main()
        case 3 :
            pascal.main()
        case 4 : 
            perfection.main()
        case _:
            print("До свидания!")
    
if __name__ == '__main__':  #инструкция для запуска, для импорта в другие файлы
    main()