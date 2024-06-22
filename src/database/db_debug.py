"""
Module for performing debugging operations on a MySQL database.

This module includes functionality to:
1. Display a custom debug banner.
2. Connect to the MySQL database using `DBConnection`.
3. Create a debug table with sample schema (`debug_users`).
4. Insert sample records into the debug table.
5. Fetch and display all records from the debug table.
6. Update a record in the debug table.
7. Fetch and display a single updated record from the debug table.
8. Delete a record from the debug table.
9. Clean up (drop) the debug table after operations.

Dependencies:
- Python packages: mysql-connector-python, dotenv

Author: devinci-it
Date: 2024 06
"""

from mysql.connector import Error
from .db_connection import DBConnection
from .db_crud import DBCrud

class DBDebug:
    """
    A utility class to perform debugging operations on the MySQL database.
    """
    @staticmethod
    def display_banner():
        print(  """
···········································································
: _______  .______    __    __    _______   _______  _______ .______      :
:|       \ |   _  \  |  |  |  |  /  _____| /  _____||   ____||   _  \     :
:|  .--.  ||  |_)  | |  |  |  | |  |  __  |  |  __  |  |__   |  |_)  |    :
:|  |  |  ||   _  <  |  |  |  | |  | |_ | |  | |_ | |   __|  |      /     :
:|  '--'  ||  |_)  | |  `--'  | |  |__| | |  |__| | |  |____ |  |\  \----.:
:|_______/ |______/   \______/   \______|  \______| |_______|| _| `._____|:
···········································································
""")

    @staticmethod
    def debug():
        """
        Performs debugging operations including testing connection, creating a debug table,
        performing CRUD operations, and cleaning up the debug table.
        """
        from ..cli.cli import CLIUtility  # Adjust import path as per your project structure

        connection = None

        try:
            DBDebug.display_banner()
            DBConnection.debug_banner()
            CLIUtility.header("DEBUGGING DATABASE")

            # Test database connection
            connection = DBConnection.connect()
            if not connection:
                CLIUtility.error("Unable to connect to database.")
                return

            CLIUtility.success("Database connection established.")

            # Use a debug table name that is less likely to conflict
            debug_table_name = "debug_users"

            # Create a debug table
            create_table_query = f"""
            CREATE TABLE IF NOT EXISTS {debug_table_name} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL
            )
            """
            success = DBCrud.execute_query(connection, create_table_query)
            if success:
                CLIUtility.success("Debug table created successfully.")
            else:
                CLIUtility.error("Failed to create debug table.")
                return

            # Insert records into debug table
            insert_query = f"INSERT INTO {debug_table_name} (name, email) VALUES (%s, %s)"
            users = [("Alice", "alice@example.com"), ("Bob", "bob@example.com")]
            for user in users:
                DBCrud.insert_record(connection, insert_query, user)

            CLIUtility.info("Sample records inserted into debug table.")

            # Fetch all records from debug table
            select_query = f"SELECT * FROM {debug_table_name}"
            result = DBCrud.fetch_all(connection, select_query)
            if result:
                for row in result:
                    CLIUtility.info(row)
            else:
                CLIUtility.error("Failed to fetch records from debug table.")
                return

            # Update record in debug table
            update_query = f"UPDATE {debug_table_name} SET email = %s WHERE name = %s"
            update_values = ("new_email@example.com", "Alice")
            success = DBCrud.execute_query(connection, update_query, update_values)
            if success:
                CLIUtility.info("Record updated in debug table.")
            else:
                CLIUtility.error("Failed to update record in debug table.")
                return

            # Fetch one record from debug table after update
            result = DBCrud.fetch_one(connection, select_query + " WHERE name = %s", ("Alice",))
            if result:
                CLIUtility.info(result)
            else:
                CLIUtility.error("Failed to fetch updated record from debug table.")
                return

            # Delete record from debug table
            delete_query = f"DELETE FROM {debug_table_name} WHERE name = %s"
            success = DBCrud.execute_query(connection, delete_query, ("Bob",))
            if success:
                CLIUtility.info("Record deleted from debug table.")
            else:
                CLIUtility.error("Failed to delete record from debug table.")
                return

            # Clean up debug table
            success = DBCrud.execute_query(connection, f"DROP TABLE IF EXISTS {debug_table_name}")
            if success:
                CLIUtility.success("Debug table cleaned up.")
            else:
                CLIUtility.error("Failed to clean up debug table.")
                return

            CLIUtility.success("DEBUGGING COMPLETED")

        except Error as e:
            CLIUtility.error(f"Error during debugging: {e}")
        finally:
            if connection and connection.is_connected():
                DBConnection.disconnect()
                CLIUtility.info("Database connection closed.")

# Example usage for debugging directly in this module
if __name__ == "__main__":
    DBDebug.debug()
