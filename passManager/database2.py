import sqlite3
conn2=sqlite3.connect("yassineDB.db")
c2=conn2.cursor()
c2.execute("CREATE TABLE IF NOT EXISTS passInfo(website TEXT ,password TEXT,CONSTRAINT ddd UNIQUE (website))")

def addPassword(website,password):
    try:
        c2.execute("INSERT INTO passInfo(website,password) VALUES(:website,:password)",{'website':str(website).lower(),'password':password})
        conn2.commit()
    except sqlite3.IntegrityError:
        print(f"{website} already has a password set on !")
        

def deletePassword(website):
    c2.execute("DELETE FROM passInfo WHERE website=:website",{'website':website})
    conn2.commit()

    
def listAllPasswords():
    c2.execute("SELECT * FROM passInfo")
    conn2.commit()
    return c2.fetchall()

