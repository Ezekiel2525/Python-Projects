import mysql.connector as connection
import time
import random
import sys
myconnect = connection.connect(host = "127.0.0.1", user = "root", password = "EzekielWorld1.", database = "supermarket")
cursor = myconnect.cursor()

class Shopping_mall:

    def __init__(self):
        print("BOT: DEAR VALUED CUSTOMER, WELCOME TO NEECORP SHOPPING MALL, THE BIGGEST ONLINE SHOPPING MALL IN THE UNIVERSE.")
        print()
        time.sleep(2)
        self.customers = []
        self.cart = {}
        self.cart_product = {}
        self.prices = {}
        self.online_status = False
        self.user_details = ["Firstname", "Lastname", "Age", "Gender", "Email", "Address", "Phone_Number"]
        self.homepage()

#this is the homepage where we begin the function
    def homepage(self):
        print("BOT: HOW MAY I BE OF SERVICE TO YOU?")
        print()
        time.sleep(2)
        self.choice = input("ENTER 1 TO REGISTER\nENTER 2 TO LOG IN\nENTER 3 TO ADD TO CART\nENTER 4 TO CHECKOUT\nENTER ANY OTHER KEY TO EXIT\n>>> ")
        if self.choice == "1":
            self.register()
        elif self.choice == "2":
            self.login()
        elif self.choice == "3":
            self.add()
        elif self.choice == "4":
            self.checkout()
        else:
            print("DEAR VALUED CUSTOMER, THANKS FOR YOUR PATRONAGE..DO HAVE A NICE DAY")
            sys.exit()

##this is the registration function
    def register(self):
        for info in self.user_details:
            self.information = input(f"Enter your {info}:>>> ").strip().upper()
            while info == "Phone_Number" and len(self.information) != 11:
                print("Phone must be 11 Digits...Try Again!")
                self.information = input(f"Enter your {info}:>>> ").strip().lower()
            self.customers.append(self.information)
        self.username = self.customers[0][0:3] + str(random.randrange(10,99))
        self.customers.append(self.username)
        self.password = self.customers[1][0:3] + str(random.randrange(10,99))
        self.customers.append(self.password)
        self.query = "INSERT INTO users (Fname, Lname, Age, Gender, Email, Address, Phone_Number, Username, Password)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        print()
        print()
        time.sleep(2)
        print("PROCESSING...")
        time.sleep(2)
        print()
        print(f"DEAR {self.customers[0]} {self.customers[1]}, YOUR REGISTRATION IS COMPLETE AND SUCCESSFUL ")
        self.verify()

    def verify(self):
        self.val = tuple(self.customers)
        cursor.execute(self.query, self.val)
        myconnect.commit()
        print("THESE ARE YOUR DETAILS")
        print()
        time.sleep(2)
        print(f"Your username is {self.customers[7]}\nYour password is {self.customers[8]}")
        print()
        print("PROCEED TO LOGIN")
        print()
        self.login()
#this is the login function
    def login(self):
        self.username = input("ENTER YOUR USERNAME:>>> ").strip().upper()
        print()
        self.password = input("ENTER YOUR PASSWORD:>>> ").strip().upper()
        self.querry = "SELECT * FROM users WHERE Username = %s and Password = %s"
        self.val = (self.username, self.password)
        cursor.execute(self.querry, self.val)
        self.result = cursor.fetchone()
        # print(self.result)
        if self.result:
            if self.username == self.result[8] and self.password == self.result[9]:
                print("LOADING....")
                time.sleep(2)
                print()
                print(f"YOU HAVE SUCCESSFULLY LOGGED IN {self.username}")
                self.online_status = True
                #this means you have been logged in and your online status is true
                print()
                self.decide = input("SALES-BOT:\nENTER 1 TO CHECKOUT\nENTER 2 TO SHOP FOR ITEMS\nENTER ANY OTHER KEY TO LOG-OUT\n>>> ")
                if self.decide == "1":
                    self.checkout()
                elif self.decide == "2":
                    self.add()
                else:
                    self.online_status = False
                    #this means you have already logged out and your online status is false
                    print()
                    print("THANKS FOR YOUR PATRONAGE...WE HOPE YOU WERE SATISFIED WITH OUR SERVICES...GOODBYE!")
                    self.homepage()
            
            else:
                print("INVALID DETAILS...CHECK THAT YOUR USERNAME OR PASSWORD IS ENTERED CORRECTLY")
                self.login()
        else:
            print("NO RECORDS OF YOUR DETAILS ON OUR DATABASE!")
            print()
            time.sleep(1)
            self.choose = input("SALES-BOT:\nENTER 1 TO RETRY AGAIN\nENTER 2 TO REGISTER\nAND ANY OTHER KEY TO LOG-OUT\n>>> ")
            #this means that you can either be a user or you are about to be register on the website
            if self.choose == "1":
                self.login()
            elif self.choose == "2":
                self.register()
            else:
                self.online_status = False
                #this means you have already logged out and your online status is false
                self.homepage()

#this is the collection function
    def add(self):
        print("SALES-BOT: WELCOME TO OUR ONLINE COLLECTION")
        print()
        time.sleep(1)
        self.collection = ["computers", "cooking", "drinks", "appliances", "toiletries", "fashion"]
        print(f"SALES-BOT:\nTHESE ARE THE COLLECTIONS WE HAVE\n{self.collection}")
        print()
        time.sleep(1)
        self.select = input("SALES-BOT:\nENTER THE COLLECTION YOU WILL LIKE TO SHOP FROM\n>>> ").strip().lower()
        print()
        print("LOADING...")
        time.sleep(1)
        if self.select in self.collection:
            if self.select == "fashion":
                print()
                time.sleep(1)
                self.select = input("SALES-BOT:\nWHICH WOULD YOU LIKE TO CHOOSE FROM (MEN OR WOMEN)\n>>> ").strip().upper()
                print()
                time.sleep(1)
                if self.select != "MEN" and self.select != "WOMEN":
                    print()
                    print("CATEGORY DOES NOT EXIST")
                    self.add()
            self.cartquerry = f"SELECT Product FROM {self.select}"
            cursor.execute(self.cartquerry,)
            self.find = cursor.fetchall()
            print()
            time.sleep(1)
            print(f"SALES-BOT:\n{self.find}\nARE THE PRODUCTS WE HAVE UNDER THE COLLECTION\n{self.select}")
            print()
            time.sleep(1)
            #self.find will fetch all the products in the specified column
            self.additem()
        else:
            print("COLLECTION DOES NOT EXIST")
            self.add()

    def additem(self):
        self.productchoice = input("SALES-BOT: ENTER THE PRODUCT NAME YOU WISH TO PURCHASE:>>> ").strip().upper()
        print()
        print("LOADING...")
        time.sleep(2)
        self.prodquery = f"SELECT * FROM {self.select} WHERE Product = {'%s'}"
        #we aim to fetch the product details
        self.val = (self.productchoice,)
        cursor.execute(self.prodquery, self.val)
        self.res = cursor.fetchone()
        # print(self.res)
        if self.res:
            print(f"THE CURRENT PRICE OF {self.productchoice.upper()} is #{self.res[3]} PER ONE\nAND WE HAVE {self.res[2]} left in our stock")
            print()
            time.sleep(2)
            print(f"BOT: IF YOU PURCHASE 10 ITEMS AND ABOVE FROM OF STOCK\nWE WILL GIVE YOU A 10% DISCOUNT ON EVERY ITEMS PURCHASED\nHOW MANY {self.productchoice.upper()} ITEMS WILL YOU LIKE FROM OUR STOCK?")
            print()
            time.sleep(2)
            self.qty = int(input(f"ENTER THE NUMBER OF {self.productchoice.upper()} ITEMS YOU WILL LIKE TO BUY FROM OUR STOCK\n>>>  "))
            print()
            while self.qty > self.res[2]:
                print("THE AMOUNT OF OUR STOCK YOU WISH TO BUY IS OUT OF REACH...\nPLEASE BEAR WITH US AND TRY AGAIN")
                self.qty = int(input(f"ENTER THE NUMBER OF {self.productchoice.upper()} ITEMS YOU WILL LIKE TO BUY FROM OUR STOCK\n>>>  "))
            else:
                self.price = self.res[3] * self.qty
                if self.qty >= 10:
                    print()
                    print("LOADING...")
                    time.sleep(2)
                    print(f"THE CURRENT PRICE OF {self.productchoice.upper()} is {self.price}")
                    print()
                    self.newprice = self.price - (self.price * 0.1)
                    self.prices.update({self.productchoice:int(self.newprice)})
                    print("PROCESSING...")
                    time.sleep(3)
                    print(f"YOU HAVE A 10% DISCOUNT AND YOUR NEW PRICE IS {self.newprice}")
                else:
                    print(f"YOUR PRICE IS {self.price}")
                    self.prices.update({self.productchoice:int(self.price)})
                self.cart_product.update({self.productchoice : self.qty})
                #this is to store the product and the quantity, where the product is the key and the qty is the value
                self.cart.update({self.select : self.cart_product})
                #this is to store the collection and the(product& value), where the collection is the key and the self.cart_product((product& value))is the value
                print()
                time.sleep(1)
                print("YOUR ITEM HAS BEEN SUCCESSFULLY ADDED TO THE CART")
                print()
                time.sleep(1)
                print("LOADING...")
                time.sleep(1)
                self.decision = input("ENTER 1 TO ADD ANOTHER ITEM TO CART\nENTER 2 TO CHECKOUT\nENTER 3 TO CHECK/ADD ANOTHER COLLECTION\nENTER ANY OTHER KEY TO GO TO HOMEPAGE\n>>> ")
                if self.decision == "1":
                    self.additem()
                elif self.decision == "2":
                    self.cart_product = {}
                    self.checkout()
                elif self.decision == "3":
                    self.cart_product = {}
                    self.add()
                else:
                    self.cart_product = {}
                    self.homepage()
        else:
            print("PRODUCT NOT IN COLLECTION!")
            self.additem()

    def checkout(self):
        if len(self.cart) == 0:
            print("YOU DO NOT HAVE ANY ITEMS IN YOUR CART...PLEASE GO AND ADD ITEMS TO YOUR CART BY GOING TO OUR HOMEPAGE TO SEEK FOR HELP")
            self.homepage()
        else:
            print(f"YOU HAVE {self.cart} IN YOUR CART")
            print()
        if self.online_status == False:
            print("YOU ARE NOT LOGGED IN YET! GO TO THE HOMEPAGE TO LOG IN")
            self.homepage()
        else:
            self.payment = input("Enter payment option. Card or Transfer ").lower()
            if self.payment == "card":
                print("Payment by card successful")
            elif self.payment == "transfer":
                print("Payment by transfer successful")
            for product in self.cart:
            #this will bring out the collection(keys) by default since the array type is a dictionary
                self.cartitem = self.cart[product]
            #this will bring out the values in the cart as the values b'cos we are accessing the values by referring to its key
                for produce in self.cartitem:
                    #produce = coke
                    #self.cartitem[produce]
                    self.querry = f"SELECT * FROM {product} WHERE Product = {'%s'}"
                    self.val = (produce,)
                    cursor.execute(self.querry, self.val)
                    self.col = cursor.fetchone()
                    # print(self.col)
                    self.newqty = self.col[2] - self.cartitem[produce]
                    #self.col is the quantity on the table and self.cartitem[produce] is the quantity we ordered
                    self.pquerry = f"UPDATE {product} SET Quantity = {'%s'} WHERE Product = {'%s'} "
                    #this is to update the  collection table, quantity and product
                    self.val2 = (self.newqty, produce)
                    cursor.execute(self.pquerry, self.val2)
                    myconnect.commit()
                    self.salesquery = "INSERT INTO sales (Order_ID, Customer_ID, Product, Quantity, Price) VALUES(%s, %s, %s, %s, %s)"
                    self.order = random.randrange(100, 999)
                    self.customer_id = self.col[0]
                    self.val3 = (self.order, self.customer_id, produce, self.cartitem[produce], self.prices[produce])
                    cursor.execute(self.salesquery, self.val3)
                    myconnect.commit()
            print()
            print("PROCESSING...")
            time.sleep(1)
            print()
            print("YOUR CHECKOUT IS COMPLETED AND SUCCESSFUL")
            self.cart = {}
            #After checking out, we empty the cart
            self.appreciate()

    def appreciate(self):
        print(f"{self.username}, THANKS FOR YOUR PATRONAGE...")
        print()
        time.sleep(2)
        self.reply = input("ENTER 1 TO SHOP AGAIN\nENTER 2 TO GO TO HOMEPAGE\nENTER ANY OTHER KEY TO QUIT\n>>> ")
        if self.reply == "1":
            self.add()
        elif self.reply == "2":
            self.homepage()
        else:
            print(f"GOODBYE {self.username}")
            sys.exit()
        
Shopping_mall()