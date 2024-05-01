import os
import sys
import site
import re
def get_venv_site_packages():
    """
    Get the site-packages directory of the virtual environment.

    Returns:
        str: The path to the site-packages directory.
    """
    # Get the path to the virtual environment's bin or Scripts directory
    venv_bin_dir = os.path.dirname(sys.executable)
    venv_dir = os.path.dirname(venv_bin_dir)
    venv_site_packages = os.path.join(os.path.split(venv_bin_dir)[0],
                                      'lib',
                                      'python3.11',
                                      'site-packages')

    # python_version =os.path.dirname(venv_site_packages)
    # print(f'\nVENV_BIN_DIR:{venv_bin_dir}',end='\n')
    # print(f'\nVENV_DIR:{venv_dir}',end='\n')
    # print(f'\nVENV_SITE_PACAKAGES:{venv_site_packages}')

    # if 'Scripts' in venv_bin_dir:
    #     venv_site_packages = os.path.join(os.path.dirname(venv_bin_dir), 'Lib', 'site-packages')
    # else:
    #     venv_site_packages = os.path.join(os.path.dirname(venv_bin_dir),
    #                                       'lib', 'python' + python_version,
    #                                       'site-packages')

    return venv_site_packages
