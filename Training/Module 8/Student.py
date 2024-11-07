def calculate_required_funds(grant, expenses):
    total_needed = 0
    monthly_expenses = expenses

    for month in range(10):
        # Вычисляем недостающую сумму для каждого месяца
        if month > 0:  # Увеличиваем расходы на 3% со второго месяца
            monthly_expenses = int(monthly_expenses * 1.03)

        deficit = monthly_expenses - grant
        total_needed += deficit if deficit > 0 else 0

    return total_needed


# Ввод данных
monthly_grant = int(input("Введите ежемесячную стипендию: "))
monthly_expenses = int(input("Введите ежемесячные расходы: "))

# Расчет необходимой суммы
required_funds = calculate_required_funds(monthly_grant, monthly_expenses)

print(f"Необходимая сумма денег от родителей: {required_funds} рублей")
