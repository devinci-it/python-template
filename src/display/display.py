from .CONSTANTS import OFFSET ,DEFAULT_TABLE_WIDTH,TERMINAL_WIDTH,MAX_WIDTH,BORDER_STYLES
import os
import click


class Display:
    """
    A class to handle text display with various formatting options and borders.

    Attributes:
    - theme (dict): A dictionary defining color and style codes for different text elements.
    - border_style (dict): A dictionary defining border characters for different styles.
    - table_width (int): The maximum width for text display.
    """

    def __init__(self, theme, border_style='thick'):
        """
        Initialize the Display object with a specified theme and border style.

        Parameters:
        - theme (dict): A dictionary defining color and style codes for different text elements.
        - border_style (str): The style of border to use ('thin', 'double', 'medium', 'thick').
                              Default is 'thick'.
        """
        self.theme = theme
        self.border_style = BORDER_STYLES.get(border_style, BORDER_STYLES['thick'])
        self.table_width = MAX_WIDTH

    def _get_terminal_width(self):
        """
        Get the current width of the terminal window.

        Returns:
        - int: The width of the terminal window.
        """
        return min(os.get_terminal_size().columns, MAX_WIDTH)

    def format_with_border(self, message):
        """
        Print a message with a top and bottom border.

        Parameters:
        - message (str): The message to display.
        """
        content_width = self.table_width + len(self.theme['border']) + len(self.theme['reset'])
        self._print_border('top', width=content_width)
        self._print_message(message, theme=self.theme['header'], justify='center', bold=True)
        self._print_border('bottom', width=content_width)

    def _print_border(self, position, width=None):
        """
        Print a border line in the specified position.

        Parameters:
        - position (str): The position of the border ('top', 'bottom', 'line').
        - width (int): The width of the border. Defaults to terminal width.
        """
        border = self.border_style
        terminal_width = self._get_terminal_width()
        if width is None:
            width = terminal_width

        if position == 'top':
            horizontal_line = border['HORIZONTAL'] * (width - (OFFSET + 2))
            click.echo(f"{self.theme['border']}{border['TOP_LEFT']}{horizontal_line}{border['TOP_RIGHT']}{self.theme['reset']}")
        elif position == 'bottom':
            horizontal_line = border['HORIZONTAL'] * (width - (OFFSET + 2))
            click.echo(f"{self.theme['border']}{border['BOTTOM_LEFT']}{horizontal_line}{border['BOTTOM_RIGHT']}{self.theme['reset']}")
        elif position == 'line':
            horizontal_line = border['HORIZONTAL'] * width
            click.echo(f"{self.theme['border']}{border['VERTICAL']} {horizontal_line}{border['VERTICAL']}{self.theme['reset']}")

    def _print_message(self, message, theme=None, justify='left', bold=False, max_width=None, indent=0):
        """
        Print a formatted message.

        Parameters:
        - message (str or list): The message or list of messages to display.
        - theme (str): The theme for the message. Defaults to 'border' theme.
        - justify (str): The justification of the text ('left', 'right', 'center'). Defaults to 'left'.
        - bold (bool): Whether to display the text in bold. Defaults to False.
        - max_width (int): The maximum width of the message. Defaults to table width.
        - indent (int): The amount of indentation for the message. Defaults to 0.
        """
        if max_width is None:
            max_width = self.table_width
        if theme is None:
            theme = self.theme['border']

        if isinstance(message, list):
            theme = self.theme['reset']
            justify = 'left'
            for line in message:
                self._print_message(line, theme, justify, bold, max_width, indent)
            return

        # Calculate the actual length of the message without ANSI escape codes
        message_length = len(click.unstyle(message))
        available_width = max_width - indent

        # Determine the justified text based on the specified justification
        if justify == 'left':
            justified_text = message.ljust(available_width)
        elif justify == 'right':
            justified_text = message.rjust(available_width)
        else:
            justified_text = f"{message:<{available_width}}"

        # Truncate the message if it exceeds the available width
        justified_text = justified_text[:available_width]

        if indent > 0:
            justified_text = ' ' * indent + justified_text

        if bold:
            justified_text = click.style(justified_text, bold=True)

        # Print the formatted message
        click.echo(f"{self.theme['border']}{self.border_style['VERTICAL']}{self.theme['reset']}{theme} {justified_text}{self.theme['reset']}{self.theme['border']}{self.border_style['VERTICAL']}{self.theme['reset']}")

    def header(self, text, bold=False):
        """
        Print a header with centered text.

        Parameters:
        - text (str): The header text to display.
        - bold (bool): Whether to display the text in bold. Defaults to False.
        """
        return self._print_message(text.ljust(self.table_width), theme=self.theme['header'], justify='center', bold=bold)

    def footer(self, text, bold=False):
        """
        Print a footer with centered text.

        Parameters:
        - text (str): The footer text to display.
        - bold (bool): Whether to display the text in bold. Defaults to False.
        """
        return self._print_message(text.center(self.table_width), theme=self.theme['reset'], justify='center', bold=bold)

    def option(self, text, bold=False):
        """
        Print an option with left-aligned text.

        Parameters:
        - text (str): The option text to display.
        - bold (bool): Whether to display the text in bold. Defaults to False.
        """
        return self._print_message(text, justify='left', theme=self.theme['option'], bold=bold)

    def body(self, text, bold=False):
        """
        Print body text with left-aligned text.

        Parameters:
        - text (str): The body text to display.
        - bold (bool): Whether to display the text in bold. Defaults to False.
        """
        return self._print_message(text.ljust(self.table_width), theme=self.theme['body_text'], justify='left', bold=bold)

    def body_highlight(self, text, bold=False):
        """
        Print highlighted body text with left-aligned text.

        Parameters:
        - text (str): The highlighted body text to display.
        - bold (bool): Whether to display the text in bold. Defaults to False.
        """
        return self._print_message(text.ljust(self.table_width), theme=self.theme['body_highlight'], justify='left', bold=bold)

    def underline(self, text, bold=False):
        """
        Print underlined text with centered text.

        Parameters:
        - text (str): The underlined text to display.
        - bold (bool): Whether to display the text in bold. Defaults to False.
        """
        return self._print_message(text, theme=self.theme['reset'], justify='center', bold=bold)

    def key_value_pair(self, key, value, bold_key=True, bold_value=False):
        """
        Print a key-value pair with left-aligned key and indented value.

        Parameters:
        - key (str): The key text to display.
        - value (str): The value text to display.
        - bold_key (bool): Whether to display the key text in bold. Defaults to True.
        - bold_value (bool): Whether to display the value text in bold. Defaults to False.
        """
        key_str = f"{key:<{self.table_width}}"
        value_str = f"{value:<{self.table_width}}"
        self._print_message(key_str, theme=self.theme['selected_option'], justify='left', bold=bold_key)
        self._print_message(value_str, theme=self.theme['option'], justify='left', bold=bold_value, indent=4)

    def header_and_sub(self, header, sub):
        """
        Print a header with a boxed format followed by a subheader split into lines.

        Parameters:
        - header (str): The header text to display.
        - sub (str): The subheader text to display below the header.
        """
        self.format_with_border(header)
        sub_lines = [sub[i:i+75] for i in range(0, len(sub), 75)]
        self._print_message(sub_lines, theme=self.theme['subheader'], justify='center', bold=True, indent=4)
        self._print_border('line')

    def banner(self, file_path):
        """
        Display a banner read from a text file.

        Parameters:
        - file_path (str): The path to the text file containing the banner text.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                banner_text = file.read()
                lines = [line.rstrip() for line in banner_text.split("\n")]
                for line in lines:
                    self.header(line)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except Exception as e:
            print(f"Error: An unexpected error occurred - {str(e)}")

