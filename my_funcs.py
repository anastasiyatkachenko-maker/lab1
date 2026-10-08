# my_funcs.py

def calculate_x(a, b):
    # Обчислення значення X за формулами з варіанту
    if a > b:
        x = (2 * a / b) + 1
    elif a == b:
        x = -445
    else: # якщо a < b
        x = (b + 5) / a
    return x

def print_pyramid(n):
    # Будуємо пірамідку з парних чисел
    # Використовуємо прості цикли, щоб вивести відступи і числа
    for i in range(2, n + 1, 2):
        row_str = ""
        
        # Ліва частина (зростання чисел)
        for j in range(2, i + 1, 2):
            row_str += str(j) + " "
            
        # Права частина (спадання чисел)
        for j in range(i - 2, 0, -2):
            row_str += str(j) + " "
        
        # Рахуємо пробіли для центрування рядка (щоб виглядало як піраміда)
        spaces = " " * (n - i)
        print(spaces + row_str.strip())