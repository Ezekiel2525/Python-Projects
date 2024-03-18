import time
import random
import sys


#BETTING APP WITHOUT USERS
class betting:
    def __init__(self):
        self.users = []
        self.password =  []
        self.betbal = [0]
        self.username = ""
        self.welcome()
        
    def welcome(self):
        print("Welcome to Baba ijebu betting app")
        self.choice = input("Enter 1 to register:>> ").strip().lower()
        if self.choice == "1":
            self.register()
        else:
            print("invalid input")
            self.welcome()

    def register(self):
        details = ['firstname', 'lastname', 'age', 'address', 'phone_number']
        for info in details:
            information = input(f"Enter your {info}:>>> ")
            if info == "lastname":
                slicename = information[0:3]
                ran_num = random.randrange(100, 999)
                self.username = slicename + str(ran_num)
                self.users.append(self.username)
            elif info == "address":
                sliceadd = information[-3:]
                ran_add = random.randrange(1111, 9999)
                self.pwd = sliceadd + str(ran_add)
                self.password.append(self.pwd)
            while info == "age" and int(information) < 18:
                print("You are too young to register...")
                information = input(f"Enter your {info}:>>> ")
            else:
                while info == "phone_number" and len(information) != 11:
                    print("Phone must be 11 digits")
                    information = input(f"Enter your {info}:>>> ")
        bet_balance = 0
        self.betbal.append(bet_balance)
        print(f"Registration complete... your username is {self.username} and your password is {self.pwd}")
        time.sleep(2)
        self.login()
   
    def login(self):
        username = input("Enter your username:>>>  ").strip().lower()
        passwd = input("Enter your password:>>>  ").strip().lower()
        if username == self.users[0] and passwd == self.password[0]:
            print("You have successfully logged in")
            self.homepage()
        else:
            print(" invalid details")
            self.login()

    def homepage(self):
        decision = input("Enter 1 to deposit money or 2 to play game: ")
        if decision == "1":
            self.deposit()
        elif decision == "2":
            self.play_game()
            
    def deposit(self):
        amount = int(input("Enter amount you want to deposit: >>> "))
        self.betbal[0] = self.betbal[0] + amount
        decision = input("if you haven't deposit, Enter 1 to deposit and 2 to go to homepage:>>> ")
        if decision == "1":
            self.deposit()
        elif decision == "2":
            self.homepage()
               
    def play_game(self):
        print("Instruction")
        decision = input("Do you wish to bet now?  Enter y to proceed:>>> ").lower()
        if decision == "y":
            if self.betbal[0] < 50:
                print("you do not have sufficient amount to bet")
                self.homepage()
            else: 
                self.betgame()
        else:
            self.homepage()

    def betgame(self):
        user_choice = []
        player_first = ['red', 'blue', 'green', 'gold', 'magenta']
        player_second = ['orange', 'yellow', 'pink', 'white', 'grey']
        player_third = ['black', 'skyblue', 'purple', 'green', 'indigo']
        count = 0
        machine = [random.choice(player_first), random.choice(player_second), random.choice(player_third)]
        for i in range(3):
            decision = input(f"Enter color {i + 1}: ")
            user_choice.append(decision)
        print(user_choice)
        for choice in user_choice:
            if choice in machine:
                count += 1
        print(machine)
        if count == 1:
            self.betbal[0] += 50
        elif count == 2:
            self.betbal[0] += 100
        elif count == 3:
            self.betbal[0] += 150
        else:
            self.betbal[0] -= 50 
        response = input(f"You are done with the game and your balance is {self.betbal[0]}. Enter 1 to replay and 2 to go home: ")
        if response == "1":
            self.betgame()
        else:
            self.homepage()
            
beet = betting()       
   
       

        

    # def register(self):
    #     self.customer = []
    #     details = ['firstname', 'lastname', 'age', 'address','phone_number']
    #     customer_num = input("Enter your customer number: ")
    #     for info in details:
    #         information = input(f"Enter your {info}:>>> ")
    #         if info == "lastname":
    #             self.customer.append(information)
    #             user = information[0:3]
    #             self.username = (f"{user}{random.randrange(100, 999)}")
    #             self.customer.append(self.username)
    #         else:
    #             while info == "age" and int(information) < 18:
    #                 print("You are not eligible to be registered!!")
    #                 information = input(f"Enter your {info}:>>> ")
    #             self.customer.append(information)
    #     password = (f"{self.customer[4][-4:]}")
    #     self.customer.append(password)
    #     self.users[customer_num] = self.customer
    #     # print(self.password)
    #     print(self.users)