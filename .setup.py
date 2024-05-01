

from setuptools import setup, find_packages
from configure import read_config_file
import configparser
from os import path as Path

def parse_scripts(filename='config.ini'):
    """
    Parse the config.ini file and return the scripts array.
    """
    scripts = []

    config = configparser.ConfigParser()
    config.read(filename)

    if 'Setup' in config:
        setup_config = config['Setup']
        scripts = setup_config.get('scripts', '').split(',')

    return scripts

def parse_modules(filename='config.ini'):
    """
    Parse the config.ini file and return the modules array.
    """
    modules = []

    config = configparser.ConfigParser()
    config.read(filename)

    if 'Setup' in config:
        setup_config = config['Setup']
        modules = setup_config.get('py_modules', '').split(',')

    return modules

def short_description():

    return """
            This repository is a Python project template designed to accelerate your development process. It offers a structured layout, necessary files, and standard configurations to jumpstart your project. Features include automated documentation generation, pre-configured directory structure, and utility modules for enhanced workflow efficiency.
            """
def readme_content():
    readme_path = f'{Path.dirname(__file__)}/README.md'
    if readme_path:
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        return "README.md not found."


def dependencies(filename='requirements.txt'):
    """
    Parse the requirements.txt file and return a list of dependencies.
    """
    with open(filename, 'r') as f:
        lines = f.read().splitlines()

    # Filter out empty lines and comments
    requirements = [line.strip() for line in lines if
                    line.strip() and not line.strip().startswith('#')]

    return requirements



def app_name():
    config = read_config_file('config.ini')
    return config['General']['appname']



setup(
    name='devinci_pykit',
    version='0.1',
    packages=find_packages(['src','bin','config','utils','tests']),
    package_dir={'': 'src'},
    install_requires=dependencies(),
    entry_points={
        'console_scripts': [
            'package:init = bin.helpers.package_init:main'
        ],
    },
    author='devinci-it',
    author_email='vince.dev@icloud.com',
    description=f'{short_description()}',
    long_description=readme_content(),
    long_description_content_type='text/markdown',
    url=f'https://github.com/devinci-it/{app_name()}',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    license='MIT',
    data_files=[
        ('', ['config.ini', 'LICENSE', 'README.md', 'requirements.txt']),
        ('docs', ['docs/*.md'])
    ],
)
