class Theme:

    @staticmethod
    def monokai():
        """
        ANSI
        :return:
        """
        colors={
            'reset': "\033[0m",  # Reset

            # Basic text styles
            'dark_purple': "\033[1;96m",  # Cyan bold
            'option': "\033[0;97m",  # White
            'border': "\033[1;36m",  # Cyan bold

            # Dark shades
            'dark_background': "\033[48;2;46;46;46m",  # Dark gray background
            'dark_comments': "\033[38;2;117;113;94m",  # Dark yellowish comments
            'byellow': "\033[38;2;239;192;80m",  # Bright yellow
            'dark_green': "\033[38;2;152;195;121m",  # Light green
            'subheader': "\033[38;2;239;138;98m",  # Bright orange
            'dark_purple': "\033[38;2;198;120;221m",  # Light purple
            'header': "\033[38;2;249;145;159m",  # Light pink
            'dark_blue': "\033[38;2;102;217;239m",  # Light blue

            # Light shades
            'li`qght_background': "\033[48;2;66;66;66m",  # Light gray background
            'ly': "\033[38;2;142;140;120m",  # Light yellowish comments
            'light_yellow': "\033[38;2;255;223;143m",  # Pale yellow
            'light_green': "\033[38;2;194;215;165m",  # Pale green
            'porq': "\033[38;2;255;179;140m",  # Pale orange
            'light_purple': "\033[38;2;209;167;255m",  # Pale purple
            'light_pink': "\033[38;2;255;197;203m",  # Pale pink
            'selected_option': "\033[38;2;135;229;255m",  # Pale blue

            # Accent colors
            'accent1': "\033[38;2;242;109;116m",  # Red
            'accent2': "\033[38;2;153;229;161m",  # Light green
            'accent3': "\033[38;2;246;187;101m",  # Yellow
            'accent4': "\033[38;2;118;183;178m",  # Cyan
            'border': "\033[38;2;196;132;251m"  # Lavender

        }

        return colors
    @staticmethod
    def material_dark():
        """
        Returns ANSI escape sequences for Material Dark color theme.
        """
        colors = {
            'reset': "\033[0m",
            'header': "\033[1;96m",  # Cyan bold
            'subheader': "\033[1;93m",  # Yellow bold
            'option': "\033[0;97m",  # White
            'selected_option': "\033[1;94m",  # Light blue bold
            'border': "\033[1;36m",  # Cyan bold
        }
        return colors

    @staticmethod
    def vampire():
        """
        Returns ANSI escape sequences for Vampire color theme.
        """
        colors = {
            'reset': "\033[0m",
            'header': "\033[1;91m",  # Red bold
            'subheader': "\033[1;93m",  # Yellow bold
            'option': "\033[0;37m",  # Light gray
            'selected_option': "\033[1;35m",  # Purple bold
            'border': "\033[1;31m",  # Red bold
        }
        return colors

    @staticmethod
    def night_owl():
        """
        Returns ANSI escape sequences for Night Owl color theme.
        """
        colors = {
            'reset': "\033[0m",
            'header': "\033[1;97m",  # White bold
            'subheader': "\033[1;95m",  # Cyan bold
            'option': "\033[0;37m",  # Light gray
            'selected_option': "\033[1;94m",  # Light blue bold
            'border': "\033[1;35m",  # Purple bold
        }
        return colors

    @staticmethod
    def ayu_dark():
        """
        Returns ANSI escape sequences for Ayu Dark color theme.
        """
        colors = {
            'reset': "\033[0m",
            'header': "\033[1;94m",  # Light blue bold
            'subheader': "\033[1;93m",  # Yellow bold
            'option': "\033[0;37m",  # Light gray
            'selected_option': "\033[1;92m",  # Green bold
            'border': "\033[1;96m",  # Cyan bold
        }
        return colors

    @staticmethod
    def nord_dark():
        """
        Returns ANSI escape sequences for Nord Dark color theme.
        """
        colors = {
            'reset': "\033[0m",
            'header': "\033[1;96m",  # Cyan bold
            'subheader': "\033[1;94m",  # Light blue bold
            'option': "\033[0;97m",  # White
            'selected_option': "\033[1;93m",  # Yellow bold
            'border': "\033[1;34m",  # Blue bold
        }
        return colors

    @staticmethod
    def nord_light():
        """
        Returns ANSI escape sequences for Nord Light color theme.
        """
        colors = {
            'reset': "\033[0m",
            'header': "\033[1;97m",  # White bold
            'subheader': "\033[1;96m",  # Cyan bold
            'option': "\033[0;37m",  # Light gray
            'selected_option': "\033[1;92m",  # Green bold
            'border': "\033[1;90m",  # Dark gray bold
        }
        return colors

    @staticmethod
    def snow_storm():
        """
        Returns ANSI escape sequences for Snow Storm color theme.
        """
        colors = {
            'reset': "\033[0m",
            'header': "\033[1;97m",  # White bold
            'subheader': "\033[1;96m",  # Cyan bold
            'option': "\033[0;37m",  # Light gray
            'selected_option': "\033[1;34m",  # Blue bold
            'border': "\033[1;90m",  # Dark gray bold
        }
        return colors

    @staticmethod
    def aurora():
        """
        Returns ANSI escape sequences for Aurora color theme.
        """
        colors = {
            'reset': "\033[0m",
            'header': "\033[1;91m",  # Red bold
            'subheader': "\033[1;93m",  # Yellow bold
            'option': "\033[0;37m",  # Light gray
            'selected_option': "\033[1;92m",  # Green bold
            'border': "\033[1;94m",  # Light blue bold
        }
        return colors

    @staticmethod
    def get_theme(name):
        """
        Returns the ANSI escape sequences for the specified theme.

        Args:
        - name (str): Name of the theme ('material_dark', 'vampire', 'night_owl', 'ayu_dark',
                      'nord_dark', 'nord_light', 'snow_storm', 'aurora').

        Returns:
        - dict: Dictionary of ANSI escape sequences for the theme.
        """
        if name == 'material_dark':
            return Theme.material_dark()
        elif name == 'vampire':
            return Theme.vampire()
        elif name == 'night_owl':
            return Theme.night_owl()
        elif name == 'ayu_dark':
            return Theme.ayu_dark()
        elif name == 'nord_dark':
            return Theme.nord_dark()
        elif name == 'nord_light':
            return Theme.nord_light()
        elif name == 'snow_storm':
            return Theme.snow_storm()
        elif name == 'aurora':
            return Theme.aurora()
        elif name == 'monokai':
            return Theme.monokai()
        else:
            raise ValueError(f"Unknown theme '{name}'")
