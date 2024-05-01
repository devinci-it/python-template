import subprocess
import argparse
import os
from colorama import init, Fore
from tabulate import tabulate
import utils

init(autoreset=True)

class SetupTool:
    """
    A tool for setting up virtual environments, managing requirements, and more.

    Attributes:
        python_cmd (str): The command used to execute Python.
        pip_cmd (str): The command used to execute pip.
    """

    def __init__(self):
        """Constructor to set Python and pip commands."""
        self.python_cmd = "python3"
        self.pip_cmd = "pip3"

    @staticmethod
    def clear_screen():
        """Clears the terminal screen."""
        os.system('clear')

    @staticmethod
    def color_print(message, color):
        """Prints a message in the specified color."""
        print(color + message)

    def create_venv(self):
        """Creates a virtual environment."""
        self.clear_screen()
        venv_name = input("Enter the name for the virtual environment: ")
        subprocess.run([self.python_cmd, "-m", "venv", venv_name])
        self.color_print(f"Virtual environment '{venv_name}' created.", Fore.GREEN)

    def activate_venv(self, venv_name=None):
        """Activates a virtual environment."""
        if not venv_name:
            venv_name = input("Enter the name of the virtual environment to activate: ")
        activate_script = os.path.join(venv_name, "bin", "activate")
        if os.path.exists(activate_script):
            subprocess.run(["source", activate_script])
            self.color_print(f"Virtual environment '{venv_name}' activated.", Fore.GREEN)
        else:
            self.color_print(f"Virtual environment '{venv_name}' not found.", Fore.RED)

    def recreate_venv(self, venv_name=None):
        """Recreates a virtual environment."""
        if not venv_name:
            venv_name = input("Enter the name of the virtual environment to recreate: ")
        subprocess.run([self.python_cmd, "-m", "venv", "--clear", venv_name])
        self.color_print(f"Virtual environment '{venv_name}' recreated.", Fore.GREEN)

    def pip_freeze(self):
        """Dumps the pip freeze."""
        self.clear_screen()
        pip_freeze_output = subprocess.check_output([self.pip_cmd, "freeze"]).decode("utf-8")
        pip_freeze_table = tabulate([line.split('==') for line in pip_freeze_output.split('\n')[:-1]],
                                    headers=['Package', 'Version'], tablefmt='fancy_grid')
        print(pip_freeze_table)

    def reinstall_requirements(self):
        """Reinstalls all requirements from requirements.txt."""
        self.clear_screen()
        subprocess.run([self.pip_cmd, "install", "-r", "requirements.txt"])
        self.color_print("All requirements reinstalled.", Fore.GREEN)

    def run_build(self):
        """Runs build commands."""
        self.clear_screen()
        if os.path.exists("setup.py"):
            try:
                subprocess.run([self.python_cmd, "setup.py", "bdist"])
                subprocess.run([self.python_cmd, "setup.py", "sdist"])
                subprocess.run([self.python_cmd, "setup.py", "bdist_wheel"])
                print("Distribution packages built successfully.")
            except subprocess.CalledProcessError as e:
                print(f"Error: {e.stderr}")
                print("Failed to build distribution packages.")
        else:
            print("Error: setup.py not found.")
        self.color_print("Build commands executed.", Fore.GREEN)

    def init_git(self):
        """Initializes a git repository."""
        self.clear_screen()
        subprocess.run(["git", "init"])
        self.color_print("Git initialized.", Fore.GREEN)

    def create_package(self, package_name):
        """Creates a new package within the src directory."""
        package_dir = os.path.join("..", package_name)
        os.makedirs(package_dir)
        self._generate_init_file(package_dir)
        self._generate_package_md(package_name)
        self._touch_python_file(package_dir)

    def to_camel_case(self, string):
        parts = string.replace("-", "_").split("_")
        camel_case = ''.join([part.capitalize() for part in parts])
        return camel_case

    def _write_to_file(self, file_path, content):
        """Writes content to a file."""
        with open(file_path, "a") as file:
            file.write(content)

    def _generate_init_file(self, package_dir):
        """Generates the __init__.py file for the package."""
        init_file_path = os.path.join(package_dir, "__init__.py")
        self._write_to_file(init_file_path,
                            f"from .{package_dir.split('/')[-1]} import {self.to_camel_case(package_dir.split('/')[-1])}\n")

    def _touch_python_file(self, package_dir):
        """Touches a Python file based on the split package directory."""
        python_file_path = os.path.join(package_dir,
                                        f"{package_dir.split('/')[-1]}.py")
        stub_file_path = os.path.join(utils.get_stubs_dir(), "class_stub.py")

        with open(stub_file_path, "r") as stub_file:
            class_template = stub_file.read()

        formatted_class = class_template.format(
            class_name=self.to_camel_case(package_dir.split('/')[-1])
        )

        self._write_to_file(python_file_path, formatted_class)

    def _generate_package_md(self, package_name):
        """Generates the markdown documentation file for the package."""
        doc_dir = "../../docs"
        package_md = os.path.join(doc_dir, f"{package_name}.md")
        with open(package_md, "w") as f:
            f.write(f"# {package_name}\n\n")
            f.write("Description of the package goes here.")



def main():
    """
    Main function to parse arguments and execute commands.
    """
    parser = argparse.ArgumentParser(description="Setup tools")
    parser.add_argument("--interactive", "-i", action="store_true", help="Enter interactive mode")
    args = parser.parse_args()

    setup_tool = SetupTool()

    choices = {
        '1': setup_tool.create_venv,
        '2': setup_tool.activate_venv,
        '3': setup_tool.recreate_venv,
        '4': setup_tool.pip_freeze,
        '5': setup_tool.reinstall_requirements,
        '6': setup_tool.run_build,
        '7': setup_tool.init_git,
        '8': lambda: setup_tool.create_package(input('PACKAGE NAME:')),
        'Q': lambda: None
    }

    if args.interactive:
        while True:
            print("\nOptions:")
            print("1. Create a virtual environment")
            print("2. Activate a virtual environment")
            print("3. Recreate a virtual environment")
            print("4. Dump pip freeze")
            print("5. Reinstall all requirements from requirements.txt")
            print("6. Run build")
            print("7. Initialize git repository")
            print("8. Create a new package")
            print("Q. Quit")

            choice = input("Enter your choice: ").upper()

            action = choices.get(choice)
            if action:
                action()
            elif choice == 'Q':
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()




