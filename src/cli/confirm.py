import click
import sys
import os
from .themes import Theme
from .prompt_base import CLIPromptBase as pbase


class ConfirmationPrompt:

    @staticmethod
    def display_confirmation(title, header=None, context=None, confirm_text=None, okay_text=None, cancel_text=None,
                             exit_text=None, theme_name='material_dark'):
        """
        Displays a confirmation dialog with dynamic title, header, context, and options.

        Args:
        - title (str): Title of the confirmation dialog.
        - header (str, optional): Header message for the confirmation dialog. Defaults to None.
        - context (str, optional): Context or details of what is being confirmed. Defaults to None.
        - confirm_text (str, optional): Text for the confirm option. Defaults to "Okay".
        - okay_text (str, optional): Text for the okay option. Defaults to "Okay".
        - cancel_text (str, optional): Text for the cancel option. Defaults to "Cancel".
        - exit_text (str, optional): Text for the exit option. Defaults to "Exit".
        - theme_name (str): Name of the color theme to use. Defaults to 'material_dark'.
        """
        theme = Theme.get_theme(theme_name)

        terminal_width, terminal_height = os.get_terminal_size(sys.stdout.fileno())

        options = [
            confirm_text if confirm_text is not None else okay_text if okay_text is not None else "Okay",
            cancel_text if cancel_text is not None else "Cancel",
            exit_text if exit_text is not None else "Exit"
        ]

        selected_index = 0  # Initialize selected index

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen command based on OS

            # Calculate table width considering padding and margins
            table_width = min(80, terminal_width - 2)

            # Print the confirmation dialog with options
            pbase.display_top_border(table_width, theme)
            click.echo(
                f"{theme['border']}  │ {theme['header']}{title.center(table_width)}{theme['border']} │ {theme['reset']}")
            pbase.display_bottom_border(table_width, theme)

            if header:
                for line in header.splitlines():
                    pbase.display_text_border(line,table_width,theme)
                    # click.echo(
                    #     f"{theme['border']}  │ {line.ljust(table_width-4)}{theme['border']}    │  {theme['reset']} ")

            pbase.display_body_border(table_width, theme)



            for idx, option in enumerate(options):
                prefix = "├" if idx == 0 else "│" if idx < len(options) - 1 else "└"
                selected_indicator = " ←" if idx == selected_index else ""
                selected_color = theme['selected_option'] if idx == selected_index else theme['option']
                click.echo(
                    f"{theme['border']}  {prefix}  {selected_color}{option[:table_width - 8].ljust(table_width - 7)}{selected_indicator}{theme['border']}  {theme['reset']}")

#            pbase.display_bottom_border(table_width, theme)
            if context:
                for line in context.splitlines():
                    click.echo(
                        f"{theme['border']}  │ {line.ljust(table_width)}{theme['border']} │ {theme['reset']}")

            pbase.display_bottom_border(table_width, theme)
            click.echo(
                f"\n{theme['subheader']}Use arrow keys (↑/↓) to navigate, Enter to select, q to quit.{theme['reset']}")

            key = click.getchar()

            if key == '\x1b[A':  # Up arrow key
                selected_index = (selected_index - 2) % len(options)
            elif key == '\x1b[B':  # Down arrow key
                selected_index = (selected_index + 2) % len(options)
            elif key == '\r':  # Enter key
                return options[selected_index]
            elif key == 'q':  # Quit key
                sys.exit()
