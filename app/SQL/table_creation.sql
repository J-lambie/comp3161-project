/*===CREATING DATABASE====*/
drop database if exists meal_plan;
create database meal_plan;
use meal_plan;

/*====CREATING TABLES=======*/
/*Strong Entities*/
create table users(
    email varchar(320) not null,
    password varchar(256) not null,
    firstname varchar(20) not null,
    lastname varchar(20) not null,
    year_of_birth year,
    primary key(email)
);

create table recipes(
    recipe_id int auto_increment not null,
    email varchar(320) not null,
    recipe_name varchar(50) not null,
    calories int not null,
    image_url varchar(320),
    primary key (recipe_id),
    foreign key (email) references users(email) on delete cascade on update cascade
);

create table meal_types(
    meal_type_name varchar(20),
    primary key (meal_type_name)
);

create table meal_plans(
    meal_plan_id int auto_increment not null,
    start_date date,
    end_date date,
    primary key (meal_plan_id)
);

create table meals(
    meal_id int auto_increment not null,
    email varchar(320),
    servings int,
    day date,
    meal_type_name varchar(20) not null,
    meal_plan_id int not null,
    primary key (meal_id),
    foreign key(email) references users(email) on delete cascade on update cascade,
    foreign key(meal_type_name) references meal_types(meal_type_name) on update cascade,
    foreign key(meal_plan_id) references meal_plans(meal_plan_id) on delete cascade on update cascade
);

create table ingredients(
    ingredients_id int auto_increment not null,
    product_name varchar(20),
    email varchar(320),
    calories_per_unit int,
    stock int,
    cost decimal(8,2),
    primary key (ingredients_id),
    foreign key (email) references users(email) on delete cascade on update cascade
);

create table units(
    unit_name varchar(20),
    primary key (unit_name)
);

create table instructions(
    recipe_id int,
    order_of_action int,
    action varchar(200),
    primary key (recipe_id,order_of_action),
    foreign key (recipe_id) references recipes(recipe_id) on delete cascade on update cascade
);

/*Relationship Entities*/
create table used_in_meals(
    recipe_id int,
    meal_id int,
    primary key (recipe_id,meal_id),
    foreign key (meal_id) references meals(meal_id) on delete cascade on update cascade,
    foreign key (recipe_id) references recipes (recipe_id) on delete cascade on update cascade   
);

create table uses_ingredients(
    recipe_id int,
    ingredients_id int,
    units varchar(20),
    calories int,
    primary key (recipe_id,ingredients_id),
    foreign key (recipe_id) references recipes(recipe_id) on delete cascade on update cascade,
    foreign key (ingredients_id) references ingredients (ingredients_id) on delete cascade on update cascade
);

create table measured_in_unit(
    ingredients_id int,
    unit_name varchar(20),
    primary key (ingredients_id,unit_name),
    foreign key (unit_name) references units (unit_name) on delete cascade on update cascade,
    foreign key (ingredients_id) references ingredients (ingredients_id) on delete cascade on update cascade
);
