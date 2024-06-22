"""
`db_crud.py` | Module for performing basic CRUD operations on a MySQL database using a provided connection.

This module provides methods to execute SQL queries for CRUD operations (Create, Read, Update, Delete) on
MySQL databases. It utilizes a MySQL Connection object from `db_connection.DBConnection` for database
interaction.

Usage:
- Ensure a valid MySQL database connection is established using `DBConnection.get_instance()`.
- Use the provided methods to execute SQL queries for CRUD operations:
  - `execute_query(connection, query, values=None)`: Executes a SQL query.
  - `fetch_all(connection, query, values=None)`: Fetches all records based on a SELECT query.
  - `fetch_one(connection, query, values=None)`: Fetches a single record based on a SELECT query.
  - `insert_record(connection, query, values)`: Inserts a record into the database.
  - `update_record(connection, query, values)`: Updates a record in the database.
  - `delete_record(connection, query, values)`: Deletes a record from the database.

Dependencies:
- Python packages: mysql-connector-python

Author: devinci-it
Date: 2024 06
"""


from mysql.connector import Error
from .db_connection import DBConnection

class DBCrud:
    """
    A utility class to perform basic CRUD operations on the MySQL database.
    """

    @staticmethod
    def _get_cursor(connection):
        """
        Helper method to get a cursor from the connection.

        Args:
        - connection: MySQL Connection object.

        Returns:
        - cursor: MySQL cursor object.
        """
        try:
            cursor = connection.cursor()
            return cursor
        except Error as e:
            print(f"Error getting cursor: {e}")
            return None

    @staticmethod
    def _close_cursor(cursor):
        """
        Helper method to close the cursor.

        Args:
        - cursor: MySQL cursor object.
        """
        try:
            if cursor:
                cursor.close()
        except Error as e:
            print(f"Error closing cursor: {e}")

    @staticmethod
    def execute_query(connection, query, values=None):
        """
        Executes a SQL query on the MySQL database.
        
        Args:
        - connection: MySQL Connection object.
        - query (str): The SQL query to execute.
        - values (tuple): Optional. Values to be substituted into the query.
        
        Returns:
        - cursor: MySQL cursor object for fetching results.
        """
        cursor = None
        try:
            cursor = DBCrud._get_cursor(connection)
            if cursor:
                if values:
                    cursor.execute(query, values)
                else:
                    cursor.execute(query)
                connection.commit()
                return cursor
        except Error as e:
            print(f"Error executing query: {e}")
        finally:
            DBCrud._close_cursor(cursor)

        return None

    @staticmethod
    def fetch_all(connection, query, values=None):
        """
        Fetches all records from the MySQL database based on the query.
        
        Args:
        - connection: MySQL Connection object.
        - query (str): The SELECT SQL query to execute.
        - values (tuple): Optional. Values to be substituted into the query.
        
        Returns:
        - list: List of tuples containing fetched rows.
        """
        cursor = None
        try:
            cursor = DBCrud._get_cursor(connection)
            if cursor:
                if values:
                    cursor.execute(query, values)
                else:
                    cursor.execute(query)
                result = cursor.fetchall()
                return result
        except Error as e:
            print(f"Error fetching all records: {e}")
        finally:
            DBCrud._close_cursor(cursor)

        return []

    @staticmethod
    def fetch_one(connection, query, values=None):
        """
        Fetches a single record from the MySQL database based on the query.
        
        Args:
        - connection: MySQL Connection object.
        - query (str): The SELECT SQL query to execute.
        - values (tuple): Optional. Values to be substituted into the query.
        
        Returns:
        - tuple: A single fetched row.
        """
        cursor = None
        try:
            cursor = DBCrud._get_cursor(connection)
            if cursor:
                if values:
                    cursor.execute(query, values)
                else:
                    cursor.execute(query)
                result = cursor.fetchone()
                return result
        except Error as e:
            print(f"Error fetching one record: {e}")
        finally:
            DBCrud._close_cursor(cursor)

        return None

    @staticmethod
    def insert_record(connection, query, values):
        """
        Inserts a record into the MySQL database.
        
        Args:
        - connection: MySQL Connection object.
        - query (str): The INSERT SQL query to execute.
        - values (tuple): Values to be inserted into the query.
        """
        DBCrud.execute_query(connection, query, values)

    @staticmethod
    def update_record(connection, query, values):
        """
        Updates a record in the MySQL database.
        
        Args:
        - connection: MySQL Connection object.
        - query (str): The UPDATE SQL query to execute.
        - values (tuple): Values to be updated in the query.
        """
        DBCrud.execute_query(connection, query, values)

    @staticmethod
    def delete_record(connection, query, values):
        """
        Deletes a record from the MySQL database.
        
        Args:
        - connection: MySQL Connection object.
        - query (str): The DELETE SQL query to execute.
        - values (tuple): Values to be deleted from the query.
        """
        DBCrud.execute_query(connection, query, values)
