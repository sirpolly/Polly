def main():
    # Ввод количества должников
    try:
        num_debtors = int(input("Введите количество должников: "))
    except ValueError:
        print("Введите корректное целое число.")
        return

    # Инициализация переменной для общей суммы долгов
    total_debt = 0

    # Запрос долга у каждого пятого должника
    for i in range(0, num_debtors, 5):  # Каждый пятый, начиная с 0
        try:
            debt = float(input(f"Введите сумму долга должника #{i}: "))
            total_debt += debt  # Добавляем долг к общей сумме
        except ValueError:
            print("Введите корректное число.")

    # Вывод общей суммы долгов
    print(f"Общая сумма долгов: {total_debt}")


# Запуск программы
if __name__ == "__main__":
    main()
