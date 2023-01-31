# Функция кодирования
def encode_to_morse_en(text: str):
    for i in text:
        print(en_morse[i], end=' ')


# Функция декодирования
def decode_from_morse_en(code: str):
    for i in code.split():
        print(morse_en[i], end='')


# То же самое, только используем русский словарь
def encode_to_morse_ru(text: str):
    for i in text:
        print(ru_morse[i], end=' ')


def decode_from_morse_ru(code: str):
    for i in code.split():
        print(morse_ru[i], end='')


def main():
    lang = input("Выберите язык программы \n1 - Русский \n2 - Хихинглиш \n")
    if lang == "1":
        function = input("1 - Кодировать \n2 - Декодировать \n")
        if function == "1":
            encode_to_morse_ru(input("Введите текст \n").lower())
        elif function == '2':
            decode_from_morse_ru(input("Введите код \n").lower())
        else:
            print('Неверный ввод: введите 1 или 2')
    elif lang == '2':
        function = input("1 - Кодировать \n2 - Декодировать \n")
        if function == "1":
            encode_to_morse_en(input("Введите текст \n").lower())
        elif function == "2":
            decode_from_morse_en(input("Введите код \n").lower())
        else:
            print('Неверный ввод: введите 1 или 2')
    else:
        print('Неверный ввод: введите 1 или 2')


# Алфавиты и соответствующие им коды, каждому i-ой букве соответствует i-ый код
ru_alphabet = "йцукенгшщзхъфывапролджэячсмитьбю "
ru_syms = ".--- / -.-. / ..- / -.- / . / -. / --. / ---- / --.- / --.. / \
.... / --.-- / ..-. / -.-- / .-- / .- / .--. / .-. / --- / .-.. / -.. / \
...- / ..-.. / .-.- / ---. / ... / -- / .. / - / -..- / -... / \
..-- / /".split(" / ")
en_alphabet = 'abcdefghijklmnopqrstuvwxyz '
en_syms = '.- / -... / -.-. / -.. / . / ..-. / --. / .... / .. / .--- / \
-.- / .-.. / -- / -. / --- / .--. / --.- / .-. / ... / - / ..- / ...- / \
.-- / -..- / -.-- / --.. / /'.split(" / ")

# Формируем словари из алфавита и кодов Морзе
en_morse = dict(zip(en_alphabet, en_syms))
morse_en = dict(zip(en_syms, en_alphabet))

ru_morse = dict(zip(ru_alphabet, ru_syms))
morse_ru = dict(zip(ru_syms, ru_alphabet))

print(ru_morse)

while True:
    main()
    exit_question = input('Хотите завершить программу?\n1 - Продолжить\n2 -Выйти')
    if exit_question == 2:
        break


