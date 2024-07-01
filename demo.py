from cli.select import CLISelectPrompt

if __name__ == "__main__":
    prompt_header = "Select an option:"
    prompt_sub = "Use arrow keys (↑/↓) to navigate, Enter to select, Ctrl+C to cancel."
    options = ["Option 1 ", " Option 2 ", " Option 3 "]
    default_index = 1

    # Example usage with different themes
    themes = ['material_dark', 'vampire', 'night_owl', 'ayu_dark', 'nord_light', 'snow_storm', 'aurora']

    for theme_name in themes:
        result = CLISelectPrompt.select(prompt_header, prompt_sub, options, default_index, theme_name)
        print(f'\nYou selected: {result}\n')
