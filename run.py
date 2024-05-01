"""Main script for running the application.

This script initializes and runs the application, configuring logging,
loading configuration settings, and handling command-line interface (CLI) utility.

Usage:
    $ python run.py

This script checks for the existence of a configuration file ('config.ini').
If the file doesn't exist, it generates a template for the configuration file.
It also ensures the existence of a directory for log files ('logs').

Attributes:
    log (Log): An instance of the logging utility.
    config (Config): An instance of the configuration handler.
    cli (CLIUtility): An instance of the command-line interface utility.
"""

import os
# from src import App, Log, Config, CLIUtility
from devinci_pykit.app import App
from log import log as Log
from config import config as Config
from cli import cli as CLI

if __name__ == "__main__":
    log = Log.Log()
    config = Config.Config()

    log.configure_logging(10, config.get_logging_format())
    cli = CLI.CLIUtility()

    if not os.path.exists('config.ini'):
        Config.generate_config_template()
        print("Config file 'config.ini' created. Please modify 'config.ini' to your needs and rerun the script.")
        exit()

    # Check and create the logs directory if it doesn't exist
    if not os.path.exists('storage/logs'):
        os.makedirs('logs')
        print("Log directory 'logs' created.")

    # Instantiate the app and run
    app = App(log, config, cli)
    app.run()
