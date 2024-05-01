class CommandLine:
    """
    Utility class for printing formatted messages and headers in the command-line interface.
    """

    # Class attributes for colors
    HEADER_COLOR = '\033[1;97m'  # Bright white
    INFO_COLOR = '\033[1;34m'  # Blue
    WARNING_COLOR = '\033[1;33m'  # Yellow
    ERROR_COLOR = '\033[1;31m'  # Red
    SUCCESS_COLOR = '\033[1;32m'  # Green
    DEBUG_COLOR = '\033[1;35m'  # Purple
    RESET_COLOR = '\033[0m'  # Reset color

    @staticmethod
    def header(title):
        """
        Prints a formatted header with the specified title.

        Args:
            title (str): The title of the header.
        """
        # Replace '[HEADER]' from the title
        title = title.replace('[HEADER]', '')

        print(f"{CommandLine.HEADER_COLOR}{'=' * max(150, min(120, len(title)))}{CommandLine.RESET_COLOR}")

        # Calculate padding for center alignment
        padding = max(0, (max(150, min(120, len(title))) - len(title)) // 2)
        print(f"{CommandLine.HEADER_COLOR}{' ' * padding}{title.upper()}{CommandLine.RESET_COLOR}")

        print(f"{CommandLine.HEADER_COLOR}{'=' * max(150, min(120, len(title)))}{CommandLine.RESET_COLOR}", end="\n")

    @staticmethod
    def info(message):
        """
        Prints an informational message with a prefixed INFO label.

        Args:
            message (str): The message to be printed.
        """
        print(f"{CommandLine.INFO_COLOR} INFO {' ' * 11}\u25CF {CommandLine.RESET_COLOR} {message}")

    @staticmethod
    def warning(message):
        """
        Prints a warning message with a prefixed WARNING label.

        Args:
            message (str): The message to be printed.
        """
        print(f"{CommandLine.WARNING_COLOR} WARNING {' ' * 8}\u25CF {CommandLine.RESET_COLOR} {message}")

    @staticmethod
    def error(message):
        """
        Prints an error message with a prefixed ERROR label.

        Args:
            message (str): The message to be printed.
        """
        print(f"{CommandLine.ERROR_COLOR} ERROR {' ' * 10}\u25CF {CommandLine.RESET_COLOR} {message}")

    @staticmethod
    def success(message):
        """
        Prints a success message with a prefixed SUCCESS label.

        Args:
            message (str): The message to be printed.
        """
        print(f"{CommandLine.SUCCESS_COLOR} SUCCESS {' ' * 8}\u25CF {CommandLine.RESET_COLOR} {message}")

    @staticmethod
    def debug(message):
        """
        Prints a debug message with a prefixed DEBUG label.

        Args:
            message (str): The message to be printed.
        """
        print(f"{CommandLine.DEBUG_COLOR} DEBUG {' ' * 10}\u25CF {CommandLine.RESET_COLOR} {message}")
