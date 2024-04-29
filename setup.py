"""
Setup script for your_package_name.

This script configures the setup parameters for your_package_name and prepares it for distribution.

Usage:
    - Replace placeholders with your actual package information.
    - Run 'python env_setup.py sdist bdist_wheel' to build the distribution package.
    - Upload the generated package to PyPI or another package repository.

Configuration Overview:
    - name: Name of the package.
    - version: Version number of the package.
    - packages: List of packages to include in the distribution.
    - package_dir: Mapping of package names to directories.
    - install_requires: List of dependencies required by the package.
    - entry_points: Configuration for console scripts and other entry points.
    - author: Author name of the package.
    - author_email: Email address of the author.
    - description: Short description of the package.
    - long_description: Long description of the package.
    - long_description_content_type: Content type of the long description.
    - url: URL of the package repository.
    - classifiers: List of classifiers for the package.
    - license: License information for the package.
    - package_data: Additional data files to include in the distribution.

"""

from setuptools import setup, find_packages

setup(
    name='your_package_name',
    version='0.1',
    packages=find_packages(where='src') + ['app'],
    package_dir={'': 'src'},
    install_requires=[],
    entry_points={
        'console_scripts': [
            'your_app_name = app.app:main',
            'your_cli_command = app.cli:main',
        ],
    },
    author='Your Name',
    author_email='your@email.com',
    description='Description of your package',
    long_description='Long description of your package',
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/your_package_name',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    license='MIT',
    package_data={
        '': ['docs/*.md', 'config.ini'],
    },
)
