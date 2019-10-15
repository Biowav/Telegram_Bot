import sqlite3
import time

class DBHelper:
    def __init__(self):
        self.connect = sqlite3.connect('gaussDB.sqlite')

    def setup_users(self):
        self.connect('''CREATE TABLE IF NOT EXISTS USERS (
  ID         INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  USER_ID    INT UNIQUE                        NOT NULL,
  FIRST_NAME VARCHAR(255)                      NOT NULL,
  LAST_NAME  VARCHAR(255)                      NULL,
  USER_NAME  VARCHAR(255)                      NULL
);''')
        self.connect.commit()

    def setup_inforusers(self):
        self.connect('''CREATE TABLE IF NOT EXISTS INFORUSERS (
  ID         INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  USER_ID    INT UNIQUE                        NOT NULL,
  FIRST_NAME VARCHAR(255)                      NOT NULL,
  LAST_NAME  VARCHAR(255)                      NULL,
  USER_NAME  VARCHAR(255)                      NULL,
  N_POLES    INT                               DEFAULT 0,
  EXPERIENCE INT                               DEFAULT 0,
  RANK       INT                               DEFAULT 0
);''')
    def setup_poles(self):
        self.connect('''CREATE TABLE IF NOT EXISTS POLES (
          USER_ID    INT                               NOT NULL,
          POLE VARCHAR(255)                            NULL,
          POLE_DATE VARCHAR(255)                       NULL,
          FOREIGN KEY(USER_ID) REFERENCES USERS(USER_ID)
        );''')

    def setup_poles_infor(self):
        self.connect('''CREATE TABLE IF NOT EXISTS INFORPOLES (
          USER_ID    INT                               NOT NULL,
          POLE VARCHAR(255)                            NULL,
          POLE_DATE VARCHAR(255)                       NULL,
          FOREIGN KEY(USER_ID) REFERENCES INFORUSERS(USER_ID)
        );''')

    def add_user(self, user_id, first_name, last_name='', username=''):
        self.connect.execute('''INSERT INTO USERS (USER_ID, FIRST_NAME, LAST_NAME, USER_NAME)
                        VALUES (?,?,?,?);''',(user_id, first_name, last_name, username))

        self.connect.commit()

    def add_inforuser(self, user_id, first_name, last_name='', username=''):
        self.connect.execute('''INSERT INTO INFORUSERS (USER_ID, FIRST_NAME, LAST_NAME, USER_NAME)
                        VALUES (?,?,?,?);''',(user_id, first_name, last_name, username))

        self.connect.commit()

    def delete_user(self, user_id):
        self.connect.execute('DELETE FROM USERS WHERE USER_ID = (?)', user_id)
        self.connect.commit()

    def delete_inforuser(self,user_id):
        self.connect.execute('DELETE FROM INFORUSERS WHERE USER_ID = (?)', user_id)
        self.connect.commit()

    def update(self, user_id,first_name,last_name,username):
        self.connect.execute('''UPDATE USERS SET FIRST_NAME=?, LAST_NAME=?, USER_NAME=? WHERE USER_ID=? AND FIRST_NAME!=?
                                AND LAST_NAME!=? AND USER_NAME!=?''',
                             ( first_name, last_name, username,user_id,first_name,last_name,username))
        self.connect.commit()

    def update_inforusers(self, user_id,first_name,last_name,username):
        self.connect.execute('''UPDATE INFORUSERS SET FIRST_NAME=?, LAST_NAME=?, USER_NAME=? WHERE USER_ID=? AND FIRST_NAME!=?
                                AND LAST_NAME!=? AND USER_NAME!=?''',
                             ( first_name, last_name, username,user_id,first_name,last_name,username))
        self.connect.commit()

    def check_username(self, user_id, username):
        """ Check if a telegram user have changed it's username and updates it.
        :param user_id: Telegram user id
        :param username: Telegram user name
        """
        self.connect.execute('''UPDATE USERS SET USER_NAME = ? WHERE  USER_ID = ? AND (USER_NAME != ? OR USER_NAME IS NULL);''',
                          (username, user_id, username))
        self.connect.commit()

    def get_user_by_id(self, user_id):
        return [user for user in
                self.connect.execute('SELECT * FROM USERS WHERE USER_ID = ?', (user_id,))]

    def get_user_by_username(self, username):
        return [user for user in
                self.connect.execute('SELECT * FROM USERS WHERE USER_NAME = ?', (username,))]

    def get_username_by_id(self,user_id):
        return [user for user in
                self.connect.execute('SELECT USERNAME FROM INFORPOLES WHERE USER_ID = ?', (user_id,))]
    def get_poleman_id(self):
        return [user for user in
                self.connect.execute('SELECT USER_ID FROM INFORPOLES WHERE ID=(SELECT MAX(ID) FROM INFORPOLES)')]

    def add_pole(self,user_id,username,pole='',pole_date=''):
        self.connect.execute('''INSERT INTO POLES (USER_ID,USERNAME, POLE, POLE_DATE,POLE_DAY)
                                VALUES (?,?,?,?,?);''', (user_id,username, pole, pole_date,int(time.strftime("%d",time.localtime()))
))
        self.connect.commit()

    def add_inforpole(self, user_id, username, pole='', pole_date=''):
        self.connect.execute('''INSERT INTO INFORPOLES (USER_ID,USERNAME, POLE, POLE_DATE,POLE_DAY)
                                VALUES (?,?,?,?,?);''',
                             (user_id, username, pole, pole_date, int(time.strftime("%d", time.localtime()))
                              ))
        self.connect.commit()


    def get_pole_day(self):
        return [user for user in self.connect.execute('SELECT POLE_DAY FROM POLES WHERE ID=(SELECT MAX(ID) FROM POLES)')]

    def get_inforpole_day(self):
        return [user for user in
                self.connect.execute('SELECT POLE_DAY FROM INFORPOLES WHERE ID=(SELECT MAX(ID) FROM INFORPOLES)')]

    def show_poles(self,username):
        return [user for user in
                self.connect.execute('SELECT * FROM POLES WHERE USERNAME = ?', (username,))]

    def show_inforpoles(self,username):
        return [user for user in
                self.connect.execute('SELECT * FROM INFORPOLES WHERE USERNAME = ?', (username,))]

    def db_to_list(self):
        self.connect.row_factory = lambda cursor, row: row[0]
        c=self.connect.cursor()
        user_ids=c.execute('SELECT USER_ID FROM USERS').fetchall()
        usernames=c.execute('SELECT USER_NAME FROM USERS').fetchall()
        dict_id_username=dict(zip(user_ids,usernames))
        return dict_id_username
