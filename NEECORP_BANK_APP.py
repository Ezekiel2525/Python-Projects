import mysql.connector as connection
import random
import sys
import time
myconnect = connection.connect(host = "127.0.0.1", user = "root", password = "EzekielWorld1.", database = "ebank")
cursor = myconnect.cursor()

class Banking:

    def __init__(self):
        print("DEAR ESTEEMED CUSTOMER, WELCOME TO NEECORP GLOBAL ONLINE BANKING")
        print()
        time.sleep(2)
        self.welcome()

    def welcome(self):
        print("WHAT WILL YOU LIKE TO DO?")
        print()
        time.sleep(2)
        self.decision = input("1. Enter 1 TO  REGISTER\n2. Enter 2 TO LOG IN\n3. Enter 3 TO DEPOSIT\n4. Enter 4 To GO BACK\n5. Enter any key to exit :>>> ").strip()
        time.sleep(1)
        print()
        if self.decision == "1":
            print("Processing.....")
            time.sleep(1)
            self.register()
        elif self.decision == "2":
            print("Processing.....")
            time.sleep(1)
            self.login()
        elif self.decision == "3":
            print("Processing.....")
            time.sleep(1)
            self.deposit()
        elif self.decision == "4":
            print("Processing.....")
            time.sleep(1)
            self.welcome()
        else:
            print("Invalid input..Try again later!")
            sys.exit()
           
    def register(self):
        self.user_details = ["fname", "lname", "age", "Gender", "Address", "Phone_Number", "Email"]
        self.customer = []
        for info in self.user_details:
            self.information = input(f"Enter your {info}:>>> ").strip()
            while info == "Phone_Number" and len(self.information) != 11:
                print("Phone must be 11 digits")
                self.information = input(f"Enter your {info}:>>> ").strip()
            self.customer.append(self.information)
        Account_Number = self.customer[5][1:]
        self.customer.append(Account_Number)
        Bvn = random.randrange(1500200025, 5500450075)
        self.customer.append(Bvn)
        self.Account_Balance = 0
        self.customer.append(self.Account_Balance)
        self.password = self.customer[1][-3:] + str(random.randint(100, 999))
        self.customer.append(self.password)
        print(self.customer)
        print("Processing...")
        print()
        time.sleep(1)
        self.the_banks()
 
    def the_banks(self):
        print("THESE ARE THE BANKS AVAILABLE..\nBANK OF AMERICA(BOA)\nKUDA BANK\nOPAY MICROFINANCE BANK")
        self.decision = input("DEAR ESTEEMED CUSTOMER, WHICH OF THE BANKS WILL YOU LIKE TO OPEN?:>>> ").strip().lower()
        if self.decision == "boa":
            self.querry = "INSERT INTO boa(Fname, Lname, Age, Gender, Address, Phone_Number, Email, Account_Number, Bvn, Account_Balance, Password) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            print("Processing.....")
            time.sleep(1)
            print()
            self.verify()
        elif self.decision == "kuda":
            self.querry = "INSERT INTO kuda(Fname, Lname, Age, Gender, Address, Phone_Number, Email, Account_Number, Bvn, Account_Balance, Password) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            print("Processing.....")
            time.sleep(1)
            print()
            self.verify()
        elif self.decision == "opay":
            self.querry = "INSERT INTO opay(Fname, Lname, Age, Gender, Address, Phone_Number, Email, Account_Number, Bvn, Account_Balance, Password) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            print("Processing.....")
            time.sleep(1)
            print()
            self.verify()
        else:
            print("The bank you entered is not available")
            self.the_banks()

    def verify(self):
        self.val = tuple(self.customer,)
        cursor.execute(self.querry, self.customer)
        myconnect.commit()
        print("Processing...")
        time.sleep(2)
        print(f"REGISTRATION COMPLETE...THANKS FOR CHOOSING US😁!")
        self.login()

    def login(self):
        self.user = input("Enter your firstname:>>> ").lower().strip()
        self.password = input("Enter your password:>>> ")
        print()
        time.sleep(1)
        print("THESE ARE THE BANKS AVAILABLE..\nBANK OF AMERICA(BOA)\nKUDA BANK\nOPAY MICROFINANCE BANK")
        print()
        time.sleep(1)
        self.banking = input("DEAR ESTEEMED CUSTOMER, WHICH OF THE BANKS WILL YOU LIKE TO OPEN?:>>> ").strip().lower()
        if self.banking == "boa":
            self.userquerry = "SELECT * FROM boa WHERE Fname = %s"
            print("Processing...")
            time.sleep(1)
            self.confirm()
        elif self.banking == "kuda":
            self.userquerry = "SELECT * FROM kuda WHERE Fname = %s"
            print("Processing...")
            time.sleep(1)
            self.confirm()
        elif self.banking == "opay":
            self.userquerry = "SELECT * FROM opay WHERE Fname = %s"
            print("Processing...")
            time.sleep(1)
            self.confirm()
        else:
            self.login()
   
    def confirm(self):
        self.val = (self.user,)
        cursor.execute(self.userquerry, self.val)
        self.loginresult = cursor.fetchone()
        if self.loginresult:
            time.sleep(1)
            print("THESE ARE YOUR DETAILS")
            print()
            time.sleep(1)
            print(f"Your username is {self.loginresult[1]}\nYour password is {self.loginresult[11]}\nYour account number is {self.loginresult[8]}")
            # if self.user == self.loginresult[1] and self.password == self.loginresult[11]:
            print("Processing...")
            time.sleep(2)
            print("LOGIN SUCCESSFUL😁!")
            print()
            time.sleep(1)
            self.homepage()
        else:
            print("YOUR RECORD IS NOT IN OUR DATABASE...LOGIN FAILED...TRY AGAIN!😣")
            self.login()

    def homepage(self):
        self.decision = input("1. Enter 1 TO TRANSFER\n2. Enter 2 TO BUY AIRTIME\n3. Enter 3 TO BUY DATA\n4. Enter 4 TO PAY FOR UTILITY\n5. Enter 5 TO DEPOSIT MONEY\nEnter any key to Exit\n:>>>  ").strip()
        print()
        time.sleep(1)
        if self.decision == "1":
            print("Processing...")
            time.sleep(1)
            self.transfer()
        elif self.decision == "2":
            print("Processing...")
            time.sleep(1)
            self.buy_airtime()
        elif self.decision == "3":
            print("Processing...")
            time.sleep(1)
            self.buy_data()
        elif self.decision == "4":
            print("Processing...")
            time.sleep(1)
            self.pay()
        elif self.decision == "5":
            print("Processing...")
            time.sleep(1)
            self.deposit()
        else:
            print("THANKS FOR YOUR BANKING WITH US.. DO HAVE A NICE DAY!")
            sys.exit()

    def deposit(self):
        print("WELCOME DEAR ESTEEMED CUSTOMER")
        time.sleep(1)
        self.admin = input("Enter your Admin password:>>> ")
        while self.admin != "ame1776":
            print("Wrong Password!...Try again!")
            self.admin = input("Enter your Admin password:>>> ")          
        else:
            self.acct_num = input("Enter your account number: ")
            print()
            print("Processing...")
            time.sleep(1)
            print("CHOOSE A BANK TO DEPOSIT INTO;\nEnter 1 for BOA\nEnter 2 for KUDA\nEnter 3 for OPAY")
            print()
            self.banking = input("Which bank do you want to deposit into:>>> ").strip().lower()
            if self.banking == "1":
                self.query = "SELECT * FROM boa WHERE Account_Number = %s"
                self.querry = "UPDATE boa SET Account_Balance = %s WHERE Account_Number = %s"
                print("Processing...")
                time.sleep(1)
                self.confirmation()
            elif self.banking == "2":
                self.query = "SELECT * FROM kuda WHERE Account_Number = %s"
                self.querry = "UPDATE kuda SET Account_Balance = %s WHERE Account_Number = %s"
                print("Processing...")
                time.sleep(1)
                self.confirmation()
            elif self.banking == "3":
                self.query = "SELECT * FROM opay WHERE Account_Number = %s"
                self.querry = "UPDATE opay SET Account_Balance = %s WHERE Account_Number = %s"
                print("Processing...")
                time.sleep(1)
                self.confirmation()

    def confirmation(self):
        self.val = (self.acct_num,)
        cursor.execute(self.query, self.val)
        self.result = cursor.fetchone()
        print(self.result)
        if self.result:
            print(f"You are about to deposit money to {self.result[1]}")
            print()
            print("Processing...")
            time.sleep(1)
            self.amount = int(input("Enter the Amount you want to deposit:>>> "))
            self.new_amount = self.result[10] + self.amount
            print(self.new_amount)
            self.val = (self.new_amount, self.acct_num)
            cursor.execute(self.querry, self.val)
            myconnect.commit()
            print("Processing...")
            time.sleep(2)
            print(f"${self.amount} was successfully sent to {self.result[1]} and your new account balance is ${self.new_amount}")
            self.welcome()

        else:
            print("ACCOUNT NUMBER NOT FOUND😣!")
            self.deposit()

    def transfer(self):
        print("CHOOSE A BANK TO TRANSFER MONEY T0;\nENTER 1 FOR BOA\nENTER 2 FOR KUDA\nENTER 3 FOR OPAY")
        print()
        print("Processing...")
        time.sleep(1)
        self.choose_bank = input(">>> ")
        print()
        self.recipient = input("Enter the recipient's account number:>>> ")
        if self.choose_bank == "1":
            self.query = "SELECT * FROM boa WHERE Account_Number = %s"
            self.querry = "UPDATE boa SET Account_Balance = %s WHERE Account_Number = %s"
            while self.recipient == self.loginresult[8]:
                print("YOU ARE A MUMU PERSON..YOU CAN'T SEND MONEY TO YOURSELF! DAMN IT!!... DUMBO!!!😡")
                self.recipient = input("Enter the recipient's account number:>>> ")
            else:
                self.sent()
                
        elif self.choose_bank == "2":
            self.query = "SELECT * FROM kuda WHERE Account_Number = %s"
            self.querry = "UPDATE kuda SET Account_Balance = %s WHERE Account_Number = %s"
            while self.recipient == self.loginresult[8]:
                print("YOU ARE A MUMU PERSON..YOU CAN'T SEND MONEY TO YOURSELF! DAMN IT!!... DUMBO!!!😡")
                self.recipient = input("Enter the recipient's account number:>>> ")
            else:
                self.sent()
                
        elif self.choose_bank == "3":
            self.query = "SELECT * FROM opay WHERE Account_Number = %s"
            self.querry = "UPDATE opay SET Account_Balance = %s WHERE Account_Number = %s"
            while self.recipient == self.loginresult[8]:
                print("YOU ARE A MUMU PERSON..YOU CAN'T SEND MONEY TO YOURSELF! DAMN IT!!... DUMBO!!!😡")
                self.recipient = input("Enter the recipient's account number:>>> ")
            else:
                self.sent()
                
        else:
            print("ACOOUNT NUMBER NOT FOUND😣!")
            self.transfer()

    def sent(self):
        self.val = (self.recipient,)
        cursor.execute(self.query, self.val)
        self.find = cursor.fetchone()
        print(self.find)
        #we needed to change from self.result to self.find to avoid running into error 
        #cuz self.result will give the acct bal of the recipient
        if self.find:
            print(f"You are about to transfer money to {self.find[1]}")
            print()
            self.amount = int(input("Enter the Amount you want to Transfer:>>> "))
            while self.amount > self.loginresult[10]:
                #this is to check if the amount i want to send is bigger than what i have in my account balance.
                #self.loginresult[10] is the index of account balance on the table
                print("Insufficient funds!..Ogbeni, you no get enough kudi, no dey whine yourself!!😏")
                self.amount = int(input("Enter the Amount you want to Transfer:>>> "))
            else:
                self.new_amount1 = self.find[10] + self.amount
                #self.find[10] is the index of the account number on the table.
                self.newbalance = self.loginresult[10] - self.amount
                self.val = (self.new_amount1, self.recipient)
                cursor.execute(self.querry, self.val)
                myconnect.commit()
                self.deduct()
        
        else:
            print("NO RECORD OF THE ACCOUNT NUMBER YOU SUPPLIED!!.. TRY AGAIN")
            self.transfer()

    def deduct(self):
        if self.banking == "boa":
            self.querry = "UPDATE boa SET Account_Balance = %s WHERE Fname = %s"
            self.val = (self.newbalance, self.user)
            cursor.execute(self.querry, self.val)
            myconnect.commit()
        elif self.banking == "kuda":
            self.querry = "UPDATE kuda SET Account_Balance = %s WHERE Fname = %s"
            self.val = (self.newbalance, self.user)
            cursor.execute(self.querry, self.val)
            myconnect.commit()
        elif self.banking == "opay":
            self.querry = "UPDATE opay SET Account_Balance = %s WHERE Fname = %s"
            self.val = (self.newbalance, self.user)
            cursor.execute(self.querry, self.val)
            myconnect.commit()
        print("Processing...")
        time.sleep(2)
        print()
        print(f"You have successfully sent {self.amount} to {self.find[1]}, your new account balance is {self.newbalance}")
        time.sleep(2)
        self.choice = input("Enter 1 to perform transaction again or 2 to go back to home page or any other key to exit:>>> ")
        if self.choice == "1":
            self.transfer()
        elif self.choice == "2":
            self.homepage()
        else:
            print("Thanks for your Patronage")
            sys.exit()

    def buy_airtime(self):
        self.val = (self.user,)
        cursor.execute(self.userquerry, self.val)
        self.loginresult = cursor.fetchone()
        self.phone = input("ENTER YOUR PHONE NUMBER:>>> ")
        while len(self.phone) != 11:
            print("PHONE NUMBER MUST BE 11 DIGITS")
            self.phone = input("ENTER YOUR PHONE NUMBER:>>> ")
        else:
            self.net_provider = ["airtel", "glo", "mtn", "etisalat"]
            self.network = input("Enter network provider ").lower()
            if self.network in self.net_provider:
                print("HOW MUCH DO YOU WANT TO BUY?")
                print()
                self.amount = int(input("Enter the Amount you wish to purchase:>>> "))
                print("Processing...")
                time.sleep(1)
                if self.banking == "boa":
                    while self.loginresult[10] < self.amount:
                        #When you want to know the acct balance of a user, you use the initial result you fetched when u 
                        #logged in... if you used it elsewhere, you will have to change the variable
                        #i changed from result to loginresult, so as not to encounter errors
                        print("BROKE PERSON..YOU NO GET MONEY.. YOU WAN DEY SHOW..OYA RUN AM AGAIN")
                        self.amount = int(input("Enter the Amount you wish to purchase:>>> "))
                    else:
                        self.newbalance = self.loginresult[10] - self.amount
                        self.querry2 = "UPDATE boa SET Account_Balance = %s where Fname = %s"
                        self.affirm_airtime()                   
                        # self.val2 = (self.newbalance, self.loginresult[8])
                        # # in the querry above, any column can be updated with the account balance as far as the variable
                        # #you saved it with is the same as what is being used.. in this case, loginresult was used
                        # # to save the information when you fetched your details, so that is why it's being used with an index
                        # #of the account number on the sql workbench
                elif self.banking == "kuda":
                    while self.loginresult[10] < self.amount:
                        print("BROKE PERSON..YOU NO GET MONEY.. YOU WAN DEY SHOW..OYA RUN AM AGAIN")
                        self.amount = int(input("Enter the Amount you wish to purchase:>>> "))
                    else:
                        self.newbalance = self.loginresult[10] - self.amount
                        self.querry2 = "UPDATE kuda SET Account_Balance = %s where Fname = %s"
                        self.affirm_airtime()
                    
                elif self.banking == "opay":
                    while self.loginresult[10] < self.amount:
                        print("BROKE PERSON..YOU NO GET MONEY.. YOU WAN DEY SHOW..OYA RUN AM AGAIN")
                        self.amount = int(input("Enter the Amount you wish to purchase:>>> "))
                    else:
                        self.newbalance = self.loginresult[10] - self.amount
                        self.querry2 = "UPDATE opay SET Account_Balance = %s where Fname = %s"
                        self.affirm_airtime()   
                else:
                    print("THE BANK YOU ENTERED DOES NOT EXIST!")
                    self.buy_airtime()
            else:
                print("THE NETWORK PROVIDER YOU ENTERED DOES NOT EXIST...TRY ANOTHER NETWORK!")
                self.buy_airtime()
    
    def affirm_airtime(self):
        self.val2 = (self.newbalance, self.user)
        cursor.execute(self.querry2, self.val2)
        myconnect.commit()
        print(f"You have successfully purchased {self.amount} worth of {self.network} airtime")
        self.op()

    def op(self):
        self.choice = input("ENTER 1 TO PERFORM OPERATION AGAIN OR 2 TO GO TO HOMEPAGE:>>> ")
        print()
        print("Proceesing...")
        time.sleep(1)
        if self.choice == "1":
            self.buy_airtime()
        elif self.choice == "2":
            self.homepage()
        else:
            self.op()

    def buy_data(self):
        self.val = (self.user,)
        cursor.execute(self.userquerry, self.val)
        self.loginresult = cursor.fetchone()
        self.phone = input("ENTER YOUR PHONE NUMBER:>>> ")
        while len(self.phone) != 11:
            print("PHONE NUMBER MUST BE 11 DIGITS")
            self.phone = input("ENTER YOUR PHONE NUMBER:>>> ")
        else:
            time.sleep(1)
            self.dataplan = input("1. ENTER #300 FOR 1GB\n2. ENTER #500 FOR 2GB\n3. ENTER #1000 FOR 5GB:>>> ")
            print("Processing...")
            time.sleep(1)
            if self.dataplan == "1":
                self.plan = "MTN"
                self.amount = 300
                time.sleep(1)
            elif self.dataplan == "2":
                self.plan = "Airtel"
                self.amount = 500
                time.sleep(1)
            elif self.dataplan == "3":
                self.plan = "GlO"
                self.amount = 1000
                time.sleep(1)
            else:
                print("INVALID INPUT")
                self.buy_data()
            if self.loginresult[10] < self.amount:
                print("INSUFFICIENT BALANCE")
                self.buy_data()
            else:
                self.newbalance = self.loginresult[10] - self.amount
                if self.banking == "boa":     
                    self.querry = "UPDATE boa SET Account_Balance = %s WHERE Fname = %s"
                    self.affirm()
                elif self.banking == "kuda":
                    self.querry = "UPDATE kuda SET Account_Balance = %s WHERE Fname = %s"
                    self.affirm()
                elif self.banking == "opay":
                    self.querry = "UPDATE opay SET Account_Balance = %s WHERE Fname = %s"
                    self.affirm()
                else:
                    print("THE BANK YOU CHOSE IS NOT AVAILABLE...TRY AGAIN LATER")
                    self.buy_data()

    def affirm(self):
        self.val = (self.newbalance, self.user)
        cursor.execute(self.querry, self.val)
        myconnect.commit()
        print("Processing...")
        time.sleep(1)
        print(f"You have successfully purchased {self.amount} worth of {self.plan}")
        self.op2()

    def op2(self):
        self.choice = input("ENTER 1 TO PERFORM TRANSACTION AGAIN OR 2 TO GO TO HOMEPAGE:>>> ")
        print("Processing...")
        time.sleep(1)
        if self.choice == "1":
            self.buy_data()
        elif self.choice == "2":
            self.homepage()
        else:
            self.op2()


    def pay(self):
        print("Me: Good Morning, Mama Nkechi")
        time.sleep(2)
        print()
        print("Me: Which food do you have on your menu today?")
        print()
        time.sleep(2)
        self.food_items = ["Rice and Egg for #1000", "Beans and Bread for #1000", "Yam and Egg for #500"]
        time.sleep(2)
        print("Mama Nkechi: These are the food items we have on the menu")
        print()
        time.sleep(2)
        for index, food in enumerate(self.food_items, start=1):
            time.sleep(2)
            print(index, food)
        time.sleep(2)
        print("Mama Nkechi: Which one would you like?")
        print()
        time.sleep(2)
        self.foodchoice = input("ENTER YOUR CHOICE:>>> ").strip().lower()
        if self.foodchoice == "1":
            self.served = "RICE AND EGG"
            self.amount = 1000
            print()
            time.sleep(2)
            self.pay2()
        elif self.foodchoice == "2":
            self.served = "BEANS AND BREAD"
            self.amount = 1000
            print()
            time.sleep(2)
            self.pay2()
        elif self.foodchoice == "3":
            self.served = "YAM AND EGG"
            self.amount = 500
            print()
            time.sleep(2)
            self.pay2()
        else:
            print("YOU MUST BUY FOOD!!!")
            self.pay()

    def pay2(self):
        self.val = (self.user,)
        cursor.execute(self.userquerry, self.val)
        self.loginresult = cursor.fetchone()
        if self.loginresult[10] < self.amount:
            print("INSUFFICIENT BALANCE")
            self.pay()
        else:
            self.newbalance = self.loginresult[10] - self.amount
            if self.banking == "boa":
                self.querry = "UPDATE boa SET Account_Balance = %s WHERE Fname = %s"
                self.affirmpay()
            elif self.banking == "kuda":
                self.querry = "UPDATE kuda SET Account_Balance = %s WHERE Fname = %s"
                self.affirmpay()
            elif self.banking == "opay":
                self.querry = "UPDATE opay SET Account_Balance = %s WHERE Fname = %s"
                self.affirmpay()
            else:
                print("THE BANK YOU CHOSE IS NOT AVAILABLE...TRY AGAIN")
                self.pay2()

    def affirmpay(self):
        self.val = (self.newbalance, self.user)
        cursor.execute(self.querry, self.val)
        myconnect.commit()
        print("Processing...")
        time.sleep(1)
        print(f"YOU HAVE BOUGHT {self.served}")
        self.op3()
    
    def op3(self):
        self.decide = input("ENTER 1 BUY FOOD AGAIN OR 2 TO GO TO HOMEPAGE:>>> ")
        print("Processing...")
        time.sleep(1)
        if self.decide == "1":
            self.pay()
        elif self.decide == "2":
            self.homepage()
        else:
            self.op3()           
Banking()




































# while self.phone_number != 11:
#                     print("IDIOT! YOU NO EVEN SABI YOUR PHONE NUMBER!..E BE LIKE SAY YOU THIEF THIS PHONE..OYA TYPE THE NUMBER AGAIN")
#                     self.phone_number = input("ENTER YOUR PHONE NUMBER:>>> ")
#                 else:
#                     print("HOW MUCH DO YOU WISH TO BUY?")
#                     self.amount = int(input("ENTER THE AMOUNT YOU WISH TO PURCHASE:>>> "))
#                     if self.banking == "boa":
#                         while self.loginresult[10] < self.amount:
#                             print("BROKE PERSON..YOU NO GET MONEY.. YOU WAN DEY SHOW..OYA PACK IT UP")
#                             self.amount = int(input("Enter the Amount you wish to purchase:>>> "))
#                         else:
#                             self.newbalance = self.loginresult[10] - self.amount
#                             self.querry2 = "UPDATE boa SET Account_Balance = %s where Account_Number = %s"
#                             self.val2 = (self.newbalance, self.loginresult[8])
#                             cursor.execute(self.querry2, self.val2)
#                             myconnect.commit()
#                             print(f"You have successfull purchase {self.amount} worth of {self.network} card")
#                     elif self.banking == "kuda":
#                         while self.loginresult[10] < self.amount:
#                             print("BROKE PERSON..YOU NO GET MONEY.. YOU WAN DEY SHOW..OYA PACK IT UP")
#                             self.amount = int(input("Enter the Amount you wish to purchase:>>> "))
#                         else:
#                             self.newbalance = self.loginresult[10] - self.amount
#                             self.querry2 = "UPDATE kuda SET Account_Balance = %s where Account_Number = %s"
#                             self.val2 = (self.newbalance, self.loginresult[8])
#                             cursor.execute(self.querry2, self.val2)
#                             myconnect.commit()
#                             print(f"You have successfull purchase {self.amount} worth of {self.network} card")
#                     elif self.banking == "opay":
#                         while self.loginresult[10] < self.amount:
#                             print("BROKE PERSON..YOU NO GET MONEY.. YOU WAN DEY SHOW..OYA PACK IT UP")
#                             self.amount = int(input("Enter the Amount you wish to purchase:>>> "))
#                         else:
#                             self.newbalance = self.loginresult[10] - self.amount
#                             self.querry2 = "UPDATE opay SET Account_Balance = %s where Account_Number = %s"
#                             self.val2 = (self.newbalance, self.loginresult[8])
#                             cursor.execute(self.querry2, self.val2)
#                             myconnect.commit()
#                             print(f"You have successfull purchase {self.amount} worth of {self.network} card")
#                             self.op()
#                     else:
#                         print("THE BANK YOU ENTERED DOES NOT EXIST!")
#                         self.buy_data()


 # def deposit(self):
    #     self.admin = input("Enter your Admin password:>>> ")
    #     if self.admin != "ame1776":
    #         print("Wrong Password!...Try again!")
    #         self.deposit()
    #     else:
    #         self.acct_num = input("Enter your account number: ")
    #         self.banking = input("Which bank do you want:>>> ").strip().lower()
    #         if self.banking == "boa":
    #             self.querry = "SELECT * FROM boa WHERE Account_Number = %s"
    #             self.confirmation()
    #             self.sendboa()
    #         elif self.banking == "kuda":
    #             self.querry = "SELECT * FROM kuda WHERE Account_Number = %s"
    #             self.confirmation()
    #             self.sendkuda()
    #         elif self.banking == "opay":
    #             self.querry = "SELECT * FROM opay WHERE Account_Number = %s"
    #             self.confirmation()
    #             self.sendopay()
    #         else:
    #             print("The bank you entered is not available!")
    #             self.deposit()

    # def confirmation(self):
    #     self.val = (self.acct_num,)
    #     cursor.execute(self.querry, self.val)
    #     self.result = cursor.fetchone()
    #     print(self.result)

    # def sendboa(self):
    #     if self.result:
    #         print("ACCOUNT NUMBER IS AVAILABLE!")
    #         self.amount = int(input("Enter Amount you want to deposit:>>> "))
    #         self.newbal = self.result[10] + self.amount
    #         self.querry = "UPDATE boa SET Account_Balance = %s where Account_Number = %s"
    #         self.val = (self.newbal, self.acct_num)
    #         cursor.execute(self.querry, self.val)
    #         myconnect.commit()
    #         print(self.acct_num)
    #         print(f"You have successfully deposited ${self.amount} into the account number {self.acct_num} and the new balance is {self.newbal}")
    #         self.choice = input("Enter\n1. To perform transaction again\n2. To Homepage\nAnd any other key to quit\n:>>> ")
    #         if self.choice == "1":
    #             self.deposit()
    #         elif self.choice == "2":
    #             self.homepage()
    #         else:
    #             sys.exit()

    #     else:
    #         print("Account not found!")
    #         self.deposit()

    # def sendkuda(self):
    #     if self.result:
    #         print("ACCOUNT NUMBER IS AVAILABLE!")
    #         self.amount = int(input("Enter Amount you want to deposit:>>> "))
    #         self.newbal = self.result[10] + self.amount
    #         self.querry = "UPDATE kuda SET Account_Balance = %s where Account_Number = %s"
    #         self.val = (self.newbal, self.acct_num)
    #         cursor.execute(self.querry, self.val)
    #         myconnect.commit()
    #         print(f"You have successfully deposited ${self.amount} into the account number {self.acct_num} and the new balance is {self.newbal}")
    #         self.choice = input("Enter\n1. To perform transaction again\n2. To Homepage\nAnd any other key to quit\n:>>> ")
    #         if self.choice == "1":
    #             self.deposit()
    #         elif self.choice == "2":
    #             self.homepage()
    #         else:
    #             sys.exit()

    #     else:
    #         print("Account not found!")
    #         self.deposit()

    # def sendopay(self):
    #     if self.result:
    #         print("ACCOUNT NUMBER IS AVAILABLE!")
    #         self.amount = int(input("Enter Amount you want to deposit:>>> "))
    #         self.newbal = self.result[10] + self.amount
    #         self.querry = "UPDATE opay SET Account_Balance = %s where Account_Number = %s"
    #         self.val = (self.newbal, self.acct_num)
    #         cursor.execute(self.querry, self.val)
    #         myconnect.commit()
    #         print(f"You have successfully deposited ${self.amount} into the account number {self.acct_num} and the new balance is {self.newbal}")
    #         self.choice = input("Enter\n1. To perform transaction again\n2. To Homepage\nAnd any other key to quit\n:>>> ")
    #         if self.choice == "1":
    #             self.deposit()
    #         elif self.choice == "2":
    #             self.homepage()
    #         else:
    #             sys.exit()

    #     else:
    #         print("Account not found!")
    #         self.deposit()

















