import mysql.connector as connection
import random
import time
import sys
import re
myconnect = connection.connect(host = "127.0.0.1", user = "root", password = "EzekielWorld1.", database = "election")
cursor = myconnect.cursor()

class sqi_election:

    def __init__(self):
        print("BOT: WELCOME TO SQI COLLEGE OF ICT, A PRESTIGIOUS INSTITUTION WHERE WE SHAPE YOUTHS TO BE PACESETTERS IN TECHNOLOGY")
        print()
        time.sleep(2)
        self.students = []
        self.std_details = ["Surname", "Lastname", "Age", "Gender", "Email", "Address", "Phone_Number", "Lvl"]
        self.online_status = False
        self.departments = ["cyber_security", "data_science", "data_analysis", "graphics", "javascript", "ui_ux", "web_development"]
        self.election = ["President" ,"Vice_president", "General_secretary"]
        self.electcand = {"President" : ["Bukayo Saka", "Kylian Mbappe"], "Vice_president" : ["Shahrukh Khan", "Amir Khan"], "General_secretary" : ["Jet Lee", "Jackie Chan"]}
        self.homepage()

#this is the homepage function, where users get to choose their options and the beginning of the program
    def homepage(self):
        print("BOT: WELCOME TO SQI ONLINE PORTAL")
        time.sleep(1)
        print()
        self.decide = input("ENTER 1 TO REGISTER\nENTER 2 TO LOG IN\nENTER ANY KEY TO EXIT\n>>> ").strip()
        if self.decide == "1":
            print("PROCESSING...")
            time.sleep(2)
            self.register()
        elif self.decide == "2":
            print("PROCESSING...")
            time.sleep(2)
            self.login()
        else:
            print("BOT: THANKS FOR VOTING...WE HOPE TO SEE YOU NEXT YEAR!!!")
            sys.exit()

#this is the registration function, where users are to be registered before using the voting portal
    def register(self):
        self.dept = input(f"ENTER THE DEPARTMENT YOU WANT TO REGISTER TO\n{self.departments}\n>>> ").strip().lower()
        print("PROCESSING...")
        print()
        time.sleep(1)
        if self.dept in self.departments:       
            for info in self.std_details:
                print()
                self.information = input(f"ENTER YOUR {info}\n>>> ").strip().lower()
                time.sleep(1)
                print()
                while info == "Email":
                    reg = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[. ]\w{2,3}$'
                    if not re.findall(reg, self.information):
                        print("BOT: INVALID EMAIL..PLEASE TRY A VALID EMAIL!")
                        self.information = input(f"ENTER YOUR {info}\n>>> ").strip().lower()
                    else:
                        print("BOT: EMAIL IS VALID")
                        break
                else:
                    while info == "Phone_Number" and len(self.information) != 11:
                        print("BOT: PHONE NUMBER MUST BE 11 DIGITS..PLEASE TRY AGAIN!")
                        self.information = input(f"ENTER YOUR {info}\n>>> ").strip().lower()
                self.students.append(self.information)
            self.username = self.students[1][0:4] + str(random.randrange(100, 999))
            self.students.append(self.username)
            self.password = self.students[0][0:3] + str(random.randrange(200, 999))
            self.students.append(self.password)
            self.matric_num = random.randrange(125000, 955000)
            self.students.append(self.matric_num)
            print()
            print(self.students)
            self.confirm()
        else:
            print("BOT: THE DEPARTMENT YOU ENTERED IS NOT AVAILABLE..PLEASE CHOOSE FROM THE DEPARTMENTS THAT ARE AVAILABLE")
            self.register()
    
    #this is the function where we get to insert the details we want into the database
    def confirm(self):
        self.rquery = f"INSERT IGNORE INTO {self.dept} (Surname, Lastname, Age, Gender, Email, Address, Phone_Number, Lvl, Username, Password, Matric_number) VALUES({'%s'}, {'%s'}, {'%s'}, {'%s'}, {'%s'}, {'%s'}, {'%s'}, {'%s'}, {'%s'}, {'%s'}, {'%s'})"
        self.val = tuple(self.students)
        cursor.execute(self.rquery, self.val)
        myconnect.commit()
        print("PROCESSING...")
        time.sleep(2)
        print(f"BOT: DEAR {self.students[0].upper()} {self.students[1].upper()}, YOU HAVE BEEN REGISTERED TO {self.dept}")
        print()
        print(f"BOT: THESE ARE YOUR DETAILS")
        print("PROCESSING...")
        time.sleep(2)
        print(f"BOT: YOUR USERNAME IS {self.students[8]}\nYOUR PASSWORD IS {self.students[9]}")
        print("BOT: PROCEED TO LOG IN")
        self.login()

#this is the login function
    def login(self):
        time.sleep(1)
        print()
        self.dept = input(f"ENTER THE DEPARTMENT THAT YOU WERE REGISTERED TO\n{self.departments}\n>>> ").strip()
        print()
        if self.dept in self.departments:
            self.username = input("ENTER YOUR USERNAME\n>>> ").strip()
            print()
            self.password = input("ENTER YOUR PASSWORD\n>>> ").strip()
            self.lquery = f"SELECT * FROM {self.dept} WHERE Username = {'%s'} and Password = {'%s'}"
            self.val = (self.username, self.password)
            cursor.execute(self.lquery, self.val)
            self.result = cursor.fetchone()
            print()
            if self.result:
                if self.username == self.result[9] and self.password == self.result[10]:
                    print("PROCESSING...")
                    time.sleep(2)
                    print(f"BOT: DEAR {self.username} YOU HAVE LOGGED IN SUCCESSULLY")
                    print()
                    print(f"BOT: PROCEED TO GET YOUR VOTER'S CARD FOR UPCOMING ELECTIONS")
                    self.performance()
                    self.online_status = True
                else:
                    print("BOT: INVALID LOGIN DETAILS...PLEASE CHECK THAT YOU ENTERED THE CORRECT DETAILS TO LOG IN!")
                    self.login()
            else:
                print("BOT: YOU HAVE NO RECORDS ON OUR DATABASE...ENSURE YOU ARE REGISTERED TO BE ABLE TO LOG IN")
                self.homepage()

        else:
            print("BOT: THE DEPARTMENT YOU ENTERED IS NOT AVAILABLE..PLEASE ENSURE YOU ENTER THE AVAILABLE DEPARTMENTS WE HAVE")
            self.login()

    def performance(self):
        print()
        print("PROCESSING...")
        time.sleep(1)
        print("BOT: WELCOME TO SQI ONLINE PORTAL")
        print()
        time.sleep(2)
        print("ENTER 1 FOR VOTER'S REGISTRATION\nENTER 2 TO CAST VOTES\nENTER 3 TO COUNT AND CHECK RESULTS")
        self.decide = input(">>> ")
        if self.decide == "1":
            self.vote_registration()
        elif self.decide == "2":
            self.cast_votes()
        elif self.decide == "3":
            self.count_votes()
        else:
            print("BOT: INVALID INPUT..PLEASE TRY AGAIN!")
            self.performance()

#this is the voting registration portal
    def vote_registration(self):
        print()
        print("PROCESSING...")
        time.sleep(2)
        print("BOT:\nWELCOME TO THE VOTING PORTAL\nENSURE TO BE REGISTERED TO BE ABLE TO EXCERSISE YOUR RIGHT AS A STUDENT\nTHE VOTING CARD WILL ENSURE YOU PARTICIPATE IN SCHOOL ELECTIONS AND SOLIDIFIES YOUR STUDENTSHIP")
        print()
        self.matric_num = input("BOT: ENTER YOUR MATRIC NUMBER\n>>> ").strip()
        self.deptreg = input(f"BOT: ENTER YOUR DEPARTMENT\n{self.departments}\n>>> ").strip().lower()
        if self.deptreg in self.departments:
            #The matric number is being used to fetch the info of the person registered in a particular dept
            self.mquery = f"SELECT * FROM {self.deptreg} WHERE Matric_number = {'%s'}"
            self.val = (self.matric_num,)
            cursor.execute(self.mquery, self.val)
            self.regresult = cursor.fetchone()
            print()
            print(self.regresult)
            if self.regresult:
                #if your info is on the database, it will fetch the details at the index specified and fill it automatically on the voter's card..we will now insert it into the voting_portal
                self.fullname = self.regresult[1] + " " + self.regresult[2]
                self.lvl = self.regresult[8]
                self.votecard = "sqi" + str(random.randrange(1000, 9500))
                self.vrquery = "INSERT IGNORE INTO voting_portal(Fullname, Department, Lvl, Voter_card, Matric_number, President, Vice_president, General_secretary)VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
                self.val = (self.fullname, self.deptreg, self.lvl, self.votecard, self.matric_num, "nil", "nil", "nil")
                cursor.execute(self.vrquery, self.val)
                myconnect.commit()
                print()
                print("PROCESSING...")
                time.sleep(2)
                print(f"BOT:\nDEAR {self.fullname.upper()}, YOUR REGISTRATION WAS SUCCESSFUL\nYOUR VOTER'S CARD IS {self.votecard}")
                print()
                time.sleep(1)
                print("BOT: PROCEED TO CAST YOUR VOTE FOR THE CANDIDATE OF YOUR CHOICE")
                print("DO YOU WANT TO VOTE?")
                print()
                self.grab = input("ENTER 1 TO CAST VOTES\nENTER 2 TO GO TO HOMEPAGE\nENTER ANY KEY TO EXIT\n>>> ")
                if self.grab == "1":
                   self.cast_votes()
                elif self.grab == "2":
                    self.homepage()
                else:
                    sys.exit()
            else:
                print("BOT: NO RECORD OF YOURS ON OUR DATABASE")
                self.vote_registration()
        else:
            print("BOT: THE DEPARTMENT YOU ENTERED IS NOT AVAILABLE..PLEASE ENTER THE DEPARTMENTS THAT ARE AVAILABLE")
            self.vote_registration()

#this is the function where votes are casted for the candidates
    def cast_votes(self):
        print()
        print("PROCESSING...")
        time.sleep(2)
        self.votecard = input("BOT: ENTER YOUR VOTER'S CARD/NUMBER\n>>> ").strip()
        #use the voter's card to fetch all the info about the person on the voting_portal
        self.cardquery = "SELECT * FROM voting_portal WHERE Voter_card = %s"
        self.cardval = (self.votecard,)
        cursor.execute(self.cardquery, self.cardval)
        self.find = cursor.fetchone()
        self.confirm_votes()
        #we had to re_select the query and val in the castvotes function by calling the execute function and placing it in the confirmvotes to ensure that the user cannot vote twice in a 
        #category..this is done to update what we have in the database to be new. we also had to change the self.val to cardval
    def confirm_votes(self):
        print()
        cursor.execute(self.cardquery, self.cardval)
        self.find = cursor.fetchone()
        if self.find:
            self.votecategory = input(f"ENTER THE CATEGORY THAT YOU WANT\n{self.election}\n>>> ").strip().capitalize()
            if self.votecategory in self.election:
                if self.votecategory == "President":
                    self.index = 6
                    if self.find[6] != "nil":
                        print("BOT: YOU HAVE ALREADY CASTED YOUR VOTE IN THIS CATEGORY")
                        self.optvote()
                elif self.votecategory == "Vice_president":
                    self.index = 7
                    if self.find[7] != "nil":
                        print("BOT: YOU HAVE ALREADY CASTED YOUR VOTE IN THIS CATEGORY")
                        self.optvote()
                elif self.votecategory == "General_secretary":
                    self.index = 8
                    if self.find[8] != "nil":
                        print("BOT: YOU HAVE ALREADY CASTED YOUR VOTE IN THIS CATEGORY")
                        self.optvote()
                print()
                print("PROCESSING...")
                time.sleep(2)
                print(f"BOT: THESE ARE THE {self.votecategory} CANDIDATES\n{self.electcand[self.votecategory]}")
                print()
                self.votechoice = input("BOT: ENTER THE CANDIDATE OF YOUR CHOICE\n>>> ").strip().title()
                while self.votechoice not in self.electcand[self.votecategory]:
                    print("BOT: CANDIDATE NOT AMONG!..PLEASE CHECK THE LIST OF CANDIDATES AVAILABLE AND VOTE AGAIN")
                    self.votechoice = input("BOT: ENTER THE CANDIDATE OF YOUR CHOICE\n>>> ").strip().title()  
                else:
                    self.vtquery = f"UPDATE voting_portal SET {self.votecategory} = {'%s'} WHERE Voter_card = {'%s'}"
                    self.val = (self.votechoice, self.votecard)
                    cursor.execute(self.vtquery, self.val)
                    myconnect.commit()
                    print()
                    print("PROCESSING...")
                    time.sleep(2)
                    print(f"BOT: YOU HAVE SUCCESSFULLY CASTED YOUR VOTE FOR {self.votechoice.upper()}")
                    print()
                    self.optvote()
            else:
                print("BOT: THE CATEGORY YOU ENTERED DOES NOT EXIST..PLEASE ENTER THE CATEGORY THAT IS AVAILABLE")
                self.confirm_votes()
        else:
            print("BOT: NO RECORD OF YOURS ON OUR DATABASE...ENSURE YOU REGISTER TO BE ABLE TO ACCESS THE VOTING PORTAL")
            self.homepage()
   
    def optvote(self):
        self.decide = input("ENTER 1 TO VOTE IN ANOTHER CATEGORY\nENTER 2 TO CHECK RESULT\nENTER ANY KEY TO GO TO HOMEPAGE\n>>> ").strip()
        if self.decide == "1":
            self.confirm_votes()
        elif self.decide == "2":
            self.count_votes()
        else:
            self.homepage()
    
    #this is the function where we count votes to know who has the maximium number of votes and the minimum number of votes
    def count_votes(self):
        self.viewresult = {}
        self.view = input("ENTER 1 TO VIEW OVERALL RESULTS\nENTER 2 TO VIEW DEPARTMENTAL RESULT\n>>> ").strip()
        if self.view == '1':
            self.choose = input(f"ENTER THE CATEGORY YOU WANT TO VIEW\n{self.election}\n>>>  ").strip().capitalize()
            if self.choose in self.election:
                for name in self.electcand[self.choose]:
                    self.pquery = f"SELECT count({self.choose}) FROM voting_portal WHERE {self.choose} = {'%s'}"
                    print()
                    self.val = (name,)
                    cursor.execute(self.pquery, self.val)
                    self.rsu = cursor.fetchone()
                    print(f"BOT: {name} Has {self.rsu[0]} votes")
                    time.sleep(1)
                    print()
                    self.viewresult.update({name:self.rsu[0]})
                self.checktie()
            else:
                print("BOT: CATEGORY NOT FOUND..PLEASE TRY THE AVAILABLE CATEGORIES AGAIN!")
                self.count_votes()
        elif self.view == "2":
            self.viewdept = input(f"ENTER THE DEPARTMENT YOU WANT TO VIEW\n{self.departments}\n>>> ").strip().lower()
            if self.viewdept in self.departments:
                self.choose = input(f"ENTER THE CATEGORY YOU WANT TO VIEW\n{self.election}\n>>> ").strip().capitalize()
                if self.choose in self.election:
                    for name in self.electcand[self.choose]:
                        self.pquery = f"SELECT count({self.choose}) FROM voting_portal WHERE Department = {'%s'} and {self.choose} = {'%s'}"
                        print()
                        print(f"BOT: {name} Has {self.count2(self.pquery, (self.viewdept, name))} votes")
                        time.sleep(1)
                        print()
                        self.viewresult.update({name:self.count2(self.pquery, (self.viewdept, name))})
                    self.checktie()
                else:
                    print("BOT: CATEGORY NOT FOUND..PLEASE TRY THE AVAILABLE CATEGORIES AGAIN!")
                    self.count_votes()
            else:
                print("BOT: THE DEPARTMENT YOU ENTERED IS NOT AVAILABLE..PLEASE ENSURE YOU ENTER THE DEPARTMENT THAT IS AVAILABLE!")
                self.count_votes()
        else:
            print("BOT: INVALID INPUT...PLEASE TRY AGAIN!")
            self.count_votes()
    
    def count2(self, query, val):
        cursor.execute(query, val)
        self.rsu = cursor.fetchone()
        return self.rsu[0]
    
    def checktie(self):
        win = max(self.viewresult.values())
        self.tie_arr = []
        for key, values in self.viewresult.items():
            if values == win:
                self.tie_arr.append(key)
        if len(self.tie_arr) > 1:
            print()
            print("BOT: THERE IS A TIE BETWEEN THE CANDITATES FOR THIS CATEGORY!")
            for i in self.tie_arr:
                print(i, end=("  "))
        else:
            print(f"BOT: THE WINNER IS {max(self.viewresult, key=self.viewresult.get)}")
            print()
            print(self.viewresult)
        self.viewresult = {}
        time.sleep(1)
        print()
        self.viewmode()

    def viewmode(self):
        print("ENTER 1 TO VIEW ANOTHER CATEGORY\nENTER 2 TO CAST VOTE\nENTER ANY OTHER KEY TO EXIT")
        self.viewside = input(">>> ")
        if self.viewside == "1":
            self.count_votes()
        elif self.viewside == "2":
            self.cast_votes()
        else:
            print("BOT: GOODBYE, THANKS FOR PARTICIPATING IN THIS YEAR'S ELECTION...WE HOPE TO SEE YOU NEXT YEAR!")
            sys.exit()

sqi_election()
 

 # def count(self, query, val):
    #     self.val = (val,)
    #     cursor.execute(query, self.val)
    #     self.rsu = cursor.fetchone()
    #     return self.rsu[0]

