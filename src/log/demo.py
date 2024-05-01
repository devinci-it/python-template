"""
Demo script showcasing the usage of the DevinciLog class for logging.

Imports:
    Log: The logging class from the log module.
    logging: The standard logging module.

Functions:
    test_decorator: A sample function to demonstrate logging.
    main: The main function of the script, demonstrating various logging functionalities.

Usage:
    Run this script to observe the logging output and behavior.

"""

from log import Log as DevinciLog
import logging

def test_decorator():
    """A sample function to demonstrate logging."""
    print("This is a test decorator.")
    return True

def main():
    """The main function demonstrating various logging functionalities."""
    # Initialize Log instance
    logger = DevinciLog(log_file='app.log', log_directory='logs')

    # Test decorator function
    test_decorator()

    # Log message for instance creation
    logger.info('LOGGER INSTANCE CREATED')

    # Set log level to DEBUG
    logger.set_log_level(logging.DEBUG)

    # Log some messages
    logger.header("LOGGER : SET TO DEBUG SAMPLE LOGGING")
    logger.info('This is an information message.')
    logger.error('An error occurred!')
    logger.warning('Warning: Something might be wrong.')
    logger.success('Operation completed successfully.')

    # Get and print the log path
    print(f"Log path: {logger.log_path}")

    # Change log level to DEBUG
    logger.set_log_level(logging.DEBUG)

    # Log header for changed log level
    logger.header("LOGGER : SET TO WARN SAMPLE LOGGING")

    # Call test decorator again
    test_decorator()

    # Change log format
    logger.set_log_format(
        '%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s : %(filename)s: %(lineno)d')

    # Log another message to see the changes
    logger.info('This is a debug message.')

    # Add .gitignore entry
    logger.add_gitignore()

    return True

if __name__ == "__main__":
    main()
