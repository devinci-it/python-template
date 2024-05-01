

from setuptools import setup, find_packages
import glob

def expand_wildcards(data_files):
    expanded_data_files = []
    for dir, files in data_files:
        expanded_files = []
        for file in files:
            if '*' in file:
                expanded_files.extend(glob.glob(file))
            else:
                expanded_files.append(file)
        expanded_data_files.append((dir, expanded_files))
    return expanded_data_files
def readme():
    with open('README.md', 'r', encoding='utf-8') as f:
        return f.read()

setup(
    name='devinci_pykit',
    version='0.1',
    packages=find_packages(['src','lib']),
    package_dir={'': 'src',
                 'lib':'lib'},
    install_requires=['colorama==0.4.6', 'tabulate==0.9.0'],
    entry_points={'console_scripts': ['package_init=bin.helpers.package_init:main', 'helper_setup=scripts.setup_utility:main']},
    author='devinci-it',
    author_email='vince.dev@icloud.com',
    description='This repository is a Python project template designed to accelerate your development process.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/devinci-it/devinci_pykit',
    classifiers=['Programming Language :: Python :: 3'],
    license='MIT',
    data_files=expand_wildcards([('', ['config.ini', 'LICENSE', 'README.md',
                       'requirements.txt']), ('docs', ['docs/*.md'])]),
    scripts=['lib/helpers/package_init.py'],
    py_modules=['tools/setup_tool/package_setup',
                'lib/helpers/package_init']
)
