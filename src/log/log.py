import logging
import os

class Log:
    log_file = 'app.log'
    log_directory = 'storage/logs'

    @staticmethod
    def configure_logging(log_level=logging.INFO, log_format='%(asctime)s - %(levelname)s - %(message)s'):
        if not os.path.exists(Log.log_directory):
            os.makedirs(Log.log_directory)

        log_path = os.path.join(Log.log_directory, Log.log_file)

        logging.basicConfig(filename=log_path, level=log_level, format=log_format)

    @classmethod
    def set_log_file(cls, file_name):
        cls.log_file = file_name

    @classmethod
    def set_log_directory(cls, directory):
        cls.log_directory = directory

    @staticmethod
    def clear_logs():
        log_files = [f for f in os.listdir(Log.log_directory) if f.endswith('.log')]
        for log_file in log_files:
            os.remove(os.path.join(Log.log_directory, log_file))

    @staticmethod
    def add_gitignore():
        gitignore_path = os.path.join(Log.log_directory, '.gitignore')
        with open(gitignore_path, 'w') as f:
            f.write("*.log\n")

    @staticmethod
    def log(message, level=logging.INFO):
        """
        Log a message with the specified log level.

        Args:
            message (str): The message to log.
            level (int, optional): The log level (default: logging.INFO).
        """
        logging.log(level, message)
