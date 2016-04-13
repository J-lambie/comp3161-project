from subprocess import call
from sys import argv, exit
from faker import Factory
import random, string

verbs = ['baked', 'boiled', 'chopped', 'sautee']

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
	command = "insert into recipes VALUES (NULL, '%s', '%s', '%d', '%s')" % (recipe['email'], recipe['recipe_name'], recipe['calories'], recipe['image_url'])
	#print command
	fil.write(command+";\n")
	fil.close()
	return True

if __name__ == '__main__':

	FAKE_EMAIL = '@fake.com'

	if len(argv) < 3:
		print "Usage python populate_recipe_script.py <table_name> <count> - To obtain 1,000,000: count = 1000"
		exit(0)
	else:
		table = argv[1]
		count = int(argv[2])

	def randomword(length):
		return ''.join(random.choice(string.lowercase) for i in range(length))

	def create_fake_recipe(ind, ind1):
		fake = Factory.create()
		email = "%s%s" % (randomword(10), FAKE_EMAIL)
		recipe_name = verbs[random.randint(0,3)] + " " + foods[ind] + " and " + drinks[ind1]
		calories = random.randint(0,1000);
		image_url = fake.word() + ".com/" + fake.word() + ".jpg" 
		recipe = {'email':email, 'recipe_name':recipe_name, 'calories':calories, 'image_url':image_url}
		return insert_recipe('meal_plan', recipe)

	def populate_recipes_table(count):
		created = 0
		while created < count:
			j = 0
			while j < count:
				create_fake_recipe(created, j)
				j += 1
			created += 1

	ACTIONS = {'recipes': populate_recipes_table}

	try:
		ACTIONS[table](count)
	except KeyError:
		print "No table named as %s" % (table)
		