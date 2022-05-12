import random

while True:
    def language(answer_language: str) -> str:
        while True:
            if answer_language == "1" or answer_language == "english":
                return "1"
            elif answer_language == "2" or answer_language == "русский":
                return "2"
            else:
                print("Попробуйте еще раз/Try again")
                answer_language = input().lower().strip()


    def rules(answer: str) -> None:
        while True:
            if answer == "да":
                print(
                    """\nВам нужно угадать слово, указанное в загадке. Вы должны выбрать букву, которая есть в слове. 
Если вы ошибаетесь, то рисуется висельник. Завершите игру до того, как нарисуется висельник!
Игра началась!"""
                )
                break
            elif answer == "yes":
                print("""\nYou need to guess the word specified in the riddle. You have to choose the letter that is 
in the word. If you are wrong, then a gallows is drawn. Finish the game before the gallows are drawn! 
The game has started! """)
                break
            elif answer == "нет":
                print("\nИгра началась!")
                break
            elif answer == "no":
                print("\nThe game has started!")
                break
            else:
                print("\nВведенные данные некорректны!/The data entered is incorrect!")
                answer = input().lower().strip()


    def level(level_answer: str) -> dict:
        while True:
            if level_answer == "1" and language(level_answer) == "1":
                words = English_dictionary_easy
                print("You have chosen an easy level!")
                return words
            elif level_answer == "2" and language(level_answer) == "1":
                words = English_dictionary_hard
                print("You have chosen a complex level!")
                return words
            elif level_answer == "1" and language(level_answer) == "2":
                words = Russian_dictionary_easy
                print("Вы выбрали легкий уровень сложности!")
                return words
            elif level_answer == "2" and language(level_answer) == "2":
                words = Russian_dictionary_hard
                print("Вы выбрали сложный уровень!")
                return words
            else:
                print("\nВведенные данные некорректны!/The data entered is incorrect!")
                level_answer = input().strip()


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
        """,
    )
    max_wrong = len(picture_of_man) - 1
    Russian_dictionary_easy = {"мебель": ("диван", "стол", "табурет", "шкаф", "вешалка", "кресло", "кровать", "стул",
                                          "этажерка"),
                               "животные": ("собака", "кошка", "свинья", "мышь", "жираф", "слон", "тигр", "лев",
                                            "волк"),
                               "одежда": ("кофта", "брюки", "платье", "рубашка", "юбка", "носки", "свитер", "пальто",
                                          "куртка"),
                               "фрукты": ("банан", "апельсин", "яблоко", "ананас", "мандарин", "киви", "персик",
                                          "абрикос", "груша")}

    English_dictionary_easy = {"furniture": ("sofa", "table", "stool", "wardrobe", "hanger", "armchair", "bed", "chair",
                                             "bookcase"),
                               "animals": ("dog", "cat", "pig", "mouse", "giraffe", "elephant", "tiger", "lion",
                                           "wolf"),
                               "clothes": ("jacket", "trousers", "dress", "shirt", "skirt", "socks", "sweater", "coat",
                                           "jacket"),
                               "fruits": ("banana", "orange", "apple", "pineapple", "tangerine", "kiwi", "peach",
                                          "apricot", "pear")}

    Russian_dictionary_hard = {"физика": ("амплитуда", "вакуум", "вольтметр", "дифракция", "изолятор", "интерференция",
                                          "конвекция", "конденсация", "радиоактивность")}

    English_dictionary_hard = {"physics": ("amplitude", "vacuum", "voltmeter", "diffraction", "insulator",
                                           "interference", "convection", "condensation", "radioactivity")}

    print("Your language/Ваш язык: 1) English 2) Русский")
    answer_language = input().lower().strip()
    language(answer_language)
    if language(answer_language) == "2":
        print("Хотите ли Вы ознакомиться с правилами? Да/Нет")
    else:
        print("Do you want to read the rules? Yes/No")
    answer = input().lower().strip()
    rules(answer)
    if language(answer_language) == "2":
        print("\nВыберите уровень сложности!\nДля легкого введите 1, для сложного введите 2: ")
    else:
        print("\nSelect a difficulty level!\nEnter 1 for Easy level, enter 2 for Complex level: ")
    level_answer = input().strip()
    words1 = level(level_answer)
    topic = random.choice(list(words1.keys()))
    word = random.choice(list(words1[topic]))
    length_of_word = "_" * len(word)
    wrong = 0
    used_letter = []
    while wrong < max_wrong and length_of_word != word:
        if language(answer_language) == "2":
            print("\nТема:\n", topic)
        else:
            print("\nTopic:\n", topic)
        print(f"{picture_of_man[wrong]}\n{used_letter}\n{length_of_word}\n")
        if language(answer_language) == "2":
            print("Введите букву: ")
        else:
            print("Enter a letter: ")
        guess = input().lower()
        while guess in used_letter:
            if language(answer_language) == "2":
                print(f"Вы уже вводили букву {guess}. Введите другую букву:")
            else:
                print(f"You have already entered the letter {guess}. Please enter a different letter:")
            guess = input().lower()
        used_letter.append(guess)
        if guess in word:
            new = ""
            for i in range(len(word)):
                if guess == word[i]:
                    new += word[i]
                else:
                    new += length_of_word[i]
            length_of_word = new
        else:
            wrong += 1
    if wrong == max_wrong:
        if language(answer_language) == "2":
            print("Вас повесили")
        else:
            print("You've died")
        print(picture_of_man[wrong])
    else:
        if language(answer_language) == "2":
            print("У тебя получилось!")
        else:
            print("You've won!")
    print(f"\n{used_letter}\n{word}")
    while True:
        if language(answer_language) == "2":
            print('Еще раз? (да/нет): ')
        else:
            print('Again? (yes/no): ')
        answer = input().lower().strip()
        if answer in ("да", "нет", "yes", "no"):
            break
        if language(answer_language) == "2":
            print('Неверный ввод')
        else:
            print('Incorrect type')
    if answer == 'да' or answer == 'yes':
        continue
    else:
        if language(answer_language) == "2":
            print('Спасибо за игру!')
        else:
            print('Thank you for playing!')
        break

