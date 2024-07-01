from src.cli.select import CLISelectPrompt  # Adjust import as per your project structure
import sys
from src.cli.helper import title_to_snake_case, snake_to_title_case
from src.cli.confirm import ConfirmationPrompt

def demo_single_select():
    prompt_header = 'Checkout available themes.'
    prompt_sub = "Use arrow keys (↑/↓) to navigate, Enter to select, q to quit."
    theme_options = ["Material Dark", "Vampire", "Night Owl", "Ayu Dark", "Nord Light", "Snow Storm", "Aurora","Monokai"]
    default_index = 0
    theme_name = 'vampire'

    while True:
        # Display the initial prompt to select a theme
        theme_name = CLISelectPrompt.select(prompt_header, prompt_sub, theme_options, default_index,title_to_snake_case(theme_name))


        if theme_name.lower() == 'q':
            break  # Exit the loop if user chooses to quit

        # Example usage with the selected theme
        print(f'\nYou selected: {theme_name}\n')

        prompt_header = snake_to_title_case(theme_name)  # Reset prompt_header for the next iteration

def demo_checkbox_select():
    prompt_header = "Select themes to activate:"
    prompt_sub = "Use arrow keys (↑/↓) to navigate, Enter to confirm, q to quit."
    theme_options = ["Material Dark", "Vampire", "Night Owl", "Ayu Dark", "Nord Light", "Snow Storm", "Aurora", "Monokai"]
    default_indices = []
    min_selection = 1  # Minimum selections required
    max_selection = 3  # Maximum selections allowed

    while True:
        selected_themes = CLISelectPrompt.checkbox_select(prompt_header, prompt_sub, theme_options, min_selection, max_selection, default_indices, 'material_dark')

        if selected_themes == 'q':
            break  # Exit the loop if user chooses to quit

        sys.stdout.flush()
        print(f'\nSelected themes: {selected_themes}\n')

        # prompt_header = "Select themes to activate:"  # Reset prompt_header for the next iteration


def demo_confirm_prompt():
    title = "Confirmation Dialog"
    context = "Are you sure you want to proceed ? "
    header=''
    okay_text = "Okay"



    stdin=ConfirmationPrompt.display_confirmation(title, header, context,theme_name='vampire')
    print(stdin)

def main():
    # print("Demo for single select:")
    #demo_single_select()
    demo_confirm_prompt()

    monokai_palette = {
        'reset': "\033[0m",  # Reset

        # Basic text styles
        'header': "\033[1;96m",  # Cyan bold
        'option': "\033[0;97m",  # White
        'selected_option': "\033[1;94m",  # Light blue bold
        'border': "\033[1;36m",  # Cyan bold

        # Dark shades
        'dark_background': "\033[48;2;46;46;46m",  # Dark gray background
        'dark_comments': "\033[38;2;117;113;94m",  # Dark yellowish comments
        'dark_yellow': "\033[38;2;239;192;80m",  # Bright yellow
        'dark_green': "\033[38;2;152;195;121m",  # Light green
        'dark_orange': "\033[38;2;239;138;98m",  # Bright orange
        'dark_purple': "\033[38;2;198;120;221m",  # Light purple
        'dark_pink': "\033[38;2;249;145;159m",  # Light pink
        'dark_blue': "\033[38;2;102;217;239m",  # Light blue

        # Light shades
        'light_background': "\033[48;2;66;66;66m",  # Light gray background
        'light_comments': "\033[38;2;142;140;120m",  # Light yellowish comments
        'light_yellow': "\033[38;2;255;223;143m",  # Pale yellow
        'light_green': "\033[38;2;194;215;165m",  # Pale green
        'light_orange': "\033[38;2;255;179;140m",  # Pale orange
        'light_purple': "\033[38;2;209;167;255m",  # Pale purple
        'light_pink': "\033[38;2;255;197;203m",  # Pale pink
        'light_blue': "\033[38;2;135;229;255m",  # Pale blue

        # Accent colors
        'accent1': "\033[38;2;242;109;116m",  # Red
        'accent2': "\033[38;2;153;229;161m",  # Light green
        'accent3': "\033[38;2;246;187;101m",  # Yellow
        'accent4': "\033[38;2;118;183;178m",  # Cyan
        'accent5': "\033[38;2;196;132;251m"  # Lavender
    }

    # Example usage

    # print("\nDemo for checkbox select:")
    # demo_checkbox_select()
    # demo_checkbox_select()

if __name__ == "__main__":
    main()
