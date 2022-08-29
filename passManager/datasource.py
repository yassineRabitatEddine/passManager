import sqlite3
import bcrypt
from cryptography import fernet
import pyperclip
conn=sqlite3.connect("yassineDB.db")
c=conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users(name TEXT UNIQUE,password TEXT,salt TEXT)")
conn.commit()
conn2=sqlite3.connect("yassineDB.db")
c2=conn2.cursor()
c2.execute("CREATE TABLE IF NOT EXISTS passwords(website TEXT UNIQUE,password TEXT)")


class User():
    
    
    def __init__(self,userName,password):
        self.userName=userName
        self.password=password
        self.salt=bcrypt.gensalt()
        
    
    def addUser(self):
        try:
            c.execute("INSERT INTO users(name,password,salt) VALUES(:name,:password,:salt)",{'name':self.userName,'salt':self.salt,'password':bcrypt.hashpw(str(self.password).encode(),self.salt)})
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False


    def deleteUser(self):
        c.execute("DELETE FROM users WHERE name=:name and password=:password",{'name':self.userName,'password':self.password})
        conn.commit()


    def authenticate(self):
        c.execute("SELECT salt FROM users WHERE name=:name",{'name':self.userName})
        conn.commit()
        s=c.fetchone()
        if s==None: return -1
        c.execute("SELECT * FROM users WHERE name=:name and password=:password",{'name':self.userName,'password':bcrypt.hashpw(str(self.password).encode(),s[0])})
        conn.commit()
       
        if c.fetchone()==None:
            return -2
        else:
            return 1
        
    def listPasswords(self):
        c2.execute("SELECT * FROM passwords")
        conn.commit()
        s=c2.fetchall()
        if s==[]: print("\nNo password has been set yet !\n")
        else :
            for i in range(len(s)):
                print(f"\nService : {s[i][0]}\nPassword : {s[i][1]}\n***********")
        

class Password():
    
    
    def __init__(self,website):
        self.website=website
        
    def addPassword(self,password):
        try:
            c2.execute("INSERT INTO passwords(website,password) VALUES(:website,:password)",{'website':self.website,'password':password})
            conn2.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        
    def deletePassword(self):
        c2.execute("DELETE FROM passwords WHERE website = :website",{'website':self.website})
        conn2.commit()
        
        
    def getPassword(self):
        c2.execute("SELECT password FROM passwords WHERE website=:website",{'website':self.website})
        conn2.commit()
        s=c2.fetchone()[0]
        if s==None:
            return False
        else:
            pyperclip.copy(s)
            return True

        
    
    def updatePassword(self,newPassword):
        c2.execute("UPDATE passwords SET password=:password WHERE website=:website",{'password':newPassword,'website':self.website})
        conn2.commit()

    