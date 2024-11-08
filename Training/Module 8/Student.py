def calculate_needed_money(educational_grant, expenses):
    total_needed = 0

    for month in range(1, 11):  # 10 месяцев
        if month > 1:
            expenses = int(expenses * 1.03)  # Увеличиваем расходы на 3%

        # Считаем, сколько денег не хватает в этом месяце
        shortfall = expenses - educational_grant

        # Если не хватает, добавляем к общему нужному
        if shortfall > 0:
            total_needed += shortfall

        print(
            f"{month}-й месяц: траты {expenses} рублей, не хватает {shortfall} рублей."
        )

    return total_needed


# Ввод данных
educational_grant = int(input("Введите ежемесячную стипендию: "))
expenses = int(input("Введите ежемесячные расходы: "))

# Вычисление и вывод результата
total_needed = calculate_needed_money(educational_grant, expenses)
print(f"Сумма денег, которую необходимо получить у родителей: {total_needed} рублей.")
