import configparser

class Config:
    """
    Utility class for handling configuration settings using configparser.

    Attributes:
        config (ConfigParser): ConfigParser instance to manage configuration settings.
    """

    def __init__(self, config_file='config.ini'):
        """
        Initializes the Config object.

        Args:
            config_file (str, optional): Path to the configuration file. Defaults to 'config.ini'.
        """
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get(self, section, key):
        """
        Retrieves a value from the configuration.

        Args:
            section (str): The section in the configuration file.
            key (str): The key whose value needs to be retrieved.

        Returns:
            str: The value corresponding to the key in the specified section.
        """
        return self.config[section][key]

    def get_logging_format(self):
        """
        Retrieves the logging format from the configuration.

        Returns:
            str: The logging format string.
        """
        return self.config.get('Logging', 'format', fallback='%(asctime)s - %(filename)s - %(levelname)s - %(message)s')

    def verify_config(self):
        """
        Verifies if the configuration file contains required sections and keys.

        Returns:
            bool: True if all required sections and keys are present, False otherwise.
        """
        required_sections = ['General', 'Logging', 'Features']
        required_keys = {
            'General': ['AppName'],
            'Logging': ['LogLevel', 'LogPath'],
            # Add more required keys for other sections as needed
        }

        for section in required_sections:
            if section not in self.config:
                return False  # Missing section

            for key in required_keys[section]:
                if key not in self.config[section]:
                    return False  # Missing key

        return True  # All required sections and keys are present

    @staticmethod
    def generate_config_template():
        """
        Generates a template configuration file.

        Creates a template configuration file with default sections and options.

        Example:
            [General]
            AppName = MyApp

            [Logging]
            LogLevel = DEBUG
            LogPath = /path/to/logs

            [Features]
            EnableFeature = True
        """
        config = configparser.ConfigParser()

        config['General'] = {
            'AppName': 'MyApp',
            # Add more general configuration options as needed
        }

        config['Logging'] = {
            'LogLevel': 'DEBUG',
            # Possible log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
            'LogPath': '/path/to/logs',
            # Add more logging configuration options as needed
        }

        config['Features'] = {
            'EnableFeature': 'True',
            # Add more feature configuration options as needed
        }

        with open('config.ini', 'w') as configfile:
            config.write(configfile)
