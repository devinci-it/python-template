
import logging
import os
from cli import cli as DevinciCLI

class Log:
    """
    Module providing logging functionality for the application.
    """

    def __init__(self, log_file, log_directory):
        """
        Initialize the Log instance.

        Args:
            log_file (str): The name of the log file.
            log_directory (str): The directory where log files will be stored.
        """
        self.log_file = log_file
        self.log_directory = log_directory
        self._initialize_cli()
        self.configure_logging()
        self.log_format = '%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s'

    def _initialize_cli(self):
        """Initialize CLI instance."""
        self.cli = DevinciCLI.CommandLine()

    def configure_logging(self, log_level=logging.INFO, log_format=None):
        """
        Configure logging settings.

        Args:
            log_level (int, optional): The log level (default: logging.INFO).
            log_format (str, optional): The format of log messages (default: None).
        """
        if log_format is None:
            log_format = self.set_log_format

        self.info(f"Logging configured: level={log_level}, format={log_format}")

        if not os.path.exists(self.log_directory):
            os.makedirs(self.log_directory)

        log_path = os.path.join(self.log_directory, self.log_file)
        if not os.path.exists(log_path):
            open(log_path, 'a').close()

        logging.basicConfig(filename=log_path, level=log_level, format=log_format)

    def log_message(self, log_level, message):
        """
        Logs a message with the specified log level.

        Args:
            log_level (str): The log level.
            message (str): The message to log.
        """
        convert_log_level = lambda level: {
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL,
        }.get(level, logging.NOTSET)

        level_int = convert_log_level(
            log_level)  # Convert level name to integer
        log_message = f"[{log_level}] {message}"
        getattr(self.cli, log_level)(log_message)
        self.log(log_message, level=level_int)

    def log_decorator(self, log_level):
        """
        Decorator function to simplify logging calls.

        Args:
            log_level (str): The log level.

        Returns:
            function: The decorated function.
        """
        def decorator(func):
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                message = f"{func.__name__} returned: {result}"
                self.log_message(log_level, message)
                return result
            return wrapper
        return decorator

    def debug_log_decorator(self, func):
        """
        Decorator function to log debug messages for functions.

        Args:
            func (function): The function to decorate.

        Returns:
            function: The decorated function.
        """
        def wrapper(*args, **kwargs):
            self.debug(f"Calling function '{func.__name__}' with arguments {args} and keyword arguments {kwargs}")
            result = func(*args, **kwargs)
            self.debug(f"Function '{func.__name__}' returned: {result}")
            return result
        return wrapper

    def header(self, message):
        """
        Logs a message with header level.

        Args:
            message (str): The message to log.
        """
        self.log_message('header', message)

    def debug(self, message):
        """
        Log a message with DEBUG level.

        Args:
            message (str): The message to log.
        """
        self.log_message('debug', message)

    def info(self, message):
        """
        Logs a message with info level.

        Args:
            message (str): The message to log.
        """
        self.log_message('info', message)

    def error(self, message):
        """
        Logs a message with error level.

        Args:
            message (str): The message to log.
        """
        self.log_message('error', message)

    def warning(self, message):
        """
        Logs a message with warning level.

        Args:
            message (str): The message to log.
        """
        self.log_message('warning', message)

    def success(self, message):
        """
        Logs a message with success level.

        Args:
            message (str): The message to log.
        """
        self.log_message('success', message)

    def clear_logs(self):
        """Clear log files."""
        log_files = [f for f in os.listdir(self.log_directory) if f.endswith('.log')]
        for log_file in log_files:
            os.remove(os.path.join(self.log_directory, log_file))

    def add_gitignore(self):
        """Add entries to .gitignore."""
        gitignore_path = os.path.join(self.log_directory, '.gitignore')
        with open(gitignore_path, 'w') as f:
            f.write("*.log\n")

    def log(self, message, level=logging.INFO):
        """
        Log a message with the specified log level.

        Args:
            message (str): The message to log.
            level (int, optional): The log level (default: logging.INFO).
        """
        logging.log(level, message)

    @property
    def log_path(self):
        """Return the path to the log file."""
        return os.path.join(self.log_directory, self.log_file)

    def set_log_level(self, log_level):
        """
        Change the log level.

        Args:
            log_level (int): The log level.
        """
        logging.getLogger().setLevel(log_level)

    def set_log_format(self, log_format):
        """
        Change the log format.

        Args:
            log_format (str): The format of log messages.
        """
        logging.getLogger().handlers[0].setFormatter(logging.Formatter(log_format))
