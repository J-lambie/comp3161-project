import MySQLdb

def execute(db , command):
    cur = db.cursor()
    try:
        cur.execute(command)
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()

if __name__ == '__main__':
    HOST = 'localhost'
    USER = 'root'
    PASSWORD = ''
    DATABASE = 'meal_plan'

    db = MySQLdb.connect(HOST, USER, PASSWORD ,DATABASE)

    print execute(db, "insert into users values ('travissmith94@hotmail.com', 'babbi3', 'Travis', 'Smith', 1994)")
    

