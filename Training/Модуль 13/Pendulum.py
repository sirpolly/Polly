def main():
    # Получаем ввод от пользователя с контролем
    while True:
        try:
            initial_amplitude = float(input("Введите начальную амплитуду (в см): "))
            if initial_amplitude <= 0:
                print("Амплитуда должна быть положительным числом. Попробуйте снова.")
                continue
            break
        except ValueError:
            print("Введите корректное число.")

    while True:
        try:
            final_amplitude = float(input("Введите амплитуду остановки (в см): "))
            if final_amplitude <= 0:
                print(
                    "Амплитуда остановки должна быть положительным числом. Попробуйте снова."
                )
                continue
            break
        except ValueError:
            print("Введите корректное число.")

    # Условия затухания
    decay_rate = 0.084  # 8.4%
    current_amplitude = initial_amplitude
    count = 0

    # Считаем количество колебаний, пока амплитуда не станет меньше конечной
    while current_amplitude > final_amplitude:
        current_amplitude *= 1 - decay_rate
        count += 1

    # Выводим результат
    print(f"Маятник считается остановившимся через {count} колебаний")


if __name__ == "__main__":
    main()
