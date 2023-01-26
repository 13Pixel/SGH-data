import sqlite3

con = sqlite3.connect('database.db')

def get_session():
    cur = con.cursor()
    return cur

cur = get_session()


#Creating table as per requirement
sql ='''CREATE TABLE CONFIGURATION(
   DEVICE_CODE CHAR(20),
   RMQ_LINK CHAR(20),
   RMQ_Queue CHAR(20),
)'''

if __name__ == "__main__":
    cur.execute(sql)