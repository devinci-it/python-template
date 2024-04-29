class CLIUtility:
    """
    Utility class for printing formatted messages and headers in the command-line interface.
    """

    @staticmethod
    def header(title):
        """
        Prints a formatted header with the specified title.

        Args:
            title (str): The title of the header.
        """
        # ANSI escape code for bright white text color
        color_code = '\033[1;97m'
        reset_code = '\033[0m'

        print(f"{color_code}{'=' * max(80, min(80, len(title)))}{reset_code}")

        # Calculate padding for center alignment
        padding = max(0, (max(80, min(80, len(title))) - len(title)) // 2)
        print(f"{color_code}{' ' * padding}{title.upper()}{reset_code}")

        print(f"{color_code}{'=' * max(80, min(80, len(title)))}"
              f"{reset_code}",end="\n")

    @staticmethod
    def info(message):
        """
        Prints an informational message with a prefixed INFO label.

        Args:
            message (str): The message to be printed.
        """
        print(f"\033[1;36m INFO {' ' * 11}\u25CF \033[0m {message}")

    @staticmethod
    def warning(message):
        """
        Prints a warning message with a prefixed WARNING label.

        Args:
            message (str): The message to be printed.
        """
        print(f"\033[1;33m WARNING {' ' * 8}\u25CF \033[0m {message}")

    @staticmethod
    def error(message):
        """
        Prints an error message with a prefixed ERROR label.

        Args:
            message (str): The message to be printed.
        """
        print(f"\033[1;31m ERROR {' ' * 10}\u25CF \033[0m {message}")

    @staticmethod
    def success(message):
        """
        Prints a success message with a prefixed SUCCESS label.

        Args:
            message (str): The message to be printed.
        """
        print(f"\033[1;32m SUCCESS {' ' * 8}\u25CF \033[0m {message}")
