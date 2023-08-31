import csv

class Managedb:
    def __init__(self,
                userID:str,
                dbFile:str='users.csv'):
        """
        Parameters:
    
            userID (``str``):
                It can be a phone number an usernaem or anything else... 
                
            dbFile (``str``, optional):
                The .csv file wich will considered as database

            kind (``int``, optional):
                Only for adding, reading or changing an old user's info

            amount (``int``, optional):
                the amount you want to add to your user
        """
        self.dbFile = dbFile
        self.userID = userID
        self.csv_reader = csv.reader(open(self.dbFile, 'r'))
    def ADD_user(self):
        with open(self.dbFile, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            rows = list(csv_reader)
        flager = False
        for row in rows:
            if row[0] == str(self.userID):
                flager = True
                break
        if not flager:
            new_info_for_him = f"{self.userID},0,0,0,0,2,1,3\n" # the info you want to be added for the new user
            with open(self.dbFile, 'a') as db:
                db.write(new_info_for_him)
                db.close()
        else:
            print('Already existed!')
    def READ_info(self,kind:int):
        for row in self.csv_reader:
            if row[0] == self.userID:
                return row[int(kind)]  
    def ADD_info(self, kind:int, amount:int):
        with open(self.dbFile, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            rows = list(csv_reader)
        for row in rows:
            if row[0] == str(self.userID):
                row[int(kind)] = str(int(row[int(kind)])+int(amount))
                break
        with open(self.dbFile, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(rows)
    def CHANGE_info(self, kind:int, amount:int):
        with open(self.dbFile, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            rows = list(csv_reader)
        for row in rows:
            if row[0] == str(self.userID):
                row[int(kind)] = str(amount)
                break
        with open(self.dbFile, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(rows)

user1 = Managedb('123456789', 'users.csv')
user1.ADD_user()
user1.READ_info(2)
user1.CHANGE_info(2,1000)
user1.ADD_info(2, 500)