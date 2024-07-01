# DBConnection Module

## **Summary:**

The `DBConnection` module in Python provides a static singleton utility class for managing connections to a MySQL database. It facilitates secure credential management through environment variables and includes methods to establish, disconnect, check connection status, and reset connections as needed. This module is designed to streamline database operations and ensure reliable database connectivity for applications.

## **Features:**
- **Static Singleton:** Ensures a single instance of `DBConnection` across the application.
- **Connection Management:** Methods to connect, disconnect, and reset connections to MySQL databases.
- **Environment Variable Support:** Utilizes environment variables (`DB_HOST`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`) for secure credential storage.
- **Debug Banner:** Displays configured database credentials for debugging purposes.
- **Error Handling:** Catches and logs errors during database connection attempts.

## **Usage Example:**
```python
from db_connection import DBConnection

# Get singleton instance
db = DBConnection.get_instance()

# Connect to database
connection = db.connect()

# Perform database operations...

# Reset connection if needed
db.reset_connection()

# Disconnect from database
db.disconnect()
```
