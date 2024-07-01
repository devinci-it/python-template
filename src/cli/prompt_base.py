import click
from tabulate import tabulate
from .themes import Theme
from .helper import get_terminal_size

class CLIPromptBase:

    @staticmethod
    def display_top_border(table_width, theme):
        """
        Displays the top border section of the select prompt.

        Args:
        - table_width (int): Width of the table for proper formatting.
        - theme (dict): Theme dictionary containing ANSI escape sequences.
        """
        border_line_top = f"{theme['border']}  ┌{'─' * (table_width + 2)}┐{theme['reset']}"
        click.echo(border_line_top)

    @staticmethod
    def display_body_border(table_width, theme):
        """
        Displays the body border section of the select prompt.

        Args:
        - table_width (int): Width of the table for proper formatting.
        - theme (dict): Theme dictionary containing ANSI escape sequences.
        """
        border_line_middle = f"{theme['border']}  ├{'─' * (table_width + 2)}┤{theme['reset']}"
        return border_line_middle

    @staticmethod
    def display_bottom_border(table_width, theme):
        """
        Displays the bottom border section of the select prompt.

        Args:
        - table_width (int): Width of the table for proper formatting.
        - theme (dict): Theme dictionary containing ANSI escape sequences.
        """
        border_line_bottom = f"{theme['border']}  └{'─' * (table_width + 2)}┘{theme['reset']}"
        click.echo(border_line_bottom)


    @staticmethod
    def display_header(prompt_header, table_width, theme):
        """
        Displays the header section of the select prompt.

        Args:
        - prompt_header (str): Header message for the select menu.
        - table_width (int): Width of the table for proper formatting.
        - theme (dict): Theme dictionary containing ANSI escape sequences.
        """
        border_line_top = f"{theme['border']}  ┌{'─' * (table_width + 2)}┐{theme['reset']}"
        header_line = f"{theme['border']}  │{theme['header']}{prompt_header.center(table_width)}{theme['border']}  │{theme['reset']}"
        border_line_bottom = f"{theme['border']}  └{'─' * (table_width + 2)}┘{theme['reset']}"
        click.echo(border_line_top)
        click.echo(header_line)
        click.echo(border_line_bottom)

    @staticmethod
    def display_subheader(prompt_sub, table_width, theme):
        """
        Displays the subheader section of the select prompt.

        Args:
        - prompt_sub (str): Sub/context message for the select menu.
        - table_width (int): Width of the table for proper formatting.
        - theme (dict): Theme dictionary containing ANSI escape sequences.
        """
        CLIPromptBase.display_top_border(table_width,theme)

        CLIPromptBase.display_cb_text_border( prompt_sub,table_width,theme)



    @staticmethod
    def display_text_border(text, table_width, theme):
        """
        Displays the body border section of the select prompt with centered text.

        Args:
        - text (str): Text message to be centered within the body border.
        - table_width (int): Width of the table for proper formatting.
        - theme (dict): Theme dictionary containing ANSI escape sequences.
        """
        centered_text = text.center(table_width)
        border_line_middle = f"{theme['border']}  ├{'─' * (table_width + 2)}┤{theme['reset']}"
        click.echo(border_line_middle)
        click.echo(f"{theme['border']}  │{centered_text}{theme['border']}  │{theme['reset']}")
        click.echo(border_line_middle)

    @staticmethod
    def display_cb_text_border(text, table_width, theme,justify= 'center'):
        """
        Displays the bottom border section of the select prompt with centered text.

        Args:
        - text (str): Text message to be centered within the bottom border.
        - table_width (int): Width of the table for proper formatting.
        - theme (dict): Theme dictionary containing ANSI escape sequences.
         - justify (str): Justification for the text ('left', 'right', 'center'). Defaults to 'center'.
        """
        if justify == 'left':
            centered_text = f"{text.ljust(table_width)}"
        elif justify == 'right':
            centered_text = f"{text.rjust(table_width)}"
        else:  # Default to center justify
            centered_text = f"{text.center(table_width)}"

        border_line_bottom = f"{theme['border']}  └{'─' * (table_width + 2)}┘{theme['reset']}"
        click.echo(f"{theme['border']}  │{theme['subheader']}{centered_text}{theme['border']}  │{theme['reset']}")
        click.echo(border_line_bottom)

    @staticmethod
    def display_options(options, selected_indices, theme, option_header=None, multi_select=False):
        """
        Displays the options section of the select prompt.

        Args:
        - options (list): List of options to display in the menu.
        - selected_indices (list): List of indices that are currently selected.
        - theme (dict): Theme dictionary containing ANSI escape sequences.
        - option_header (str or None): Optional header for the options section.
        - multi_select (bool): Whether multi-select is enabled.

        """
        table = []

        if option_header is not None:
            header_line = f"{theme['option']} {option_header} {theme['reset']}\n"
            click.echo(header_line)
            CLIPromptBase.display_bottom_border(80,theme)
            click.echo()  # Print a blank line after the header
            CLIPromptBase.display_text_border(option_header, 80, theme)


        CLIPromptBase.display_top_border(80, theme)

        for index, option in enumerate(options):
            if index == 0:
                click.echo()  # Print a blank line before the first option

            if index in selected_indices:
                formatted_option = f"{theme['border']}  ├\t{theme['selected_option']}{option}{theme['reset']}"
            else:
                formatted_option = f"{theme['border']}    \t{theme['option']}{option}{theme['reset']}"
            table.append([formatted_option])

        table_output = tabulate(table, headers=[''], tablefmt='plain', showindex=False)
        click.echo(f'\t{table_output}')
        click.echo(f"\n{theme['subheader']}{theme['reset']}\n")

        CLIPromptBase.display_bottom_border(80, theme)
