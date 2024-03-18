import mysql.connector as connection
import time
import sys
import re
import random
myconnect = connection.connect(host = "127.0.0.1", user = "root", password = "EzekielWorld1.", database = "e_banking")
cursor = myconnect.cursor()

class Ebanking:

    def __init__(self):
        print("DEAR CUSTOMER, WELCOME TO NEECORP INTERNET BANKING, WHERE WE OFFER THE BEST SERVICES IN THE UNIVERSE")
        time.sleep(2)
        print()
        self.online_staus = False
        self.welcome()

    def welcome(self):
        self.choose = input("ENTER 1 TO REGISTER\nENTER 2 TO LOG IN\nENTER 3 TO DEPOSIT\nENTER 4 TO GO BACK TO OPTIONS\nENTER ANY KEY TO EXIT\n>>> ").strip()
        if self.choose == "1":
            self.register()
        elif self.choose == "2":
            self.login()
        elif self.choose == "3":
            self.deposit()
        elif self.choose == "4":
            self.welcome()
        else:
            print("THANKS FOR YOUR PATRONAGE..DO HAVE A NICE DAY!")
            sys.exit()
        
    def register(self):
        self.banks = ["access", "gtb", "zenith"]
        self.banking = input(f"THESE ARE THE BANKS AVAILABLE\n{self.banks}\nWHICH OF THE BANKS WILL YOU LIKE TO BE REGISTERED TO\n>>> ").strip().lower()
        if self.banking in self.banks:
            self.customer = []
            self.details = ["Surname", "Lastname", "Age", "Address", "Email", "Phone_Number", "Gender"]
            for info in self.details:
                self.information = input(f"ENTER YOUR {info}\n>>>  ").strip().lower()
                while info == "Email":
                    reg = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[. ]\w{2,3}$"
                    if not re.findall(reg, self.information):
                        print("INVALID EMAIL..PLEASE TRY A VALID EMAIL")
                        self.information = input(f"ENTER YOUR {info}\n>>>  ").strip().lower()
                    else:
                        print("EMAIL IS VALID")
                        break
                else:
                    while info == "Phone_Number" and len(self.information) != 11:
                        print("PHONE NUMBER MUST BE 11 DIGITS..PLEASE TRY AGAIN!")
                        self.information = input(f"ENTER YOUR {info}\n>>>  ").strip().lower()
                self.customer.append(self.information)
            self.username = self.customer[1][0:4] + str(random.randint(10, 99))
            self.customer.append(self.username)
            self.password = self.customer[0][0:3] + str(random.randint(0, 50))
            self.customer.append(self.password)
            self.bvn = random.randrange(100000000, 900000000)
            self.customer.append(self.bvn)
            self.acct_num = random.randrange(1250000000, 9550000000)
            self.customer.append(self.acct_num)
            self.acctbal = 0
            self.customer.append(self.acctbal)
            print(self.customer)
            self.query = f"INSERT IGNORE INTO {self.banking} (Surname, Lastname, Age, Address, Email, Phone_Number, Gender, Username, Password, Bvn, Account_number, Account_balance)VALUES({'%s'}, {'%s'}, {'%s'},{'%s'}, {'%s'}, {'%s'}, {'%s'}, {'%s'}, {'%s'}, {'%s'}, {'%s'}, {'%s'})"
            self.val = tuple(self.customer)
            cursor.execute(self.query, self.val)
            myconnect.commit()
            print("PROCESSING...")
            time.sleep(2)
            print()
            print(f"DEAR {self.customer[0].upper()} {self.customer[1].upper()}, YOUR REGISTRATION WAS SUCCESSFUL!, YOU ARE NOW A CUSTOMER OF {self.banking.upper()} ")
            print()
            time.sleep(1)
            print(f"THESE ARE YOUR DETAILS\nYOUR USERNAME IS {self.customer[7]}\nYOUR PASSWORD IS {self.customer[8]}")
            print()
            time.sleep(1)
            print("PROCEED TO LOG IN")
            self.login()
        else:
            print(f"THE BANK {self.banking.upper()} YOU CHOSE IS NOT AVAILABLE...PLEASE CHOOSE AMONG THE BANKS AVAILABLE WHICH ARE {self.banks}")
            print()
            self.register()

    def login(self):
        #you have to choose the bank to log into because there are three banks with three different customers..entering the right details to a wrong bank will lead to error
        print()
        self.banks = ["access", "gtb", "zenith"]
        self.bbanking = input(f"THESE ARE THE BANKS AVAILABLE\n{self.banks}\nWHICH OF THE BANKS WILL YOU LIKE TO LOG INTO\n>>> ").strip().lower()
        if self.bbanking in self.banks:
            self.user = input("ENTER YOUR USERNAME\n>>> ").strip().lower()
            print()
            self.password = input("ENTER YOUR PASSWORD\n>>> ").strip().lower()
            print()
            self.userquerry = f"SELECT * FROM {self.bbanking} WHERE Username = {'%s'} and Password = {'%s'}"
            self.confirm()
        else:
            print(f"{self.banking.upper()} BANK IS NOT AVAILABLE..PLEASE ENTER THE BANKS THAT ARE AVAILABLE")
            print()
            self.login()

    def confirm(self):
        self.uval = (self.user, self.password)
        cursor.execute(self.userquerry, self.uval)
        self.loginresult = cursor.fetchone()
        if self.loginresult is not None:
                print("PROCESSING...")
                time.sleep(2)
                print()
                print(f"DEAR {self.user.upper()}, YOU HAVE LOGGED IN SUCCESSFULLY.")
                self.online_staus = True
                self.homepage()
        else:
            print("LOGIN FAILED!!...YOU HAVE NO RECORD ON OUR DATABASE...PLEASE GO TO THE MAIN PAGE TO REGISTER OR ENTER YOUR CORRECT LOG IN DETAILS")
            self.welcome()
    
    def homepage(self):
        self.operation = input("ENTER 1 TO TRANSFER\nENTER 2 TO BUY DATA\nENTER 3 TO BUY AIRTIME\nENTER 4 TO PAY FOR UTILITIES\nENTER 5 TO GO TO MAIN PAGE\n>>> ").strip()
        if self.operation == "1":
            self.transfer()
        elif self.operation == "2":
            self.buy_data()
        elif self.operation == "3":
            self.buy_airtime()
        elif self.operation == "4":
            self.pay_utilities()
        elif self.operation == "5":
            self.welcome()
        else:
            self.homepage() 

    def deposit(self):
        print("AS AN ADMIN, YOU CAN ONLY HAVE 3 ATTEMPTS TO ENTER YOUR PASSWORD")
        print()
        self.count = 0
        self.limit = 3
        while self.count < self.limit:
            self.admin = input("ENTER THE ADMIN PASSWORD\n>>> ").strip().lower()
            print()
            if self.admin == "ame246":
                print("PASSWORD CORRECT")
                self.confirm_2()
            else:
                print("WRONG PASSWORD..IF YOU EXCEED YOUR ATTEMPTS YOU WILL HAVE TO WAIT FOR 10SECS TO ENTER IT AGAIN..SO ENTER THE CORRECT PASSWORD")
                # self.admin = input("ENTER THE ADMIN PASSWORD\n>>> ").strip().lower()
                self.count += 1                                    
        else:
            print("YOU HAVE EXCEEDED YOUR ATTEMPTS YOU WILL HAVE TO WAIT FOR 10SECS TO ENTER IT AGAIN!")
            print() 
            time.sleep(10)
            self.deposit()

    def confirm_2(self):
        #you have to choose the bank to DEPOSIT into because there are three banks with three different customers..entering the right details to a wrong bank will lead to error
        self.banks = ["access", "gtb", "zenith"]
        self.cbanking = input(f"THESE ARE THE BANKS AVAILABLE\n{self.banks}\nWHICH OF THE BANKS WILL YOU LIKE TO DEPOSIT MONEY INTO\n>>> ").strip().lower()
        if self.cbanking in self.banks:
            self.acct_num = input("ENTER YOUR ACCOUNT NUMBER\n>>> ").strip()
            self.squery = f"SELECT * FROM {self.cbanking} WHERE Account_number = {'%s'}"
            self.uquery = f"UPDATE {self.cbanking} SET Account_balance = {'%s'} WHERE Account_number = {'%s'}"
            self.val = (self.acct_num,)
            cursor.execute(self.squery, self.val)
            self.result = cursor.fetchone()
            if self.result is not None:
                print("PROCESSING...")
                time.sleep(1)
                print()
                print(f"YOU ARE ABOUT TO DEPOSIT MONEY TO {self.result[1].upper()} {self.result[2].upper()}")
                self.amount = int(input("ENTER THE AMOUNT YOU WANT TO DEPOSIT\n>>> "))
                self.new_amount = self.result[12] + self.amount
                self.val = (self.new_amount, self.acct_num)
                cursor.execute(self.uquery, self.val)
                myconnect.commit()
                print("PROCESSING")
                print()
                time.sleep(2)
                print(f"${self.amount} WAS SUCCESSFULLY SENT TO {self.result[1].upper()} AND YOUR NEW ACCOUNT BALANCE IS ${self.new_amount}")
                self.welcome()
            else:
                print("ACCOUNT NUMBER NOT FOUND...PLEASE TRY AGAIN")
                self.deposit()
        else:
            print(f"{self.bbanking.upper()} BANK IS NOT AVAILABLE..PLEASE ENTER THE BANKS THAT ARE AVAILABLE")
            print()
            self.confirm_2()
    
    def transfer(self):
        self.uval = (self.user,self.password)
        cursor.execute(self.userquerry, self.uval)
        self.loginresult = cursor.fetchone()
        self.banks = ['access', 'gtb', 'zenith']
        self.banking = input(f"WHICH OF THESE BANKS DO YOU WANT TO TRANSFER MONEY TO\n{self.banks}\n>>> ").strip()
        if self.banking in self.banks:
           self.recipient = input("ENTER THE RECIPIENT'S ACCOUNT NUMBER\n>>> ")
           print()
           while self.recipient == self.loginresult[11]:
               print("YOU CAN'T SEND MONEY TO YOURSELF...")
               print()
               self.recipient = input("ENTER THE RECIPIENT'S ACCOUNT NUMBER\n>>> ")
           else:
               self.tquery = f"SELECT * FROM {self.banking} WHERE Account_number = {'%s'}"
               self.val = (self.recipient,)
               cursor.execute(self.tquery, self.val)
               self.find = cursor.fetchone()
               print(self.find)
               self.sent()
        else:
           print(f"{self.banking.upper()} BANK IS NOT AVAILABLE..PLEASE ENTER AN AVAILABLE BANK")
           print()
           self.transfer()
              
    def sent(self):
        if self.find is not None:
            self.amount = int(input("ENTER THE AMOUNT YOU WISH TO TRANSFER\n>>> "))
            print()
            while self.amount > self.loginresult[12]:
                print("DEAR CUSTOMER, YOU DO NOT HAVE SUFFICIENT FUNDS TO CARRY OUT THIS TRANSACTION..PLEASE TRY AGAIN")
                print()
                self.amount = int(input("ENTER THE AMOUNT YOU WISH TO TRANSFER\n>>> "))
            else:
                time.sleep(1)
                print(f"YOU ARE ABOUT TO SEND MONEY TO {self.find[1].upper()} {self.find[2].upper()}")
                self.newamt = self.find[12] + self.amount
                self.newbalance = self.loginresult[12] - self.amount
                self.tuquery = f"UPDATE {self.banking} SET Account_balance = {'%s'} WHERE Account_number = {'%s'}"
                self.val1 = (self.newamt, self.recipient)
                cursor.execute(self.tuquery, self.val1)
                myconnect.commit()
                self.deduct()
        else:
            print("ACCOUNT NOT FOUND")

    def deduct(self):
        self.dquery = f"UPDATE {self.bbanking} SET Account_balance = {'%s'} WHERE Username = {'%s'}"
        self.val2 = (self.newbalance, self.user)
        cursor.execute(self.dquery, self.val2)
        myconnect.commit()
        print()
        print("PROCESSING...")
        time.sleep(2)
        print(f"YOU HAVE SUCCESSFULLY TRANSFERRED ${self.amount} TO {self.find[1].upper()} {self.find[2].upper()} AND YOUR NEW ACCOUNT BALANCE IS ${self.newbalance}")
        self.opt()

    def opt(self):
        print()
        time.sleep(1)
        self.choice = input("ENTER 1 TO PERFORM ANOTHER TRANSACTION\nENTER 2 TO GO TO HOMEPAGE\nENTER ANY KEY TO GO BACK TO THE MAINPAGE\n>>> ")
        if self.choice == "1":
            self.transfer()
        elif self.choice == "2":
            self.homepage()
        else:
            self.welcome()

    def buy_data(self):
        self.uval = (self.user,self.password)
        cursor.execute(self.userquerry, self.uval)
        self.loginresult = cursor.fetchone()
        self.phone = input("ENTER YOUR PHONE NUMBER\n>>> ")
        while len(self.phone) != 11:
            print("PHONE NUMBER MUST BE 11 DIGITS")
            print()
            self.phone = input("ENTER YOUR PHONE NUMBER\n>>> ")
        else: 
            self.network_provider = ['mtn', 'glo', 'airtel', '9mobile']
            self.network = input(f"THESE ARE THE NETWORKS AVAILABLE\n{self.network_provider}\nENTER THE NETWORK YOU WISH TO PURCHASE\n>>> ").strip()
            if self.network in self.network_provider:
                self.dataplan = input("1. ENTER #300 FOR 1GB\n2. ENTER #500 FOR 2GB\n3. ENTER #1000 FOR 5GB\n>>> ")
                if self.dataplan == "1":
                    self.amount = 300
                    self.affirm()
                elif self.dataplan == "2":
                    self.amount = 500
                    self.affirm()
                elif self.dataplan == "3":
                    self.amount = 1000
                    self.affirm()
                else:
                    print("INVALID INPUT")
                    self.buy_data()
            else:
                print("THE NETWORK YOU ENTERED IS NOT AVAILABLE")
                self.buy_data()

    def affirm(self):
        if self.bbanking:
                while self.loginresult[12] < self.amount:
                    print("INSUFFICIENT BALANCE")
                    self.buy_data()
                else:
                    self.new_amount2 = self.loginresult[12] - self.amount
                    self.bdquery = f"UPDATE {self.bbanking} SET Account_balance = {'%s'} WHERE Username = {'%s'}"
                    self.fval = (self.new_amount2, self.user)
                    cursor.execute(self.bdquery, self.fval)
                    myconnect.commit()
                    print("PROCESSING...")
                    print()
                    time.sleep(2)
                    print(f"YOU HAVE SUCCESSFULLY PURCHASED ${self.amount} WORTH OF {self.network.upper()} DATA AND YOUR ACCOUNT BALANCE IS ${self.new_amount2}")
                    print()
                    time.sleep(1)
                    self.choice = input("ENTER 1 TO PERFORM ANOTHER TRANSACTION\nENTER 2 TO GO TO HOMEPAGE\nENTER ANY KEY TO GO BACK TO THE MAINPAGE\n>>> ")
                    if self.choice == "1":
                        self.buy_data()
                    elif self.choice == "2":
                        self.homepage()
                    else:
                        self.welcome()
        else:
            self.buy_data()

    def buy_airtime(self):
        self.uval = (self.user,self.password)
        cursor.execute(self.userquerry, self.uval)
        self.loginresult = cursor.fetchone()
        self.phone = input("ENTER YOUR PHONE NUMBER\n>>> ")
        while len(self.phone) != 11:
            print("PHONE NUMBER MUST BE 11 DIGITS")
            print()
            self.phone = input("ENTER YOUR PHONE NUMBER\n>>> ")
        else: 
            self.network_provider = ['mtn', 'glo', 'airtel', '9mobile']
            self.network = input("ENTER THE NETWORK YOU WISH TO PURCHASE\n>>> ").strip()
            if self.network in self.network_provider:
                self.amount = int(input("ENTER THE AMOUNT\n>>> "))
                if self.bbanking:
                    while self.amount > self.loginresult[12]:
                        print("INSUFFICIENT FUNDS")
                        self.amount = int(input("ENTER THE AMOUNT\n>>> "))
                    else:
                        self.newbal = self.loginresult[12] - self.amount
                        self.bquery = f"UPDATE {self.bbanking} SET Account_balance = {'%s'} WHERE Username = {'%s'}"
                        self.affirm2()
            else:
                print("THE NETWORK YOU ENTERED IS NOT AVAILABLE")
                self.buy_airtime()         

    def affirm2(self):
        self.vali = (self.newbal, self.user)
        cursor.execute(self.bquery, self.vali)
        myconnect.commit()
        print("PROCESSING...")
        print()
        time.sleep(2)
        print(f"DEAR {self.loginresult[1].upper()}, YOU HAVE SUCCESSFULLY PURCHASED ${self.amount} WORTH OF AIRTIME AND YOUR ACCOUNT BALANCE IS ${self.newbal}")
        print()
        time.sleep(1)
        self.choice = input("ENTER 1 TO PERFORM ANOTHER TRANSACTION\nENTER 2 TO GO TO HOMEPAGE\nENTER ANY KEY TO GO BACK TO THE MAINPAGE\n>>> ")
        if self.choice == "1":
            self.buy_airtime()
        elif self.choice == "2":
            self.homepage()
        else:
            self.welcome()
 
    def pay_utilities(self):
        self.uval = (self.user,self.password)
        cursor.execute(self.userquerry, self.uval)
        self.loginresult = cursor.fetchone()
        self.utility = ["gotv", "dinner", "car-repair"]
        self.decide = input(f"THESE ARE THE UTILITIES WE WANT TO PAY FOR\n{self.utility}\nENTER THE ONE YOU WISH TO PAY FOR\n>>> ")
        if self.decide in self.utility:
            self.amount = int(input("ENTER THE AMOUNT TO PAY\n>>> "))
            while self.amount > self.loginresult[12]:
                print("INSUFFICIENT FUNDS!")
                print()
                self.amount = int(input("ENTER THE AMOUNT TO PAY\n>>> "))
            else:
                self.affirm3()
        else:
            print("THE UTILITY YOU ENTERED IS NOT ON THE LIST")
            self.pay_utilities()

    def affirm3(self):
        if self.bbanking:
            self.nwamount = self.loginresult[12] - self.amount
            self.paquery = f"UPDATE {self.bbanking} SET Account_balance = {'%s'} WHERE Username = {'%s'}"
            self.pval = (self.nwamount, self.user)
            cursor.execute(self.paquery, self.pval)
            myconnect.commit()
            print("PROCESSING...")
            print()
            time.sleep(2)
            print(f"DEAR {self.loginresult[1].upper()} {self.loginresult[2].upper()} YOU HAVE SUCCESSFULLY PAID FOR {self.decide.upper()} AND YOUR NEW ACCOUNT BALANCE IS ${self.nwamount}")
            print()
            time.sleep(1)
            self.choice = input("ENTER 1 TO PERFORM ANOTHER TRANSACTION\nENTER 2 TO GO TO HOMEPAGE\nENTER ANY KEY TO GO BACK TO THE MAINPAGE\n>>> ")
            if self.choice == "1":
                self.pay_utilities()
            elif self.choice == "2":
                self.homepage()
            else:
                self.welcome()
        else:
            self.pay_utilities()

        

           
                





        
























                
     



               
        
                
                    
               
 



Ebanking()

