# main.py
import my_funcs

while True:
    print("\n" + "="*30)
    print("ГОЛОВНЕ МЕНЮ")
    print("="*30)
    print("1. Обчислити значення X (Завдання 1.1)")
    print("2. Побудувати піраміду (Завдання 1.2)")
    print("0. Вийти з програми")
    
    choice = input("Оберіть пункт меню (0, 1 або 2): ")
    
    if choice == '1':
        print("\nВведіть додатні числа a та b:")
        
        # Цикл для перевірки на додатні числа
        while True:
            a = float(input("a = "))
            b = float(input("b = "))
            
            if a > 0 and b > 0:
                break # Якщо все ок, виходимо з циклу
            else:
                print("Помилка! Числа a та b повинні бути додатними. Спробуйте ще раз.")
        
        res = my_funcs.calculate_x(a, b)
        print("-> Результат X =", round(res, 4))
        
    elif choice == '2':
        # Перевірка для числа N
        while True:
            n = int(input("\nВведіть парне число N (від 2 до 10) для піраміди: "))
            
            if 1 <= n <= 10 and n % 2 == 0:
                break
            else:
                print("Помилка! N має бути парним і від 2 до 10 (тобто 2, 4, 6, 8 або 10).")
        
        print("\nВаша піраміда:")
        my_funcs.print_pyramid(n)
        
    elif choice == '0':
        print("Роботу завершено. Гарного дня!")
        break
        
    else:
        print("Неправильний вибір, спробуйте ще раз.")