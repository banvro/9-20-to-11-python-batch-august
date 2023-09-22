import mysql.connector

# pip inatll mysql-connector-python 

conn = mysql.connector.connect(host = "localhost", username = "root", password = "1234", database = "morning")

# if conn.is_connected:
#     print("Database Connected..")

cuserser = conn.cursor()

cuserser.execute("insert into info values(3, 'xyz', 'xyz@gamil', '92836493');")

conn.commit()









# sql queries 

# show databases;

# create database morning;

# use morning;

# show tables;


# create table info(id int, Name varchar(20), Email varchar(30), Number varchar(12));

# insert into info values(1, "kriss", "kriss@gamil", "891239862");

# select * from info;
