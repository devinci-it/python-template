"""
db_connection.py

This module provides a static singleton utility class `DBConnection` for managing connections
to a MySQL database using credentials stored in environment variables.
It includes methods to establish, disconnect, check connection status, and reset the connection.

"""

from ..cli.cli import CLIUtility
from mysql.connector import Error, connect
from dotenv import load_dotenv
import os

class DBConnection:
    """
    Static singleton utility class to manage database connection.
    """

    _instance = None
    _connection = None

    @staticmethod
    def get_instance():
        """
        Returns the singleton instance of DBConnection.

        If the instance does not exist, it initializes it using environment variables.
        """
        if DBConnection._instance is None:
            DBConnection._instance = DBConnection()
        return DBConnection._instance

    @staticmethod
    def debug_banner():
        """
        Displays a debug banner showing configured credentials and server details.
        """
        load_dotenv()
        host = os.getenv("DB_HOST")
        database = os.getenv("DB_NAME")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")

        banner = f"""
        {'=' * 60}
        DEBUG BANNER: DATABASE CONFIG
        {'=' * 60}
        Host:     {host:<20}
        Database: {database:<20}
        User:     {user:<20}
        Password: {password:<20}
        """
        print(banner)

    @staticmethod
    def connect():
        """
        Establishes a connection to the MySQL database using credentials from environment variables.

        Returns:
        - connection: MySQL Connection object.
        """
        load_dotenv()
        host = os.getenv("DB_HOST")
        database = os.getenv("DB_NAME")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")

        try:
            CLIUtility.info("Connecting to MySQL database...")
            DBConnection._connection = connect(
                host=host,
                database=database,
                user=user,
                password=password
            )
            CLIUtility.success("Connected to MySQL database")
            return DBConnection._connection
        except Error as e:
            CLIUtility.error(f"Error connecting to MySQL database: {e}")
            return None

    @staticmethod
    def disconnect():
        """
        Disconnects from the MySQL database.
        """
        if DBConnection._connection and DBConnection._connection.is_connected():
            DBConnection._connection.close()
            CLIUtility.success("Disconnected successfully")

    @staticmethod
    def is_connected():
        """
        Checks if the connection to MySQL database is still active.

        Returns:
        - bool: True if connected, False otherwise.
        """
        return DBConnection._connection.is_connected() if DBConnection._connection else False

    @staticmethod
    def reset_connection():
        """
        Resets the connection to the MySQL database by reconnecting.

        Returns:
        - connection: Reconnected MySQL Connection object.
        """
        DBConnection.disconnect()
        CLIUtility.info("Resetting MySQL connection...")
        return DBConnection.connect()

# Example usage:
db = DBConnection.get_instance()
# db.connect()
# db.reset_connection()
# db.disconnect()
