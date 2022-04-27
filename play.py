import random

picture_of_man = (
    """
    --------
    |      
    |
    |
    |
    |
    ----------
    """,
    """
    --------
    |      |
    |   
    |
    |
    |
    ----------
    """,
    """
    --------
    |      |
    |      0
    |     
    |     
    |
    ----------
    """,
    """
    --------
    |      |
    |      0
    |      X
    |      
    |
    ----------
    """,
    """
    --------
    |      |
    |      0
    |     /X
    |      
    |
    ----------
    """,
    """
    --------
    |      |
    |      0
    |     /X\  
    |      
    |
    ----------
    """,
    """
    --------
    |      |
    |      0
    |     /X\  
    |     /
    ----------
    """,
    """
    --------
    |      |
    |      0
    |     /X\ 
    |     / \ 
    |
    ----------
    """
)
max_wrong = len(picture_of_man) - 1
words = {"УРОКИ": "Что можно приготовить, но нельзя съесть?",
         "ШАХМАТИСТ": "Кто ходит сидя?",
         "ДВЕРЬ": "Кто приходит, кто уходит, все ее за ручку водят.",
         "ДОРОГА": "Если б встала, до неба достала б.",
         "День": "К вечеру умирает, по утру оживает.",
         "РАДИО": "В Москве говорят, а у нас слышно.",
         "ВРЕМЯ": "Без ног и без крыльев оно, быстро летит, не догонишь его.",
         "ТУАЛЕТНАЯ": "Самая популярная бумага",
         "СЕКРЕТОМ": "Чем можно поделиться только один раз?"}

word = random.choice(list(words.keys()))
length_of_word = "_" * len(word)
wrong = 0
used_letter = []
print("Хотите ли Вы ознакомиться с правилами?")
answer = input("Введите ДА или НЕТ: ").lower().strip()
while True:
    if answer == "да":
        print("""\nВам нужно угадать слово, указанное в загадке. Вы должны выбрать букву, которая есть в слове. 
Если вы ошибаетесь, то рисуется висельник. Завершите игру до того, как нарисуется висельник!
Игра началась!""")
        break
    elif answer == 'нет':
        print("\nИгра началась!")
        break
    else:
        print("Введенные данные некорректны!")
        answer = input("Введите ДА или НЕТ: ").lower().strip()
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

