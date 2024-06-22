"""
This script initializes a MySQL database by performing the following steps:

1. Takes user input for database host, name, user, and password securely.
2. Generates an SQL initialization script that creates the database, user, and grants privileges.
3. Executes the SQL script using subprocess with MariaDB's command line tool.
4. Removes sensitive information (passwords) from the SQL script after execution.
5. Writes database credentials to a .env file for secure storage.
6. Tests the database connection using the provided credentials.

Dependencies:
- Python packages: mysql-connector-python, dotenv
- External tools: MariaDB (required for subprocess execution)

Usage:
Ensure MariaDB is installed and the 'mariadb' command is available in the system PATH.
Run the script and follow the prompts to initialize the database.

Logging:
Logs are written to 'init_db.log' with detailed information about script execution.

Note:
Ensure proper permissions are set for sensitive files like the .env file (chmod 650).

Author: devinci-it
Date: 2024 06
"""


import os
import getpass
import subprocess
import mysql.connector
from mysql.connector import Error
from src.cli import CLIUtility
import logging
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(filename='init_db.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InitDB:
    @staticmethod
    def init_database():
        """
        Initializes the database based on user input, generates SQL scripts,
        executes them using subprocess, removes sensitive information,
        writes database credentials to .env file, and tests database connection.
        """
        try:
            db_host = input("Enter database host: ")
            db_name = input("Enter database name: ")
            db_user = input("Enter database user: ")
            db_password = getpass.getpass(prompt="Enter database password: ")

            # Log CLI banner
            CLIUtility.header("DATABASE INITIALIZATION")

            script_path = "scripts/db/init.sql"
            if os.path.exists(script_path):
                choice = input(f"Initialization script '{script_path}' already exists. Overwrite? (y/n): ").lower()
                if choice != 'y':
                    CLIUtility.info("Initialization aborted.")
                    return

            InitDB._generate_sql_script(script_path, db_host, db_name, db_user, db_password)

            # Log subprocess execution
            logging.info(f"Running SQL initialization script: {script_path}")
            subprocess.run(f"sudo mariadb -u root < {script_path}", shell=True, check=True)
            logging.info("SQL initialization script executed successfully")

            InitDB._remove_sensitive_info_from_script(script_path)

            InitDB._write_env_file(db_host, db_name, db_user, db_password)

            # Test database connection
            InitDB._test_db_connection(db_host, db_name, db_user, db_password)

        except Error as e:
            CLIUtility.error(f"Error initializing database: {e}")
            logging.error(f"Error initializing database: {e}")
        except IOError as e:
            CLIUtility.error(f"Error writing environment file: {e}")
            logging.error(f"Error writing environment file: {e}")
        finally:
            if os.path.exists(script_path):
                InitDB._remove_sensitive_info_from_script(script_path)

    @staticmethod
    def _generate_sql_script(script_path, db_host, db_name, db_user, db_password):
        """
        Generates or updates the SQL initialization script with database credentials.
        """
        try:
            with open(script_path, "w") as sql_file:
                sql_file.write(f"CREATE DATABASE IF NOT EXISTS {db_name};\n")
                sql_file.write(f"CREATE USER IF NOT EXISTS '{db_user}'@'{db_host}' IDENTIFIED BY '{db_password}';\n")
                sql_file.write(f"GRANT ALL PRIVILEGES ON {db_name}.* TO '{db_user}'@'{db_host}' WITH GRANT OPTION;\n")

            CLIUtility.success(f"Initialization script '{script_path}' generated.")

        except IOError as e:
            CLIUtility.error(f"Error generating SQL script: {e}")
            logging.error(f"Error generating SQL script: {e}")

    @staticmethod
    def _remove_sensitive_info_from_script(script_path):
        """
        Removes sensitive information (passwords) from the SQL script after execution.
        """
        try:
            with open(script_path, "r+") as sql_file:
                lines = sql_file.readlines()
                sql_file.seek(0)
                for line in lines:
                    if 'IDENTIFIED BY' not in line:
                        sql_file.write(line)
                sql_file.truncate()

            CLIUtility.success(f"Sensitive information removed from '{script_path}'.")

        except IOError as e:
            CLIUtility.error(f"Error removing sensitive information from script: {e}")
            logging.error(f"Error removing sensitive information from script: {e}")

    @staticmethod
    def _write_env_file(db_host, db_name, db_user, db_password):
        """
        Writes database credentials to a .env file and sets secure permissions.
        """
        try:
            env_file_path = ".env"
            with open(env_file_path, "w") as env_file:
                env_file.write(f"DB_HOST={db_host}\n")
                env_file.write(f"DB_NAME={db_name}\n")
                env_file.write(f"DB_USER={db_user}\n")
                env_file.write(f"DB_PASSWORD={db_password}\n")

            os.chmod(env_file_path, 0o650)  # Set secure permissions on .env file

            CLIUtility.success(f"Environment variables written to '{env_file_path}'.")

        except IOError as e:
            CLIUtility.error(f"Error writing environment file: {e}")
            logging.error(f"Error writing environment file: {e}")

    @staticmethod
    def _test_db_connection(db_host, db_name, db_user, db_password):
        """
        Tests the database connection using the provided credentials.
        """
        try:
            connection = mysql.connector.connect(
                host=db_host,
                database=db_name,
                user=db_user,
                password=db_password
            )

            if connection.is_connected():
                connection.close()
                CLIUtility.success("Database connection test successful.")
            else:
                CLIUtility.error("Failed to establish database connection.")
                logging.error("Failed to establish database connection.")

        except Error as e:
            CLIUtility.error(f"Error connecting to database: {e}")
            logging.error(f"Error connecting to database: {e}")

    @staticmethod
    def _generate_sql_script(script_path, db_host, db_name, db_user, db_password):
        """
        Generates or updates the SQL initialization script with database credentials.
        """
        try:
            with open(script_path, "w") as sql_file:
                sql_file.write(f"CREATE DATABASE IF NOT EXISTS {db_name};\n")
                sql_file.write(f"CREATE USER IF NOT EXISTS '{db_user}'@'{db_host}' IDENTIFIED BY '{db_password}';\n")
                sql_file.write(f"GRANT ALL PRIVILEGES ON {db_name}.* TO '{db_user}'@'{db_host}' WITH GRANT OPTION;\n")

            CLIUtility.success(f"Initialization script '{script_path}' generated.")

        except IOError as e:
            CLIUtility.error(f"Error generating SQL script: {e}")
            logging.error(f"Error generating SQL script: {e}")

    @staticmethod
    def _remove_sensitive_info_from_script(script_path):
        """
        Removes sensitive information (passwords) from the SQL script after execution.
        """
        try:
            with open(script_path, "r+") as sql_file:
                lines = sql_file.readlines()
                sql_file.seek(0)
                for line in lines:
                    if 'IDENTIFIED BY' not in line:
                        sql_file.write(line)
                sql_file.truncate()

            CLIUtility.success(f"Sensitive information removed from '{script_path}'.")

        except IOError as e:
            CLIUtility.error(f"Error removing sensitive information from script: {e}")
            logging.error(f"Error removing sensitive information from script: {e}")

    @staticmethod
    def _write_env_file(db_host, db_name, db_user, db_password):
        """
        Writes database credentials to a .env file and sets secure permissions.
        """
        try:
            env_file_path = ".env"
            with open(env_file_path, "w") as env_file:
                env_file.write(f"DB_HOST={db_host}\n")
                env_file.write(f"DB_NAME={db_name}\n")
                env_file.write(f"DB_USER={db_user}\n")
                env_file.write(f"DB_PASSWORD={db_password}\n")

            os.chmod(env_file_path, 0o650)  # Set secure permissions on .env file

            CLIUtility.success(f"Environment variables written to '{env_file_path}'.")

        except IOError as e:
            CLIUtility.error(f"Error writing environment file: {e}")
            logging.error(f"Error writing environment file: {e}")

    @staticmethod
    def _test_db_connection(db_host, db_name, db_user, db_password):
        """
        Tests the database connection using the provided credentials.
        """
        try:
            connection = mysql.connector.connect(
                host=db_host,
                database=db_name,
                user=db_user,
                password=db_password
            )

            if connection.is_connected():
                connection.close()
                CLIUtility.success("Database connection test successful.")
            else:
                CLIUtility.error("Failed to establish database connection.")
                logging.error("Failed to establish database connection.")

        except Error as e:
            CLIUtility.error(f"Error connecting to database: {e}")
            logging.error(f"Error connecting to database: {e}")

if __name__ == "__main__":
    InitDB.init_database()
