import random
from enum import Enum
import sys



users = []
password = []
username = ""
betbal = 0

# player_wins = 0
# python_wins = 0

def bet():
    print("\nWELCOME TO BABA IJEBU BEETING APP")
    welcome()




def welcome():
    global users
    global password
    global username
    global betbal
    
    decision = input("\nENTER.....\n1 FOR REGISTRATION\n2 FOR LOGIN\n>>> ").strip().lower()
    if decision not in ['1', '2']:
        print("\nYOU CAN ONLY USE 1 OR 2, ANY OTHER KEY IS INVALID")
        welcome()
    elif decision == '1':
        return register()
    elif decision == '2':
        return login()
        


def register():
    global users
    global password
    global username
    global betbal
    details = ['FULLNAME', 'AGE', 'ADDRESS', 'PHONE_NUMBER']
    for info in details:
        information = input(f"ENTER YOUR {info}\n>>> ").strip().lower()
        if info == 'FULLNAME':
            if information.isdigit():
                print(f"{info} MUST BE IN LETTERS")
                return register()
            else:
                slicename = information[0:4]
                ran_num = random.randrange(10, 99)
                username = slicename + str(ran_num)
                users.append(information)
                users.append(username)
        elif info  == 'AGE' and int(information) < 18:
            print(f"\nDEAR {users[0]} YOU ARE TOO YOUNG TO REGISTER")
            return register()
        elif info == 'ADDRESS':
            sliceadd = information[0:4]
            ran_add = random.randrange(100, 999)
            pwd = sliceadd + str(ran_add)
            password.append(pwd)
        while info == 'PHONE_NUMBER' and len(information) < 11 or len(information) > 15:
            print(f'\nDEAR {users[0]}, YOUR PHONE NUMBER MUST BE 11 DIGITS IF YOU ARE USING A NIGERIAN NUMBER\nAND 15 FOR INTERNATIONAL NUMBER')
            information = input(f"ENTER YOUR {info}\n>>> ")
    print(f"\nREGISTRATION COMPLETE....YOUR USERNAME IS {username.upper()} and your password is {pwd.upper()}")
    return login()

def login():
    global users
    global password
    global username
    global betbal
    user_input = input(f"ENTER YOUR USERNAME\n>>> ").strip().lower()
    user_password = input(f"ENTER YOUR PASSWORD\n>>> ").strip().lower()
    if username == user_input and password[-1] == user_password:
        print(f"\nYOU HAVE LOGGED IN SUCCESSFULLY")
        return decide()
    else:
        print("\nINVALID DETAILS...PLEASE ENTER THE CORRECT DETAILS")
        return login()

def decide():
    global users
    global password
    global username
    global betbal
    print("\nYOU MUST HAVE A DEPOSIT OF $500 TO BE ABLE TO PLAY THE GAME,\nBUT IF YOU HAVE THE MONEY, YOU CAN PLAY THE GAME DIRECTLY")
    choice = input("ENTER...\n1 TO DEPOSIT\n2 TO PLAY GAME\n>>> ")
    if choice not in ['1', '2']:
        print("YOU CAN ONLY USE 1 or 2")
        return decide()
    elif choice == '1':
        return deposit()
    elif choice == '2':
        return play_game()
    
    

def deposit():
    global users
    global password
    global username
    global betbal
    amount = int(input("ENTER THE AMOUNT YOU WISH TO DEPOSIT\nBUT IT MUST BE AT LEAST $500\n>>> "))
    betbal = betbal + amount
    print(f"\n\nDEAR {username}, YOU HAVE SUCCESSFULLY DEPOSITED  ${betbal}")
    if betbal < 500:
        print(f"\n\nDEAR {username}, YOU HAVE INSUFFICIENT FUNDS , HENCE YOU CAN'T PLAY\nYOU HAVE TO DEPOSIT AT LEAST $500 TO BE ABLE TO PLAY")
        return deposit()
    elif betbal == 500 or betbal > 500:
        return play_game()
    

def play_game():
    global betbal
    game_count = 0
    player_wins = 0
    python_wins = 0
    decision = input('\nDO YOU WISH TO BET NOW?\nENTER Y TO BET\n>>> ').strip().lower()
    if decision.lower() != 'y':
        print("\nINVALID INPUT")
        return play_game()   
    elif decision.lower() == 'y':
        if betbal < 500:
            print("\nYOU HAVE INSUFFICIENT FUNDS, GO AND DEPOSIT $500 AT LEAST TO BE ABLE TO PLAY")
            mdecide = input("\nENTER...\n1 TO DEPOSIT\n2 TO GO BACK TO HOMEPAGE\n>>>> ")
            if mdecide not in ['1', '2']:
                print("\nINVALID OPTIONS.. YOU CAN ONLY USE 1 OR 2")
                return play_game()
            elif mdecide == '1':
                return deposit()
            elif mdecide == '2':
                return welcome()
        # else:
        #     play_rps()
            

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins
        global username
        global betbal

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input('\nENTER....\n1 FOR ROCK\n2 FOR PAPER\n3 FOR SCISSORS\n>>> ').strip()
        if playerchoice not in ['1', '2', "3"]:
            print("\nYOU MUST USE 1, 2 OR 3")
            return play_rps()
        
        player = int(playerchoice)

        computerchoice = int(random.choice("123"))

        print(f"\n{username.upper()} CHOSE {str(RPS(player)).replace('RPS.', '')}.")
        print(f"\nPYTHON  CHOSE {str(RPS(computerchoice)).replace("RPS.", '')}.")

        def decide_winner(playerchoice, computerchoice):
            nonlocal player_wins
            nonlocal python_wins
            global username
            global betbal
            if player == 1 and computerchoice == 3:
                player_wins += 1
                betbal += 100
                return '🎉🎉🎉 YOU WIN!!'
            elif player == 2 and computerchoice == 1:
                player_wins += 1
                betbal += 100
                return '🎉🎉🎉 YOU WIN!!'
            elif player == 3 and computerchoice == 2:
                player_wins += 1
                betbal += 100
                return '🎉🎉🎉 YOU WIN!!'
            elif player == computerchoice:
                return 'WE HAVE A TIE GAME😲!!!'
            else:
                python_wins += 1
                betbal -= 100
                return 'PYTHON WINS🐍!!!'
            
        game_result = decide_winner(player, computerchoice)
        print(f"\nYOU NEW BALANCE AFTER PLAYING IS {betbal}")
            

        print(game_result)


        nonlocal game_count
        game_count += 1

        print(f"\nGAME COUNT: {str(game_count)}")
        print(f"\nPLAYER WINS: {str(player_wins)}")
        print(f"\nPYTHON WINS: {str(python_wins)}")


        print("\nPLAY AGAIN?")

        while True:
            playagain = input("\nENTER....\nY FOR YES\nQ FOR QUIT\n>>> ").strip().lower()
            if playagain not in ['y', 'q']:
                print("\nYOU CAN ONLY USE Y OR Q")
                continue
            else:
                break

        if playagain.lower() == 'y':
            return play_game()
        else:
            sys.exit(f"\n{username}, THANK YOU FOR PLAYING!!!😉")

    return play_rps()


    
bet()







    

