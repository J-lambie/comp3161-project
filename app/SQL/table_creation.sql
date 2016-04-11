/*===CREATING DATABASE====*/
create database COMP3161_PROJECT;
use COMP3161_PROJECT;

/*====CREATING TABLES=======*/
/*Strong Entities*/
create table User(
    email varchar(50),
    password varchar(256),
    first_name varchar(20),
    last_name varchar(20),
    DOB date,
    primary key(email)
);
create table Recipe(
    recipe_id int auto_increment not null,
    recipe_name varchar(50),
    calories int,
    primary key (recipe_id)
);
create table Meal(
    meal_id int auto_increment not null,
    servings int,
    day date,
    primary key (meal_id)
);
create table Meal_Type(
    meal_type_name varchar(20),
    primary key (meal_type_name)
);
create table Meal_Plan(
    meal_plan_id int auto_increment not null,
    start_date date,
    end_date date,
    primary key (meal_plan_id)
);
create table Ingredients(
    ingredients_id int auto_increment not null,
    product_name varchar(20),
    calories_per_unit int,
    stock int,
    cost decimal(8,2),
    primary key (ingredients_id)
);
create table Unit(
    unit_name varchar(20),
    primary key (unit_name)
);
create table Instructions(
    recipe_id int,
    order_of_action int,
    action varchar(200),
    primary key (recipe_id,action)
);

/*Relationship Entities*/
create table Used_In_Meals(
    recipe_id int,
    meal_id int,
    primary key (recipe_id,meal_id),
    foreign key (meal_id) references Meal(meal_id) on delete cascade on update cascade,
    foreign key (recipe_id) references Recipe (recipe_id) on delete cascade on update cascade   
);
create table Has_Meal_Type(
    meal_id int,
    meal_type_name varchar(20),
    primary key (meal_id,meal_type_name),
    foreign key (meal_id) references Meal(meal_id) on delete cascade on update cascade,
    foreign key (meal_type_name) references Meal_Type
);
create table Contains_Meal_Plan(
    meal_id int,
    meal_plan_id int,
    primary key (meal_id,meal_plan_id),
    foreign key (meal_id) references Meal?(meal_id) on delete cascade on update cascade
    foreign key (meal_plan_id) references Meal_Plan (meal_plan_id) on delete cascade on update cascade
);
create table Uses_Ingredients(
    recipe_id int,
    ingredients_id int,
    units varchar(20),
    calories int,
    primary key (recipe_id,ingredients_id),
    foreign key (recipe_id) references Recipe(recipe_id) on delete cascade on update cascade,
    foreign key (ingredients_id) references Ingredients (ingredients_id) on delete cascade in updae cascade
);
create table Owns_ingredients(
    email varchar (50),
    ingredients_id int,
    primary key (email,ingredients_id),
    foreign key (email) references User (email) on delete cascade on update cascade,
    foreign key (ingredients_id) references Ingredients (ingredients_id) on delete cascade on update cascade
);
create table Has_Unit(
    ingredients_id int,
    unit_name varchar(20),
    primary key (ingredients_id,unit_name),
    foreign key (unit_name) references Unit (unit_name) on delete cascade on update cascade,
    foreign key (ingredients_id) references Ingredients (ingredients_id) on delete cascade on update cascade
);