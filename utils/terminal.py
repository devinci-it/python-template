import subprocess

def get_terminal_size():
    try:
        columns = int(subprocess.check_output(['tput', 'cols']))
        lines = int(subprocess.check_output(['tput', 'lines']))
        return columns, lines
    except Exception as e:
        print(f"Error retrieving terminal size: {e}")
        return None, None