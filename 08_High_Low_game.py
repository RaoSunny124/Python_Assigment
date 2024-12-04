def high_low_game():
    print("\033[34m Welcome to the High-Low Game!\n-----------------------------\033[0m")

    from random import randint


    score = 0
    round = 0
    user_ask = input('\033[1;3m Run this game (yes or not)?:\033[0m ').strip().lower()
    if user_ask == 'not':
        print("Game stopped. See you next time!")
    elif user_ask == 'yes':
            while round < 5:
                round = round+1
                print(f'Round {round} begins!')  
                Player_num = randint(1 , 101)
                print(f"Your number is {Player_num}.")
                Computer_num = randint(1 , 101)
                user_guess = input("\033[1;3m What do u think your number is higher or lower than the computer's number(higher or lower)?:\033[0m").strip().lower()
                while user_guess not in ['higher', 'lower']:
                        user_guess = input("\033[1;3m Invalid input! Please type 'higher' or 'lower': \033[0m").strip().lower()      
                if user_guess == 'higher':
                    if Player_num > Computer_num:
                        print(f'u are right.Computer number is {Computer_num}.')
                        score += 1
                    else:
                        print(f'u are wrong.Computer number was {Computer_num}.')    
                elif user_guess == 'lower':
                    if Player_num < Computer_num:
                        print(f'u are right.Computer number is {Computer_num}.')
                        score += 1
                    else:
                        print(f'u are wrong.Computer number was {Computer_num}.') 
                print(f'Your score is now {score}.')          
                print('\033[34m------------------------------ \033[0m')
            print(f"\033[1;3m Game over! Your final score is {score} out of {round} Rounds.\033[0m")           
    else:
        print("\033[1;3m Wrong input. Please type 'yes' or 'not'.\033[0m")  
    print("\033[34mThank you for playing! 😊🎉\033[0m")    
            




high_low_game()