from connect_mysql import connect_db
from mysql.connector import Error

# question 1 task 1

def add_member(id, name, age):
    conn = connect_db()
    if conn is not None:
        try:
            #Information to be added to the Members table, given when called
            cursor = conn.cursor()
            query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"
            new_member = (id, name, age)

            #Adds the information to the Members table
            cursor.execute(query, new_member)
            conn.commit()
            print("New member successfully added.")
        
        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

# question 2 task 2

def add_workout_session(member_id, date, duration_minutes, calories_burned):
    conn = connect_db()
    if conn is not None:
        try: 
            #The information to be inserted into the WorkoutSessions table when called
            cursor = conn.cursor()
            query = "INSERT INTO WorkoutSessions(member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)"
            new_workout_session = (member_id, date, duration_minutes, calories_burned)

            # Adds the information to the table 
            cursor.execute(query, new_workout_session)
            conn.commit()
            print("New workout session added successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

# question 1 task 3
def update_member_age(member_id, new_age):
    conn = connect_db()
    if conn is not None:
        try: 
            cursor = conn.cursor()


            #This code checks if the member whose age is to be updated exists
            check_query = "SELECT * FROM Members WHERE id = %s"
            cursor.execute(check_query, (member_id,))
            result = cursor.fetchall()

            # if the member exists, this will update their age
            if result: 
                update_age = "UPDATE Members SET age = %s WHERE id = %s"
                cursor.execute(update_age, (new_age, member_id))
                conn.commit()
                print(f"Member ID {member_id} age updated to {new_age}")
            
            #This will execute if the member does not exist
            else:
                print("This member ID does not have a member assigned to it.")
        
        #To catch potential errors
        except Error as e:
            print(f"Error: {e}")

        finally: 
            cursor.close()
            conn.close()

# question 1 task 4

def delete_workout_session(session_id):
    conn = connect_db()
    if conn is not None:
        try: 
            cursor = conn.cursor()

            # checks if the workout session we want to delete exists
            check_query = "SELECT * FROM WorkoutSessions WHERE session_id = %s"
            cursor.execute(check_query, (session_id,))
            result = cursor.fetchall()
            
            # if the workout session exists, this code will delete it
            if result:
                delete_session = "DELETE FROM WorkoutSessions WHERE session_id = %s"
                cursor.execute(delete_session, (session_id,))
                conn.commit()
                print(f"Session {session_id} successfully deleted.")
            
            # if the session does not exist, this will execute
            else: 
                print("This session ID does not exist.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

add_member(5, "Stephanie", 26)
add_workout_session(3, "2024-07-31", 140, 620)
update_member_age(3, 25)
