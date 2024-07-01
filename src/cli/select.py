import click
import os
import sys
from tabulate import tabulate
from .themes import Theme
from .prompt_base import CLIPromptBase as  pbase

class CLISelectPrompt:

    @staticmethod
    def select(prompt_header, prompt_sub, options, default_index=0, theme_name='material_dark'):
        """
        Displays a select prompt and returns selected option(s).

        Args:
        - prompt_header (str): Header message for the select menu.
        - prompt_sub (str): Sub/context message for the select menu.
        - options (list): List of options to display in the menu.
        - default_index (int): Default index to highlight/select.
        - theme_name (str): Name of the color theme to use.

        Returns:
        - str or list: Selected option or list of selected options.
        """
        theme = Theme.get_theme(theme_name)

        selected_indices = [default_index]

        terminal_width, terminal_height = os.get_terminal_size(sys.stdout.fileno())

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen command based on OS

            # Calculate table width considering padding and margins
            table_width = min(80, terminal_width - 4)

            # Print the header and subheader with bold borders
            pbase.display_header(prompt_header, table_width, theme)

            # Print the options
            pbase.display_options(options, selected_indices, theme)
            pbase.display_subheader(prompt_sub, table_width, theme)

            # if len(options) > 1:
            #     click.echo(f"\nUse arrow keys (↑/↓) to navigate, Enter to select, q to quit.")
            # else:
            #     click.echo(f"\nPress Enter to select, q to quit.")

            key = click.getchar()

            if key == '\x1b[A':  # Up arrow key
                selected_indices[0] = (selected_indices[0] - 1) % len(options)
            elif key == '\x1b[B':  # Down arrow key
                selected_indices[0] = (selected_indices[0] + 1) % len(options)
            elif key == '\r':  # Enter key
                return options[selected_indices[0]]
            elif key == 'q':  # Quit key
                sys.exit()  # Exit the program
