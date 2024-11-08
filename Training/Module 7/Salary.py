62300  # Запрос зарплаты за каждый месяц
months = [
    "Январь",
    "Февраль",
    "Март",
    "Апрель",
    "Май",
    "Июнь",
    "Июль",
    "Август",
    "Сентябрь",
    "Октябрь",
    "Ноябрь",
    "Декабрь",
]
salaries = []

for month in months:
    while True:
        try:
            salary = float(input(f"Введите зарплату за {month}: "))
            salaries.append(salary)
            break
        except ValueError:
            print("Пожалуйста, введите числовое значение.")

# Вычисление средней зарплаты за год
average_salary = sum(salaries) / len(salaries)

# Вывод средней зарплаты за год
print(f"Средняя зарплата за год: {average_salary:.2f}")
