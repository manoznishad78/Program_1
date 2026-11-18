import mysql.connector
from mysql.connector import Error

connection = None
cursor = None

try:
    # 1. Connect to your database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",      
        database="campusbookstore"     
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # 2. Get inputs from the user
        username = input('Enter username: ')
        password = input('Enter password: ')

        # 3. Write the INSERT query with placeholders
        query = "INSERT INTO infos (username, password) VALUES (%s, %s)"
        data_to_insert = (username, password)

        # 4. Execute the query
        cursor.execute(query, data_to_insert)

        # 5. COMMIT the transaction to permanently save the data
        connection.commit()
        print(f"User '{username}' added successfully!")

        # 6. OPTIONAL: Verify by displaying all users in the table
        print("\n--- Current Users in Database ---")
        cursor.execute("SELECT username, password FROM infos")
        records = cursor.fetchall()
        for row in records:
            print(f"Username: {row[0]}, Password: {row[1]}")

except Error as e:
    print(f"Error while communicating with MySQL: {e}")
    if connection:
        connection.rollback()

finally:
    # 7. Clean up resources
    if cursor is not None:
        cursor.close()
    if connection is not None and connection.is_connected():
        connection.close()
        print("\nMySQL connection closed.")
