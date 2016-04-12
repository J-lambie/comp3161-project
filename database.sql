/*====CREATING TABLES=======*/
/*Strong Entities*/
create table users(
  email varchar(320) not null,
  password varchar(30) not null,
  firstname varchar(30) not null,
  lastname varchar(30) not null,
  year_of_birth year not null,
  primary key(email)
);
