"""
Pacakge Directory Initializer

This script creates a directory structure for a Python project based on predefined templates.

The directory structure includes directories for documentation, development scripts, package files,
storage, tests, and virtual environment, along with corresponding configuration files and scripts.

Usage:
    python package_init.py [--root-dir ROOT_DIR] [--empty] [--package-name
    PACKAGE_NAME]

Options:
    --root-dir ROOT_DIR     Root directory for the project structure. Defaults to the current working directory.
    --empty                  Create the directory structure only if the root directory is empty.
    --package-name PACKAGE_NAME  Name of the package directory. Defaults to 'package'.
"""

import os
import argparse

def create_directory_structure(root_dir, package_name):
    """
    Creates the directory structure for the project.

    Parameters:
    root_dir (str): The root directory where the project structure will be created.
    package_name (str): The name of the package directory.
    """
    dirs = [
        'docs',
        'dev_scripts',
        package_name,
        f'{package_name}/utils',
        f'{package_name}/bin',
        f'{package_name}/config',
        f'{package_name}/env',
        'storage',
        'storage/logs',
        'storage/files',
        'stubs',
        'tests',
        'tests/unit_tests',
        'tests/integration_tests',
        'tests/bin',
        'venv/bin',
        'venv/lib'
    ]

    files = [
        'LICENSE',
        'README.md',
        'config.ini',
        'config.py',
        'dev_scripts/setup_database.py',
        'dev_scripts/run_tests.py',
        'dev_scripts/other_dev_script.py',
        'docs/index.md',
        'requirements.txt',
        'setup.py',
        f'{package_name}/__init__.py',
        f'{package_name}/main_module.py',
        f'{package_name}/utils/__init__.py',
        f'{package_name}/utils/helper_functions.py',
        f'{package_name}/bin/demo_script.py',
        f'{package_name}/config/config.ini',
        f'{package_name}/env/.env',
        f'{package_name}/config.py',
        'storage/logs/debug.log',
        'storage/logs/error.log',
        f'{package_name}/storage/files'
    ]

    for directory in dirs:
        try:
            os.makedirs(os.path.join(root_dir, directory))
            about_file_path = os.path.join(root_dir, directory, ".about")
            with open(about_file_path, 'w') as about_file:
                about_file.write(f"This directory is used for {directory}.")
        except FileExistsError:
            print(f"Directory '{directory}' already exists. Skipping creation.")

    for file in files:
        try:
            os.makedirs(os.path.join(root_dir, os.path.dirname(file)))
            open(os.path.join(root_dir, file), 'w').close()
            about_file_path = os.path.join(root_dir, file[:-3], ".about")
            with open(about_file_path, 'w') as about_file:
                about_file.write(f"This file is used for {file}.")
        except FileExistsError:
            print(f"File '{file}' already exists. Skipping creation.")

def main():
    """
    Main function to create a directory structure for a Python project.
    """
    parser = argparse.ArgumentParser(description='Create a directory structure for a project.')
    parser.add_argument('--root-dir', default=os.getcwd(), help='Root directory for the project structure.')
    parser.add_argument('--empty', action='store_true', help='Create the directory structure only if the root directory is empty.')
    parser.add_argument('--package-name', default='package', help='Name of the package directory.')
    args = parser.parse_args()

    if args.empty and os.listdir(args.root_dir):
        print("Root directory is not empty. Use --empty option to create the structure only if the directory is empty.")
        return

    create_directory_structure(args.root_dir, args.package_name)

if __name__ == "__main__":
    main()
