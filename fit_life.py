"""Проект FitLife - MVP версия 1.0"""

WATER_ML_PER_KG = 30
DELIMITERS_COUNT = 40
CONVERT_TO_MILLI_FACTOR = 1000

# 1. Знакомство
print("Привет! Познакомимся?")
user_name = input("Введите Ваше имя: ")
user_age = int(input("Введите Ваш возраст: "))


# 2. Сбор данных
user_weight = float(
    input(
        "Введите Ваш вес в кг, "
        "используя точку (например 70.5): "
    )
)
user_height = float(
    input(
        "Введите Ваш рост в метрах, "
        "используя точку (например 1.75): "
    )
)


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)

# Подсчет воды: вес * 30 мл
water_needed_ml = user_weight * WATER_ML_PER_KG
water_needed_l = water_needed_ml / CONVERT_TO_MILLI_FACTOR
water_needed_l = round(water_needed_l, 1)

# 4. Вывод красивого результата
print()
print(f"{'':=>{DELIMITERS_COUNT}}")
print(f"Отчет для пользователя: {user_name}, ({user_age} л.)")
print(f"Ваш Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_needed_l} л. в день")
print()
print("Расчет окончен. Будьте здоровы!")
