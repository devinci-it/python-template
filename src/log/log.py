import logging
import os

class Singleton(type):
    """
    Metaclass for creating Singleton classes.

    This metaclass ensures that only one instance of the class exists throughout
    the application lifecycle.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Call method to retrieve the singleton instance.

        If an instance of the class does not exist, it creates and stores it.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Logger(metaclass=Singleton):
    """
    Singleton Logger class for centralized logging.

    Attributes:
        log_file (str): Name of the log file.
        log_directory (str): Directory where log files are stored.
        log_level (int): Logging level (default: logging.INFO).
        log_format (str): Format for log messages (default: '%(asctime)s - %(levelname)s - %(message)s').
    """

    def __init__(self):
        """
        Initialize the logger with default attributes.
        """
        self.log_file = 'app.log'
        self.log_directory = 'storage/logs'
        self.log_level = logging.INFO
        self.log_format = '%(asctime)s - %(levelname)s - %(message)s'
        self.configure_logging()

    def configure_logging(self):
        """
        Configure logging settings based on current attributes.
        """
        if not os.path.exists(self.log_directory):
            os.makedirs(self.log_directory)

        log_path = os.path.join(self.log_directory, self.log_file)

        logging.basicConfig(filename=log_path, level=self.log_level, format=self.log_format)

    def set_log_file(self, file_name):
        """
        Set the log file and reconfigure logging.

        Args:
            file_name (str): Name of the log file.
        """
        self.log_file = file_name
        self.configure_logging()

    def set_log_directory(self, directory):
        """
        Set the log directory and reconfigure logging.

        Args:
            directory (str): Directory path for log files.
        """
        self.log_directory = directory
        self.configure_logging()

    def set_log_level(self, level):
        """
        Set the logging level and reconfigure logging.

        Args:
            level (int): Logging level (e.g., logging.INFO, logging.DEBUG).
        """
        self.log_level = level
        self.configure_logging()

    def set_log_format(self, format):
        """
        Set the log format and reconfigure logging.

        Args:
            format (str): Format string for log messages.
        """
        self.log_format = format
        self.configure_logging()

    def clear_logs(self):
        """
        Clear all log files in the log directory.
        """
        log_files = [f for f in os.listdir(self.log_directory) if f.endswith('.log')]
        for log_file in log_files:
            os.remove(os.path.join(self.log_directory, log_file))

    def add_gitignore(self):
        """
        Create a .gitignore file in the log directory to ignore log files.
        """
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

# Singleton instance of Logger
logger = Logger()
