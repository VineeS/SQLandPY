import mysql.connector

# establishing the connection 
connection = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
) 

cursor = connection.cursor()
word = input("enter the word :")
query = cursor.execute(f"SELECT * FROM Dictionary WHERE EXPRESSION = '{word}' ")
results = cursor.fetchall()

#print(results[0])
if results:
    for result in results:
        print(result[1])
else:
    print("No word found !!")


