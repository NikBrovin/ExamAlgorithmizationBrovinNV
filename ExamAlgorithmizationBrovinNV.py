import random

class krutoi:
    def play_game():
        user_score = 0
        for _ in range(3):
            program_number = [random.randint(1, 24) for _ in range(3)]
            user_number = int(input("введите число в диапозоне от 1 до 24"))
            if user_number in program_number:
                user_score += 1
        if user_score >= 2:
            print ("вы выйграли")
        else:
            print ("вы проиграли ")
krutoi.play_game()