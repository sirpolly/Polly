import random


def rock_paper_scissors(user_choice):
    choices = ["камень", "ножницы", "бумага"]
    computer_choice = random.choice(choices)

    print(f"Вы выбрали: {user_choice}")
    print(f"Компьютер выбрал: {computer_choice}")

    if user_choice == computer_choice:
        return "Ничья!"
    elif (
        (user_choice == "камень" and computer_choice == "ножницы")
        or (user_choice == "ножницы" and computer_choice == "бумага")
        or (user_choice == "бумага" and computer_choice == "камень")
    ):
        return "Вы победили!"
    else:
        return "Вы проиграли!"


def guess_the_number(secret_number):
    user_guess = None
    attempts = 0

    while user_guess != secret_number:
        user_guess = int(input("Угадайте число от 1 до 100: "))
        attempts += 1

        if user_guess < secret_number:
            print("Слишком маленькое число, попробуйте снова.")
        elif user_guess > secret_number:
            print("Слишком большое число, попробуйте снова.")
        else:
            print(
                f"Поздравляем! Вы угадали число {secret_number} "
                f"за {attempts} попыток."
            )


def main_menu():
    while True:
        print("\nВыберите игру:")
        print("1. Камень, ножницы, бумага")
        print("2. Угадай число")
        print("3. Выход")

        choice = input("Введите номер игры: ")

        if choice == "1":
            user_choice = input("Введите ваш выбор (камень, ножницы, бумага): ").lower()

            if user_choice in ["камень", "ножницы", "бумага"]:
                result = rock_paper_scissors(user_choice)
                print(result)
            else:
                print(
                    "Некорректный выбор. Пожалуйста, выберите "
                    "камень, ножницы или бумагу."
                )

        elif choice == "2":
            secret_number = random.randint(1, 100)
            guess_the_number(secret_number)

        elif choice == "3":
            print("Спасибо за игру! До свидания!")
            break

        else:
            print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")


# Запуск главного меню
main_menu()
