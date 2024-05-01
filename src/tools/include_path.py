import sys
import os

def add_package_to_python_path(package_path):
    """
    Add a specific package directory to the Python path.

    Parameters:
    package_path (str): The path to the package directory.
    """
    # Ensure the package path is absolute
    package_path = os.path.abspath(package_path)

    # Check if the package directory exists
    if not os.path.exists(package_path):
        raise ValueError("Package directory does not exist.")

    # Append the package directory to the Python path if it's not already there
    if package_path not in sys.path:
        sys.path.append(package_path)
        print(f"Added '{package_path}' to Python path.")

# Example usage:
# Add your package directory to the Python path