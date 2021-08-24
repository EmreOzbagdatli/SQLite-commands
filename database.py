import sqlite3

# Creating new Database.
conn = sqlite3.connect('Gyminformations.db')

c = conn.cursor()

# Creating table.

c.execute("""CREATE TABLE IF NOT EXISTS gyMembers

    (first_name text,
     last_name text,
     age INTEGER,
     sex text,
     weight INTEGER,
     height INTEGER,
     membership text)
     """)


all_members = [('Emre','Özbağdatlı',23,'Male',75,185,'yes'),
               ('Umut','Güven',23,'Male',85,185,'yes'),
               ('Ecem','Yıldız',22,'Female',55,163,'yes'),
               ('Sena','Pamuk',19,'Female',50,155,'yes'),
               ('Aleyna','Çakır',26,'Female',69,175,'yes'),
               ('Ali','Demir',19,'Male',82,176,'yes'),
               ('Mehmet','Demir',23,'Male',92,190,'yes'),
               ('Gizem','Kılıç',20,'Female',86,180,'yes'),
               ('Ayşe','Turgut',21,'Female',66,163,'yes'),
               ('Emrecan','Direk',23,'Male',60,196,'yes'),]

#c.executemany("INSERT INTO gyMembers VALUES(?,?,?,?,?,?,?)",all_members)

#Update our database.
c.execute("""UPDATE gyMembers SET weight = 65 WHERE first_name = 'Aleyna'""")
c.execute("""UPDATE gyMembers SET weight = 82 WHERE first_name = 'Gizem'""")
c.execute("""UPDATE gyMembers SET weight = 70 WHERE first_name = 'Emrecan'""")
c.execute("""UPDATE gyMembers SET weight = 80 WHERE first_name = 'Ali'""")

#Delete out databse record.
c.execute("""DELETE from gyMembers WHERE rowid = '5'""")


#Updating users memberships.
c.execute("""UPDATE gyMembers SET membership = 'No' WHERE  sex = 'Male' or sex = 'Female'""")

#input 1 record.
#c.execute("""INSERT INTO gyMembers VALUES ('Mehmet','Çolak','30','Male','100','205','Yes')""")


c.execute("""SELECT rowid,*FROM gyMembers""")

#c.execute("""SELECT rowid,*FROM gyMembers WHERE sex = 'Male'""")
Datas = c.fetchall()

#Print our datas on compiler.
for Data in Datas:
    print(Data)

conn.commit()

conn.close()