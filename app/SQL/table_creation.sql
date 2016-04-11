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
    
);
create table Unit();
create table Instructions();

/*Relationship Entities*/
create table Used_In_Meals();
create table Has_Meal_Type();
create table Contains_Meal_Plan();
create table Uses_Ingredients();
create table Owns_ingredients();
create table Has_Unit();