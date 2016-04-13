from subprocess import call
from sys import argv, exit
import MySQLdb
from faker import Factory
import random, string

f = open('foods.txt', 'r')
g = open('drinks.txt', 'r')
foods = []
drinks = []

for food in f:
	foods += [food.strip()]
for drink in g:
	drinks += [drink.strip()]

print foods
print drinks

f.close()
g.close()


def insert_recipe(db, recipe):
	fil = open('recipes.sql', 'a')
	command = "insert into recipes (NULL, '%s', '%s', '%d', '%s')" % (recipe['email'], recipe['recipe_name'], recipe['calories'], recipe['image_url'])
	print command
	fil.write(command+";\n")
	fil.close()
	return execute(db, command)

def execute(db, command):
	try:
		cur = db.cursor()
		cur.execute(command)
		db.commit()
		print command + ';'
		return True
	except Exception as e:
		db.rollback()
		if __name__ != '__main__':
			print str(e)
		return False

if __name__ == '__main__':

	HOST = 'localhost'
	USER = 'root'
	PASSWORD = ''
	DATABASE = 'meal_plan'

	FAKE_EMAIL = '@fake.com'

	if len(argv) < 3:
		print "Usage python populate_recipes.py <table_name> <count>"
		exit(0)
	else:
		table = argv[1]
		count = int(argv[2])

	def randomword(length):
		return ''.join(random.choice(string.lowercase) for i in range(length))

	db = MySQLdb.connect(HOST, USER, PASSWORD, DATABASE)

	def create_fake_recipe(ind, ind1):
		
		fake = Factory.create()
		email = "%s%s" % (randomword(10), FAKE_EMAIL)
		recipe_name = foods[ind] + " and " + drinks[ind1]
		calories = random.randint(0,1000);
		image_url = fake.word() + ".com/" + fake.word() + ".jpg" 
		recipe = {'email':email, 'recipe_name':recipe_name, 'calories':calories, 'image_url':image_url}
		return insert_recipe(db, recipe)

	def populate_recipes_table(count):
		print "hello world"
		created = 0
		j = 0
		while created < count:
			while j < count:
				if not create_fake_recipe(created, j):
					pass
				else:
					j += 1
			created += 1
		db.close()

	ACTIONS = {'recipes': populate_recipes_table}

	try:

		ACTIONS[table](count)
	except KeyError:
		print "No table named as %s" % (table)
		