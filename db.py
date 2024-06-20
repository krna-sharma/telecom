from mysql.connector import connect
from constant import *

class Database:
    def __init__(self):
        pass

    def connections(self):
        try:
            connections = connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
            )
            return connections
        except Exception as e:
            print("Issue in connecting with DB: ", e)

    def read_data_db(self, table_nm, cols = "*"):
        conn = self.connections()
        cursor = conn.cursor()
        try:
            print(f"select {cols} from {table_nm};")
            cursor.execute(f"select {cols} from {table_nm};")
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(f"Issue in reading data from DB: {e}")

    def insert_db(self, table,  values, columns = ''):
        conn = self.connections()
        cursor = conn.cursor()
        try:
            print(f"Insert into {table} values ({values})")
            cursor.execute(f"Insert into {table} {columns}"
                           f"values {values}")
            conn.commit()
        except Exception as e:
            print(f"Issue in inserting {table} DB: {e}")

    def update_db(self, table, new_val, whr_val, updt_col, whr_col):
        conn = self.connections()
        cursor = conn.cursor()
        try:
            print(f"Update {table} set {updt_col} = {new_val}, plan_status "
                           f"= 'Active' where {whr_col} = {whr_val}")
            cursor.execute(f"Update {table} set {updt_col} = '{new_val}', plan_status "
                           f"= 'Active' where {whr_col} = '{whr_val}'")
            conn.commit()

        except Exception as e:
            print(f"Issue in Updating {table} DB: {e}")