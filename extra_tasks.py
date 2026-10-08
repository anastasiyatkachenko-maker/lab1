# extra_tasks.py
import math

# Завдання 1: Обчислити значення виразу
print(" Обчислення виразу y = tan(α) + sin(β) ")
# Переводимо введені значення з градусів у радіани, бо math працює з радіанами
alpha_deg = float(input("Введіть кут α (в градусах): "))
beta_deg = float(input("Введіть кут β (в градусах): "))

alpha_rad = math.radians(alpha_deg)
beta_rad = math.radians(beta_deg)

y = math.tan(alpha_rad) + math.sin(beta_rad)
print(f"Результат обчислення y = {y:.4f}")


# Завдання 2: Задача про студента
print("\n Розрахунок боргу студента за 10 місяців ")
stipendia = 50.0
vitraty = 80.0
borg = 0.0

# Проходимось циклом по кожному з 10 місяців
for misyats in range(1, 11):
    if vitraty > stipendia:
        borg += (vitraty - stipendia)
        
    # Кожного місяця витрати зростають на 2%
    vitraty = vitraty * 1.02 

print(f"Загальна сума, яку студент візьме в борг: {borg:.2f} грн")