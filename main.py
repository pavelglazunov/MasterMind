from random import randint
from time import sleep


def create_number():
    number = ""
    for i in range(4):
        number += str(randint(0, 9))
    return number


def start(was_active=False):
    if not was_active:
        print("╔══════════════════════════════════════════════════════════════════╗\n"
              "║  ╔╗  ╔╗ ╔══╗ ╔══╗ ╔════╗ ╔═══╗ ╔═══╗    ╔╗  ╔╗ ╔══╗ ╔╗ ╔╗ ╔══╗   ║\n"
              "║  ║║  ║║ ║╔╗║ ║╔═╝ ╚═╗╔═╝ ║╔══╝ ║╔═╗║    ║║  ║║ ╚╗╔╝ ║╚═╝║ ║╔╗╚╗  ║\n"
              "║  ║╚╗╔╝║ ║╚╝║ ║╚═╗   ║║   ║╚══╗ ║╚═╝║    ║╚╗╔╝║  ║║  ║╔╗ ║ ║║╚╗║  ║\n"
              "║  ║╔╗╔╗║ ║╔╗║ ╚═╗║   ║║   ║╔══╝ ║╔╗╔╝    ║╔╗╔╗║  ║║  ║║╚╗║ ║║ ║║  ║\n"
              "║  ║║╚╝║║ ║║║║ ╔═╝║   ║║   ║╚══╗ ║║║║     ║║╚╝║║ ╔╝╚╗ ║║ ║║ ║╚═╝║  ║\n"
              "║  ╚╝  ╚╝ ╚╝╚╝ ╚══╝   ╚╝   ╚═══╝ ╚╝╚╝     ╚╝  ╚╝ ╚══╝ ╚╝ ╚╝ ╚═══╝  ║\n"
              "╚══════════════════════════════════════════════════════════════════╝\n")
    start_game = input("Введите r, чтобы ознакомиться с правилами\n"
                       "Введите s, чтобы начать \n").lower()

    while start_game not in ["s", "r"]:
        print("Введено неправильное значение")
        start_game = input("Введите r, чтобы ознакомиться с правилами\n"
                           "Введите s, чтобы начать \n").lower()

    if start_game == "r":
        rules()
        sleep(5)
        start(True)
    return


def rules():
    print("ПРАВИЛА\n"
          "Компьютер загадывает четырехзначное число (в том числе и 0000, 0001 и тд \n"
          "Игрок делая ход, вписывает число и получает в ответ количество цифр, присутствующих в загаданном числе \n"
          "и количество цифр, стоящих на \"на своем месте\" - тое есть на тех же позициях, что и в загаданном числе\n"
          "Задача игрока за наименьшие число ходов угадать загаданное число")


def correct_input(number):
    return len(number) == 4 and (int(number) or number == "0000")


def check(number, count_now):
    count_of_input = 0
    count_of_twice = 0

    number = list(number)
    count_now = list(count_now)

    win = False

    for j in range(len(number)):
        if number[j] == count_now[j]:
            count_of_twice += 1

    for i in number:
        if i in count_now:
            count_of_input += 1
            count_now.pop(count_now.index(i))

    if count_of_twice == 4:
        win = True

    return count_of_input, count_of_twice, win


def main():
    start()
    game = True
    count = 1
    count_now = create_number()

    while game:
        input_number = input(f"Попытка номер {count}, введите число: ")
        if correct_input(input_number):
            coincidence, twice, win = check(input_number, count_now)
            if win:
                print(f"Победа, вы уложились в {count} ходов")
                break
            print(f"Совпадает: {coincidence} \n"
                  f"На своих местах: {twice}")
            count += 1
        else:
            print("Введено неправильное значение")


if __name__ == '__main__':
    # start()
    main()
