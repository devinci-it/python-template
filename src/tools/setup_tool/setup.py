

from setuptools import setup, find_packages

def readme():
    with open('README.md', 'r', encoding='utf-8') as f:
        return f.read()

setup(
    name='devinci_pykit',
    version='0.1',
    packages=find_packages([]),
    package_dir={'': 'src'},
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
    data_files=[('', ['config.ini', 'LICENSE', 'README.md', 'requirements.txt']), ('docs', ['docs/*.md'])],
    scripts=['bin/helpers/package_init.py'],
    py_modules=['package_setup', 'site_packages']
)
