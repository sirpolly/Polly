def main():
    рабочие_часы = 8  # Количество рабочих часов
    задачи_выполнены = 0  # Счетчик выполненных задач
    жена_позвонила = False  # Флаг, указывающий, что жена звонила

    for час in range(1, рабочие_часы + 1):
        # Генерируем случайное количество задач для выполнения
        задачи_текущего_часа = int(input(f"Сколько задач выполнил Максим в {час}-й час? "))
        задачи_выполнены += задачи_текущего_часа  # Обновляем счетчик выполненных задач
        
        # Проверяем, позвонила ли жена
        if not жена_позвонила:
            ответ = input("Жена звонит. Ответить на звонок? (да/нет): ").strip().lower()
            if ответ == "да":
                жена_позвонила = True  # Устанавливаем флаг, что Максим ответил на звонок
                print("Максим ответил на звонок.")
            else:
                print("Максим не ответил на звонок.")

    # Выводим результат
    print(f"\nМаксим выполнил {задачи_выполнены} задач за день.")
    if жена_позвонила:
        print("Нужно зайти в магазин.")

if __name__ == "__main__":
    main()
    