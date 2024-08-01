from connect_mysql import connect_db
from mysql.connector import Error

# question 2 task 1

def get_members_in_age_range(start_age, end_age):
    conn = connect_db()
    if conn is not None:
        try:
            # Searches through the database
            cursor = conn.cursor()
            query = "SELECT id, name, age FROM Members WHERE age BETWEEN %s and %s"
            #execute the query with the age range given
            cursor.execute(query, (start_age, end_age))
            # fetches the results of the previous line
            result = cursor.fetchall()

            # checks if any results were found within the age range
            if result:
                print("Members in the specified age range: ")
                for row in result:
                    id, name, age = row
                    print(f"Member ID: {id}, Member Name: {name}, Member Age: {age}")
            # if no members were found in the age range, this will print
            else:
                print("No members in that age range in the database.")
        
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()



