"""Module to manipulate site-packages directory."""

import os
import sys

def add_package_to_pth(package_path):
    """
    Add a package directory to the .pth file in the site-packages directory.

    Parameters:
    package_path (str): The path to the package directory.
    """
    venv_site_packages = get_venv_site_packages()

    # Create or append to the .pth file
    pth_file_path = os.path.join(venv_site_packages, 'custom_packages.pth')
    with open(pth_file_path, 'a') as f:
        f.write(package_path + '\n')

def get_venv_site_packages():
    """
    Get the site-packages directory of the virtual environment.

    Returns:
    str: The path to the site-packages directory.
    """
    venv_bin_dir = os.path.dirname(sys.executable)

    # Construct the path to the site-packages directory
    if 'Scripts' in venv_bin_dir:
        venv_site_packages = os.path.join(os.path.dirname(venv_bin_dir), 'Lib', 'site-packages')
    else:
        venv_site_packages = os.path.join(os.path.dirname(venv_bin_dir), 'lib', 'python' + sys.version[:3], 'site-packages')

    return venv_site_packages
