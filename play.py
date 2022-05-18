import random
import dictionaries

def rules(answer):
    while True:
        if answer == "да":
            print(
                """\nВам нужно угадать слово, указанное в загадке. Вы должны выбрать букву, которая есть в слове. 
Если вы ошибаетесь, то рисуется висельник. Завершите игру до того, как нарисуется висельник!
Игра началась!"""
            )
            break
        elif answer == "нет":
            print("\nИгра началась!")
            break
        else:
            print("\nВведенные данные некорректны!")
            answer = input("Введите ДА или НЕТ: ").lower().strip()


def level(otvet):
    while True:
        if otvet == "1":
            words = dictionaries.easy_words
            print("Вы выбрали легкий уровень сложности!")
            return words
        elif otvet == "2":
            words = dictionaries.hard_words
            print("Вы выбрали сложный уровень!")
            return words
        else:
            print("Введенные данные некорректны!")
            otvet = input(
                "\nВыберите уровень сложности.\nДля легкого введите 1, для сложного введите 2: "
            ).strip()

picture_of_man = ''
with open("handpicture.txt", "r") as file:
    picture_of_man = file.read()



max_wrong = len(picture_of_man) - 1

print("Хотите ли Вы ознакомиться с правилами?")
answer = input("Введите ДА или НЕТ: ").lower().strip()
rules(answer)
otvet = input(
    "\nВыберите уровень сложности!\nДля легкого введите 1, для сложного введите 2: "
).strip()
words = level(otvet)
word = random.choice(list(words.keys()))
length_of_word = "_" * len(word)
wrong = 0
used_letter = []
while wrong < max_wrong and length_of_word != word:
    print("\nВот тебе небольшая подсказка:\n", words[word])
    print(picture_of_man[wrong])
    print("Вы уже предлагали следующие буквы: ", used_letter)
    print("Отгаданное вами в слове сейчас выглядит так: ", length_of_word, "\n")
    guess = input("Введите букву: ").upper()
    while guess in used_letter:
        print("Вы уже вводили букву ", guess)
        guess = input("Введите другую букву: ").upper()
    used_letter.append(guess)
    if guess in word:
        print(f"Буква {guess} есть в слове!")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += word[i]
            else:
                new += length_of_word[i]
        length_of_word = new
    else:
        print(f"К сожалению буквы {guess} нет в слове.")
        wrong += 1
if wrong == max_wrong:
    print("Вас повесили")
    print(picture_of_man[wrong])
else:
    print("У тебя получилось!")
print("Вы предлагали следующие буквы: ", used_letter)
print("Отгаданное вами в слове выглядит так: ", length_of_word, "\n")
print("Было загадано слово ", word)
