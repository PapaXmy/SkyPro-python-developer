import random

list_words = ["paskal", "python", "go", "rust", "delphi"]

morse_dict = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
}

answers = []


def morse_encode(word):
    """
    Получает слово, возвращает его в виде азбуки морзе.
    """

    morse_word = []

    for i in word:

        for key, value in morse_dict.items():
            if i == key:
                morse_word.append(value)

    return " ".join(morse_word)


def get_word(words):
    """
    Получает список слов и возвращает случайное слово из списка
    """

    mixing_word = random.sample(words, 1)

    return "".join(mixing_word)


def print_statistics(answer):
    """
    Печатает статистику на основе ответов пользователя из списка answers
    """

    right = [i for i in answer if i is True]
    wrong = [i for i in answer if i is False]
    print(
        f"Всего задачек: {len(answers)}\n"
        f"Отвечено верно: {len(right)}\n"
        f"Отвечено неверно: {len(wrong)}"
    )


user_answer = input(
    "Сегодня мы потренируемся расшифровать морзяку.\n" "Нажмите Enter и начнем."
)


# цикл по вопросам
for number in range(1, 6):
    random_word = get_word(list_words)  # получаем случайное слово
    user_answer = input(
        f"Слово {number} {morse_encode(random_word)}\n").lower()

    # проверяем верно ли ответил пользователь
    if user_answer == random_word:
        print(f"Верно, {random_word}!")
        answers.append(True)
    else:
        print(f"Неверно, {random_word}!")
        answers.append(False)


# печатаем статистику
print("---------------")
print_statistics(answers)
