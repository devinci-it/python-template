from setuptools import setup, find_packages
import configparser
from os import path as Path
import json

class PackageSetup:

    def __init__(self, config_filename='config.ini'):
        self.config = configparser.ConfigParser()

        self.defaults = {
            'name': 'devinci_pykit',
            'version': '0.1',
            'package_dir': {'': 'src'},
            'classifiers': ['Programming Language :: Python :: 3'],
            'license': 'MIT',
            'long_description_content_type': 'text/markdown'
        }

        # Get values from config or use defaults
        self.name = self.get_config_value('General', 'name',
                                          default=self.defaults['name'])
        self.version = self.get_config_value('General', 'version',
                                             default=self.defaults['version'])
        self.required = {
            'General': ['name', 'version', 'package_dir', 'requirements_file',
                        'author', 'author_email', 'description', 'readme_file',
                        'url', 'classifiers', 'license'],
            'Setup': [],
            'DataFiles': ['_', 'docs'],
            'EntryPoints': [],
            'PyModules': ['utilities'],
            'Scripts': ['package_init']
        }

        self.config.read(config_filename)

    def get_config_value(self, section, key=None, default=None):
        if section in self.config:
            if key is not None and key in self.config[section]:
                return self.config[section][key]
            else:
                return self.config[section]
        return default

    def parse_data_files(self, data_files_sec):

        if isinstance(data_files_sec, configparser.SectionProxy):
            try:
                parsed_data_files = self._format_section_as_list_of_tuples(
                    data_files_sec)
                print(parsed_data_files)
            except json.JSONDecodeError:

                print("Error: Failed to parse data_files configuration as JSON.")

            return parsed_data_files
    def generate_setup_py(config_filename='config.ini',
                          setup_stub_filename='stubs/setup_stub.py',
                          output_filename='setup.py'):
        with open(setup_stub_filename, 'r') as stub_file:
            setup_stub_content = stub_file.read()

        package_setup = PackageSetup(config_filename)

        setup_content = setup_stub_content.format(
            name=package_setup.get_config_value('General', 'name'),
            version=package_setup.get_config_value('General', 'version'),
            packages=find_packages(
                package_setup.get_config_value('General', 'package_dir')),
            package_dir={'': package_setup.get_config_value('General', 'package_dir')},
            install_requires=package_setup.dependencies(
                package_setup.get_config_value('General', 'requirements_file')),
            entry_points=package_setup.parse_entry_points(
                package_setup.get_config_value('EntryPoints')),
            author=package_setup.get_config_value('General', 'author'),
            author_email=package_setup.get_config_value(
                'General', 'author_email'),
            description=package_setup.get_config_value('General', 'description'),
            long_description=package_setup.readme_content(
                package_setup.get_config_value('General', 'readme_file')),
            long_description_content_type='text/markdown',
            url=package_setup.get_config_value('General', 'url'),
            classifiers=package_setup.get_config_list(
                'General', 'classifiers'),
            license=package_setup.get_config_value('General', 'license'),
            data_files=package_setup.parse_data_files(
                package_setup.get_config_value('DataFiles')),
            scripts=package_setup.parse_scripts(
                package_setup.get_config_value('Scripts')),
            py_modules=package_setup.parse_modules(
                package_setup.get_config_value('PyModules'))
        )

        with open(output_filename, 'w') as setup_file:
            setup_file.write(setup_content)

        print(f"{output_filename} generated successfully.")

    def setup_package(self):
        setup(
            name=self.get_config_value('General', 'name'),
            version=self.get_config_value('General', 'version'),
            packages=find_packages(self.get_config_value('General', 'package_dir')),
            package_dir={'': self.get_config_value('General', 'package_dir')},
            install_requires=self.dependencies(self.get_config_value('General', 'requirements_file')),
            entry_points=self.parse_entry_points(self.get_config_value('EntryPoints')),
            author=self.get_config_value('General', 'author'),
            author_email=self.get_config_value('General', 'author_email'),
            description=self.get_config_value('General', 'description'),
            long_description=self.readme_content(self.get_config_value('General', 'readme_file')),
            long_description_content_type='text/markdown',
            url=self.get_config_value('General', 'url'),
            classifiers=self.get_config_list('General', 'classifiers'),
            license=self.get_config_value('General', 'license'),
            data_files=self.parse_data_files(self.get_config_value('DataFiles')),
            scripts=self.parse_scripts(self.get_config_value('Scripts')),
            py_modules=self.parse_modules(self.get_config_value('PyModules'))
        )

    def dependencies(self, filename='requirements.txt'):
        with open(filename, 'r') as f:
            lines = f.read().splitlines()
        requirements = [line.strip() for line in lines if
                        line.strip() and not line.strip().startswith('#')]
        return requirements

    def parse_entry_points(self, entry_points):

        if isinstance(entry_points, configparser.SectionProxy):
            entry_points_str = self._format_section_as_list_string(entry_points)

            entry_points_list = eval(entry_points_str)

            formatted_entry_points = []
            for key, values in entry_points_list:
                for value in values:
                    formatted_entry_points.append(f"{key}={value}")

            print(formatted_entry_points,type(formatted_entry_points))
            formatted_entry_points = []
            for key, values in entry_points_list:
                append_me =  f"{key}={values[0]}"
                formatted_entry_points.append(append_me)

            # Convert the formatted entry points dictionary to a JSON string
            print({'console_scripts': formatted_entry_points})
            return ({'console_scripts': formatted_entry_points})

            # for each in entry_points:
            #     entry_points.append(each)

            # string_value = json.dumps( {"console_scripts":entry_point_val},
                                      # indent=2)


        elif isinstance(entry_points, str):
            try:
                entry_points_dict = json.loads(entry_points)
            except json.JSONDecodeError:
                print("Error: Failed to parse entry_points as JSON.")
        else:
            print(f"Error: Invalid entry_points format.\n{entry_points}")

    def parse_scripts(self, scripts_sec):
        if isinstance(scripts_sec, configparser.SectionProxy):
            return self._format_section_as_list_val(scripts_sec)
        else:
            print("Error: Invalid scripts format.")
            return "[]"

    def parse_modules(self, modules_sec):
        if isinstance(modules_sec, configparser.SectionProxy):
            return self._format_section_as_list_val(modules_sec)
        else:
            print("Error: Invalid modules format.")
            return "[]"

    def get_config_list(self, section, key):
        if section in self.config and key in self.config[section]:
            value = self.config[section][key]
            return [item.strip() for item in value.split(',')]
        else:
            return []


    def readme_content(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return "README file not found."

    def config_verified(self):
        config_errors = []

        # Check if config sections exist and keys are present
        for section, keys in self.required.items():
            if section not in self.config:
                config_errors.append(
                    f"Section '{section}' missing in config.ini")
            else:
                # Check if required keys exist
                for key in keys:
                    if key not in self.config[section]:
                        config_errors.append(
                            f"Key '{key}' missing in section '{section}' of config.ini")

        # Check if files specified in config are present and readable
        files_to_check = [self.get_config_value('General', 'requirements_file'),
                          self.get_config_value('General', 'readme_file')]
        for file_path in files_to_check:
            if not Path.exists(file_path):
                config_errors.append(
                    f"File '{file_path}' specified in config.ini does not exist")
            if not Path.isfile(file_path):
                config_errors.append(
                    f"'{file_path}' specified in config.ini is not a file")
            if not Path.isfile(file_path):
                config_errors.append(
                    f"'{file_path}' specified in config.ini is not readable")

        # Check if entry points are specified
        if 'EntryPoints' in self.config:
            entry_points = self.config['EntryPoints']
            if not entry_points:
                config_errors.append(
                    f"No entry points specified in section 'EntryPoints' of config.ini")

        if config_errors:
            for error in config_errors:
                print(f"Config verification error: {error}")
            return False
        else:
            print("Config verification passed.")
            return True

    def _format_section_as_list_string(self, section):
        """
        Formats the keys and values of a configparser section as a string representing a list.
        """
        if isinstance(section, configparser.SectionProxy):
            formatted_pairs = []
            for key, value in section.items():
                values_list = [val.strip() for val in value.split(',')]
                formatted_pairs.append((key, values_list))

            # Convert each pair to string format
            formatted_string = '[' + ', '.join(
                [f"('{key}', {value})" for key, value in formatted_pairs]) + ']'

            return formatted_string
        else:
            print("Error: Invalid section format.")
            return "[]"

    def _format_section_as_list_val(self, section):
        """
        Formats the values of a configparser section as a list string.
        """
        if isinstance(section, configparser.SectionProxy):
            formatted_values = []
            for value in section.values():
                formatted_values.extend(
                    [val.strip() for val in value.split(',')])
            formatted_string = '[' + ', '.join(
                [f"'{value}'" for value in formatted_values]) + ']'
            return formatted_string
        else:
            print("Error: Invalid section format.")
            return "[]"

    def _format_section_as_list_of_tuples(self, section):
        """
        Formats the values of a configparser section as a list of tuples.
        Each tuple contains a key-value pair from the section.
        """
        if isinstance(section, configparser.SectionProxy):
            formatted_values = []
            for key, value in section.items():
                if key == '_':
                    key = ''
                values_list = [val.strip() for val in value.split(',')]
                formatted_values.append((key, values_list))
                print(formatted_values)
            return formatted_values
        else:
            print("Error: Invalid section format.")
            return []