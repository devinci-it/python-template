import logging
import configparser
import os
import inspect


class App:
    """Class representing the main application."""

    def __init__(self, log, config, cli):
        """
        Initialize the App.

        Args:
            log (Log): The logging utility instance.
            config (ConfigParser): The configuration parser instance.
            cli (CLIUtility): The command-line interface utility instance.
        """
        self.app_name = None
        self.log_level = None
        self.log = log
        self.cli = cli
        self.config = config

    def setup_logging(self):
        """Set up logging configuration."""

        log_format = '%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s'
        logging.basicConfig(level=self.log_level, format=log_format)

    def parse_config(self):
        """Parse configuration file and set configuration values."""
        try:
            self.app_name = self.config.get('General', 'AppName')
            self.log_level = int(self.config.get('Logging', 'LogLevel'))
            return True
        except Exception as e:
            self.cli.error(f"Parsing error occurred: {str(e)}")
            return False

    def log_decorator(log_level):
        """Decorator function to simplify logging calls."""

        def decorator(func):
            def wrapper(self, message):
                func(self, message)
                log_message = f"[{log_level.upper()}] {message}"
                if log_level == "info":
                    self.cli.info(log_message)
                    self.log.log(log_message)
                elif log_level == "error":
                    self.cli.error(log_message)
                    self.log.log(log_message)
                elif log_level == "warning":
                    self.cli.warning(log_message)
                    self.log.log(log_message)
                elif log_level == "success":
                    self.cli.success(log_message)
                    self.log.log(log_message)

            return wrapper

        return decorator

    @log_decorator("info")
    def info(self, message):
        """Log an informational message."""
        pass

    @log_decorator("error")
    def error(self, message):
        """Log an error message."""
        pass

    @log_decorator("warning")
    def warning(self, message):
        """Log a warning message."""
        pass

    @log_decorator("success")
    def success(self, message):
        """Log a success message."""
        pass

    def run(self):
        """Main method to run the application."""
        try:
            self.info("Now running `app.py`.")
            self.cli.header(f"Welcome")
            self._initialize_configuration()
            self.success("Initialization successful.")
            self.cli.header(f"Logging Config")
            self.info("Attempting to initialize logging configurations.")
            self._initialize_logging()
            self._initialize_application()
        except Exception as e:
            self._handle_error(e)

    def _initialize_configuration(self):
        """Initialize configuration parsing."""
        self.info("Initializing configuration parsing.")
        if self.parse_config():
            self.success("Configuration parsing successful.")
        else:
            self.error("Parsing error occurred")
            raise RuntimeError("Configuration parsing failed")

    def _initialize_logging(self):
        """Initialize logging."""
        self.info("Setting up logging.")
        self.setup_logging()
        self.success("Logging setup successful.")

    def _initialize_application(self):
        """Initialize the application."""
        self.info(" Application initializing.")
        self.cli.header(f"Running {self.app_name}")
        self.success(f"{self.app_name} started.")

    def _handle_error(self, error):
        """Handle application errors."""
        self.error(f"Error running the application: {str(error)}")
