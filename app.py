import configparser
import os
import logging

class AppContext:
    """
    Application context to manage configuration settings and resources.
    """
    def __init__(self):
        self.config = self.read_config()
        self.setup_logging()

    def read_config(self):
        """
        Read configuration settings from config.ini.
        """
        config = configparser.ConfigParser()
        config_file = 'config.ini'

        if os.path.exists(config_file):
            config.read(config_file)
            return config
        else:
            raise FileNotFoundError(f"Config file {config_file} not found.")

    def setup_logging(self):
        """
        Setup logging based on configuration settings.
        """
        logging_config = self.config['Logging']
        log_dir = logging_config.get('log_dir', 'logs')
        log_level = logging_config.get('log_level', 'INFO')

        # Validate log level
        log_level = getattr(logging, log_level.upper(), logging.INFO)

        # Create log directory if it doesn't exist
        os.makedirs(log_dir, exist_ok=True)

        # Configure logging
        logging.basicConfig(filename=os.path.join(log_dir, 'app.log'),
                            level=log_level,
                            format='%(asctime)s - %(levelname)s - %(message)s')

class MyApplication:
    """
    Main application class.
    """
    def __init__(self, app_context):
        self.app_context = app_context

    def run(self):
        logging.info("Application started.")
        # Your application logic goes here

if __name__ == "__main__":
    # Create the application context
    app_context = AppContext()

    # Initialize and run the application
    app = MyApplication(app_context)
    app.run()
