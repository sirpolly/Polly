import time


def main():
    # Запрос размера файла
    while True:
        try:
            file_size = int(input("Укажите размер файла для скачивания (в Мб): "))
            if file_size <= 0:
                print(
                    "Размер файла должен быть положительным числом. Попробуйте снова."
                )
                continue
            break
        except ValueError:
            print("Пожалуйста, введите корректное число.")

    # Запрос скорости соединения
    while True:
        try:
            speed = float(input("Какова скорость вашего соединения (в Мб/с): "))
            if speed <= 0:
                print(
                    "Скорость соединения должна быть положительным числом. Попробуйте снова."
                )
                continue
            break
        except ValueError:
            print("Пожалуйста, введите корректное число.")

    # Инициализация переменных
    downloaded = 0.0  # float для скачанного объема
    seconds = 0

    # Начало процесса скачивания
    while downloaded < file_size:
        time.sleep(1)  # Имитация времени скачивания в 1 секунду
        seconds += 1

        # Увеличиваем скачанный объем, но не превышаем размер файла
        downloaded += speed
        if downloaded > file_size:
            downloaded = file_size

        # Вычисление процента скачанного
        percent = (downloaded / file_size) * 100

        # Вывод информации о прогрессе
        print(
            f"Прошло {seconds} сек. Скачано {int(downloaded)} из {file_size} Мб ({int(percent)}%)"
        )

    print(f"Скачивание завершено за {seconds} секунд.")


if __name__ == "__main__":
    main()
