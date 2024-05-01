"""
Demo script for generating a setup.py file from config.ini using package_setup module.

Note: This script is available for package initialization.

"""

from tools.setup_tool import package_setup


from log.log import Log
if __name__ == "__main__":
    # Initialize package setup
    packager = package_setup.PackageSetup()
    Log=Log('app.log','storage')


    if packager.config_verified():


        print("\nConfig verification passed.")
        print("You are about to install the package with the following setup:")
        # Display package information
        print(f"\nName: {packager.name}")
        print(f"Version: {packager.version}")
        # print(f"Author: {packager.author}")
        # print(f"Author Email: {packager.author_emayil}")
        # print(f"Description: {packager.description}")
        # print(f"URL: {packager.url}")
        # print(f"License: {packager.license}")

        # Prompt user to continue installation
        while True:
            choice = input(
                "\nDo you want to continue with the installation? (yes/no): ").lower()
            if choice in ['yes', 'y']:
                # Generate setup.py if the user chooses to continue
                packager.generate_setup_py('config.ini')
                break
            elif choice in ['no', 'n', 'N', 'NO', 'q', 'Q']:
                print("Installation aborted.")
                break
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
    else:
        print("Config verification failed. Please check your config.ini file.")
