from .display import Display

theme= {
            'reset': "\033[0m",
            'header': "\033[1;97m",  # White bold
            'subheader': "\033[1;96m",  # Cyan bold
            'option': "\033[0;37m",  # Light gray
            'selected_option': "\033[1;34m",  # Blue bold
            'border': "\033[1;90m",  # Dark gray bold
            'body_text': "\033[0;37m",  # Bright white
            'body_highlight': "\033[1;97m",  # Bright white bold
        }
DISPLAY = Display(theme, border_style='thick')

