from functools import wraps

def handle_database_operations(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        cursor = self.mysql.connection.cursor()

        try:
            result = func(self, cursor, *args, **kwargs)
            return result
        
        except Exception as error:
            print("Database error:", error)
        
        finally:
            cursor.close()

    return wrapper
  

class Users():
    def __init__(self,mysql) -> None:
        self.mysql = mysql

    @handle_database_operations
    def validate_user(self, cursor, username, password):

        cursor.execute("SELECT * FROM users WHERE name = %s AND password = %s", (username, password))
        response = cursor.fetchone()

        if response:
            return response
        
        return None
        
