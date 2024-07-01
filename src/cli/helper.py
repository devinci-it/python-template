import subprocess
import re

def get_terminal_size():
    try:
        columns = int(subprocess.check_output(['tput', 'cols']))
        lines = int(subprocess.check_output(['tput', 'lines']))
        return columns, lines
    except Exception as e:
        print(f"Error retrieving terminal size: {e}")
        return None, None


def title_to_snake_case(title_str):
    # Replace spaces with underscores
    snake_str = title_str.replace(' ', '_')
    # Convert to lowercase
    snake_str = snake_str.lower()
    return snake_str

def snake_to_title_case(snake_str):
    # Replace underscores with spaces
    title_str = snake_str.replace('_', ' ')
    # Capitalize each word
    title_str = title_str.title()
    return title_str

