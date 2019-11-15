""" Gurpinder Grewal"""
import mysql.connector
from tabulate import tabulate
print("\nGurpinder Grewal\n")
# try except is used for successful database connection
try:
    # create and open database connection
    # Use your Own Credentials to Connect to Mysql
    
    mydb = mysql.connector.connect(
         host="",
         user="",
         passwd="",
        database=""
     )
    if(mydb):
        print("\t*****Connection succesful*****")

    mycursor = mydb.cursor()
    # mycursor.execute("CREATE DATABASE canadianCheese")
    # Show database
    # mycursor.execute("SHOW DATABASES")
    # for x in mycursor:
    #     print(x)
    # mycursor.execute("SHOW TABLES")
    # for x in mycursor:
    #   print(x)

    # Store strings of command in array
    commands = ["1 to Add data to database",
                "2 to retrieve one record and display record ",
                "3 to display all records from database",
                "4 to Emptied Database Table",
                "0 to exit"]

    # printing the options to stdout for user to select
    def print_commands():
        print("Option:\n")
        for option in commands:
            print(option)
        print("*"*40)

    # method to add record to Database
    def add_data():
        cheeseId = (input("Enter Cheese ID:\t "))
        cheeseName = input("Enter Cheese Name:\t ")
        mName = input("Enter Manufacturer Name:\t")
        mProvince = input("Enter Province Name:\t")
        mType = input("Enter Manufacturer Type:\t")
        sql = "INSERT INTO cheese (cheeseID,cheeseName,mName,mProvince,mType) VALUES (%s,%s,%s,%s,%s)"
        val = (cheeseId, cheeseName, mName, mProvince, mType)
        # values are sent through parameter in query %s to prevent sql injection
        # execute method is use to run sql query
        mycursor.execute(sql,val)
        mydb.commit()
        print("***************** Record Inserted Successfully ************************")

    # method to retrieve single record from database
    def display_one():
        chID = input("Enter Cheese ID want to display : ")
        # prevention from sql injection pass value sepratelly
        sql = "SELECT * FROM cheese WHERE cheeseID = %s "
        mycursor.execute(sql, (chID,))
        # fetchone is used to retrieve single record
        myresult = mycursor.fetchone()
        print(myresult)
        # return statement is used for test case
        return myresult

    # method to display all records user input
    def display_all():
        mycursor.execute("SELECT * FROM cheese")
        myresult = mycursor.fetchall()
        print(tabulate(myresult, headers=['CheeseID', 'CheeseName','Manufacture','Province','Type','PK'], tablefmt='psql'))

    # method to Emptied Table
    def delete_data():
        mycursor.execute("DELETE FROM cheese")
        mydb.commit()
        print("\t**** Table Emptied ****")

    while True:
        print_commands()
        command = input("Enter your command: ")
        if(command == '0'):
            print("----------- Exit ------------")
            break
        elif(command == '1'):
            add_data()
        elif(command == '2'):
            display_one()
        elif(command == '3'):
            display_all()
        elif(command == '4'):
            delete_data()
        else:
            print("**** Invalid Option ****\n ")

except mysql.connector.Error as e:
    print("\t***** Not succesful ****")
    print("Something went wrong"+format(e))
finally:
    print("*************** Run Test *****************")





