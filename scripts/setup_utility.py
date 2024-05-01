import argparse
from log.log import Log as DevinciLog
from tools.setup_tool.package_setup import PackageSetup


def main():
    """
    Main function for the package setup script.
    This script allows various operations related to package setup, such as verification of configuration,
    generation of setup.py file, and running the setup process.

    Command-line arguments:
    - -f, --force: Force setup even if setup.py file exists
    - -v, --verify: Verify config
    - -g, --generate: Generate setup.py
    - -r, --run: Run setup
    """
    # Create argument parser
    parser = argparse.ArgumentParser(description='Package Setup Script')

    # Add arguments
    parser.add_argument('-f', '--force', action='store_true', help='Force setup even if setup.py file exists')
    parser.add_argument('-v', '--verify', action='store_true', help='Verify config')
    parser.add_argument('-g', '--generate', action='store_true', help='Generate setup.py')
    parser.add_argument('-r', '--run', action='store_true', help='Run setup')

    # Parse arguments
    args = parser.parse_args()

    # Handle arguments
    if args.verify:
        packager = PackageSetup()
        if packager.config_verified():
            print("\nConfig verification passed.")
        else:
            print("Config verification failed. Please check your config.ini file.")

    if args.generate:
        PackageSetup.generate_setup_py(args.force)

    if args.run:
        if args.force:
            PackageSetup.generate_setup_py(force=True)
        packager = PackageSetup()
        if packager.config_verified():
            print("\nConfig verification passed.")
            print("You are about to install the package with the following setup:")

            # Display package information
            pkg_setup = PackageSetup()
            print(f"\nName: {pkg_setup.name}")
            print(f"Version: {pkg_setup.version}")
            print(f"Author: {pkg_setup.author}")
            print(f"Author Email: {pkg_setup.author_email}")
            print(f"Description: {pkg_setup.description}")
            print(f"URL: {pkg_setup.url}")
            print(f"License: {pkg_setup.license}")

            # Prompt user to continue installation
            while True:
                choice = input("\nDo you want to continue with the installation? (yes/no): ").lower()
                if choice in ['yes', 'y']:
                    # Run setup.py if the user chooses to continue
                    PackageSetup.run_setup()
                    break
                elif choice in ['no', 'n', 'q']:
                    print("Installation aborted.")
                    break
                else:
                    print("Invalid choice. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
