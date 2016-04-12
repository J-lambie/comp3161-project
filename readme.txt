How to run the system
---------------------
Step1
------
Setup a virtual environment by:
-install virtualenv:
        pip install virtualenv
-create a virtual environment using:
        virtualenv venv
-start the virtual environment by:
        source venv/bin/activate

Step2
------
Dowload the required libraries and frameworks
-Run the following:
        pip install -r requirements.txt

Step3
-------
Start the server:
For C9:
        mysql-clt start
        mysql-ctl cli
        
        In the mysql client run the folowing:
        source app/SQL/table_creation.sql;
        create user root;
        grant all privileges on meal_plan to root;
        
        

Step 4
-------
Run the system:
-Run the command :
        python run.py

DATABASE CONCERNS
-----------------
assumes root user with no password and database called meal_plan

You may need to install libmysqlclient-dev
-Run command:
        sudo apt-get install libmysqlclient-dev
