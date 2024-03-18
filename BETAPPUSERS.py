import time
import random
import sys

#BETTING APP WITH USERS
class betting:

    def __init__(self):
        self.users = ["ola", "ire"]
        self.password = ["1234", "4322"]
        self.balance = [12000, 10000]
        self.bet_amount = 0 
        self.log = zip(self.users, self.password)
        self.welcome()

    def welcome(self):
        print("Welcome to baba ijebu betting app")
        self.choice = input("Enter 1 to register or 2 to login or 3 to Exit:>>> ")
        if self.choice == "1":
            self.register()
        elif self.choice == "2":
            self.login()
        elif self.choice == "3":
            sys.exit()
        else:
            self.welcome()

    def register(self):
        details = ['fname', 'lname', 'age', 'address', 'phone_number']
        for info in details:
            information = input(f"Enter your {info}:>>> ")
            if info == "lname":
                slicename = information[0:3]
                ran_num = random.randrange(100, 999)
                self.username = slicename + str(ran_num)
                self.users.append(self.username)
            elif info == "address":
                sliceadd = information[-3:]
                ran_add = random.randrange(120000, 900000)
                self.pwd = sliceadd + str(ran_add)
                self.password.append(self.pwd)
            while info == "age" and int(information) < 18:
                print("YOU ARE NOT ELIGIBLE TO REGISTER")
                information = input(f"Enter your {info}:>>> ")
            else:
                while info == "phone_number" and len(information) != 11:
                    print("phone must be 11 digits")
                    information = input(f"Enter your {info}:>>> ")
        bet_balance = 0
        self.balance.append(bet_balance)
        print(f"Registration complete...your username {self.username} and password is {self.pwd}")
        time.sleep(2)
        self.login()

    def login(self):
        self.user_input = input("Enter your username:>>> ")
        self.user_pwd = input("Enter your password:>>> ")
        if (self.user_input, self.user_pwd) in self.log:
            print(f"Login successful")
            self.homepage()
        else:
            print("Invalid Details...Try again")
            self.login()
    
    def homepage(self):
        self.select = input("Enter 1 to deposit money, 2 to play game, 3 to go to welcome page:>>> ")
        if self.select == "1":
            self.deposit()
        elif self.select == "2":
            self.play_game()
        elif self.select == "3":
            self.welcome()
        
    def deposit(self):
        self.bet_amount = int(input("Enter amount you want to deposit:>>> "))
        self.userbal = self.balance[self.users.index(self.user_input)]
        self.userbal = self.userbal + self.bet_amount
        self.balance[self.users.index(self.user_input)] = self.userbal  
        print(self.userbal)
        decide = input("Enter 1 to perform another transaction or 2 to go home:>>> ")
        if decide == "1":
            self.deposit()
        elif decide == "2":
            self.homepage()
        else:
            print("invalid input")
            self.welcome()

    def play_game(self):
        print("Instructions")
        decision = input("Do you want to bet now?  Enter y to proceed:>>> ").lower()
        # self.bet_amount = int(input("Enter the amount you want to bet with:>>> "))
        self.userbal = self.balance[self.users.index(self.user_input)]
        # self.userbal = self.userbal + self.bet_amount
        # self.balance[self.users.index(self.user_input)] = self.userbal
        if decision == "y":
            if self.userbal < 50:
                print("Insufficient Balance")
                self.homepage()
            else:
                self.betgame()
        else:
            self.homepage()

    def betgame(self):
        userchoice = []
        choice_1 = ['red', 'yellow', 'green', 'magenta', 'aqua']
        choice_2 = ['blue', 'purple', 'pink', 'orange', 'black']
        choice_3 = ['white', 'navy', 'peru', 'mauve', 'grey']
        machine = [random.choice(choice_1), random.choice(choice_2), random.choice(choice_3)]
        count = 0
        for i in range(3):
            player_choice = input(f"Enter color {i + 1}:>>> ")
            userchoice.append(player_choice)
        print(userchoice)
        print(machine)
        for color in userchoice:
            if color in machine:
                count += 1
        if count == 1:
            self.userbal += 50
        elif count == 2:
            self.userbal += 100
        elif count == 3:
            self.userbal += 150
        else:
            self.userbal -= 50
        response = input(f"You are done with the game. your account balance is {self.userbal} Enter 1 to play again or 2 to go back home:>> ")
        if response == "1":
            self.betgame()
        elif response == "2":
            self.homepage()
        
beet = betting()


            

            
        