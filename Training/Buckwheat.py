# Изначальное количество гречки в килограммах
initial_weight = 100
# Количество гречки, которое уходит в месяц
monthly_decrease = 4

# Цикл for для подсчета оставшегося количества гречки
for month in range(1, (initial_weight // monthly_decrease) + 1):
    remaining_weight = initial_weight - (monthly_decrease * month)
    print(f"Через {month} месяц(а)(ев) у вас будет {remaining_weight} кг гречки.")

# Вывод информации, когда гречка полностью расходуется
if remaining_weight <= 0:
    print("Гречка закончится через", month, "месяц(а)(ев).")
