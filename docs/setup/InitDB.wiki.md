# `init_db.py` 
## InitDB Script: Initializing a MySQL Database

**Overview:**
The `InitDB` script automates the initialization process for a MySQL database. It prompts users for essential database configuration details, generates SQL scripts, executes them securely, and manages sensitive information. The script is designed to streamline database setup tasks, ensuring efficiency and security.

**Key Features:**
1. **User Input**: Users are prompted for database host, name, user, and password using secure input methods.
   
2. **SQL Script Generation**: Automatically generates SQL scripts (`init.sql`) that create the specified database, user, and grant necessary privileges.

3. **Execution and Security**:
   - Utilizes subprocess to execute SQL scripts securely via MariaDB's command line tool.
   - Removes sensitive information (like passwords) from the generated SQL script post-execution to maintain security.

4. **Environment Setup**:
   - Writes database credentials securely to a `.env` file, ensuring sensitive data is stored safely.
   - Sets appropriate permissions (`chmod 650`) on the `.env` file to restrict access.

5. **Database Connection Testing**: Validates the database connection using the provided credentials to ensure successful setup.

**Usage Instructions:**
- **Prerequisites**: Ensure MariaDB is installed and accessible via the `mariadb` command.
- **Execution**: Run the script and follow the prompts to enter database details.
- **Logging**: Detailed logs (`init_db.log`) provide insights into script execution and any encountered errors.

**Dependencies:**
- **Python Packages**: `mysql-connector-python`, `dotenv`
- **External Tools**: MariaDB (for SQL script execution)

**Example Script:**
```python
# Sample usage
if __name__ == "__main__":
    InitDB.init_database()
```

**Author and Date:**
- **Author**: devinci-it
- **Creation Date**: 06-22-2024

**Additional Notes:**
- Ensure proper configuration and permissions management to maintain database and file security.
- Customize script behavior or error handling as per specific project requirements.

This script offers a structured approach to database initialization, suitable for projects requiring automated setup and secure management of database credentials.
