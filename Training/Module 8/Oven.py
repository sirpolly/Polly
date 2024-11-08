import time


def microwave_timer(reverse_timer):
    for second in range(reverse_timer, -1, -1):
        print(f"Осталось времени: {second} секунд")

        # Проверяем ввод пользователя
        user_input = input(
            "Введите '1', если хотите забрать еду, или '0' для продолжения: "
        )

        if user_input == "1":
            print(
                f"Готово, забирай. Таймер был прерван на {second} секунде."
            )
            return
        elif user_input != "0":
            print("Неверный ввод. Пожалуйста, введите '0' или '1'.")

        # Задержка на 1 секунду только если секунды еще остались
        if second > 0:
            time.sleep(1)

    print("Кушать подано, идите жрать!")


# Ввод времени таймера с обработкой ошибок
try:
    reverse_timer = int(input("Введите время для таймера в секундах: "))
    if reverse_timer < 0:
        print("Время таймера должно быть неотрицательным.")
    else:
        microwave_timer(reverse_timer)
except ValueError:
    print("Пожалуйста, введите целое число.")
