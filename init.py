"""
init.py

This script initializes the database and handles environment setup for the application.

It performs the following tasks:
1. Clears the terminal screen for a clean interface.
2. Initializes the database using InitDB class from scripts.init_db module.
3. Reloads environment variables from .env file after initializing the database.
4. Attempts to connect to the database using db_connector.db object.
5. Logs connection status and handles exceptions gracefully.

Usage:
- Ensure to have a .env file with appropriate database credentials (DB_HOST, DB_NAME, DB_USER, DB_PASSWORD).
- Execute `python init.py` to run this script and initialize the database.

"""

import os
import subprocess
from dotenv import load_dotenv
from src.cli import CLIUtility
from scripts.init_db import InitDB
from src.database import DBDebug
from src.database import DBConnection as dbcon
def main():
    subprocess.run(['clear'])
    CLIUtility.header("Database Initialization")

    db_initializer = InitDB()
    #db_initializer.init_database()
    dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '.env'))


    try:
        from src.database.db_connection import db
        load_dotenv()
        db.connect()
        # db.debug_banner()
        if db.is_connected():
            debugger=DBDebug()
            debugger.debug()
            CLIUtility.success("Database connection established.")
        else:
            CLIUtility.error("Failed to establish database connection.")
    except Exception as e:
        CLIUtility.error(f"Error connecting to database: {e}")
    finally:
        db.disconnect()
        CLIUtility.info("Database connection closed.")

if __name__ == "__main__":
    main()

