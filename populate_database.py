from sys import argv, exit
import MySQLdb
from faker import Factory
import random, string

def insert_user(db , user):
    command = "insert into users values ('%s', '%s', '%s', '%s', %d)" % (user['email'], user['password'], user['firstname'], user['lastname'], user['year_of_birth'])
    return execute(db, command)

def execute(db , command):
    try:
        cur = db.cursor()
        cur.execute(command)
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        print e.strerror()
        return False

if __name__ == '__main__':

    HOST = 'localhost'
    USER = 'root'
    PASSWORD = ''
    DATABASE = 'meal_plan'

    FAKE_EMAIL = '@fake.com'

    if len(argv) < 3:
        print "Usage python populate_database.py <table_name> <count>"
        exit(0)
    else:
        table = argv[1]
        count = int(argv[2])

    def randomword(length):
        return ''.join(random.choice(string.lowercase) for i in range(length))

    db = MySQLdb.connect(HOST, USER, PASSWORD ,DATABASE)

    def create_fake_user():
        fake = Factory.create()
        name = fake.name().split()
        firstname = name[0]
        lastname = name[1]
        email = "%s%s" % (randomword(10), FAKE_EMAIL)
        password = randomword(15)
        year = random.randint(1950 , 2003)

        user = {'email': email , 'password' : password, 'firstname': firstname, 'lastname': lastname, 'year_of_birth': year} 

        return insert_user(db, user)

    def populate_users_table(count):
        created = 0
        for user in range(0, count):
            if not create_fake_user():
                break
            else:
                created += 1
        print "%d of %d users created" % (created, count)
        db.close()

    ACTIONS = {'users': populate_users_table}

    try:
        ACTIONS[table](count)
    except KeyError:
        print "No table named %s" % (table)
