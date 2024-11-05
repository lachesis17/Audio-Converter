import os
from configparser import ConfigParser

CONFIG_FILE = 'settings.ini'
CONFIG_DIR = 'assets/settings'
CONFIG_FILE_FULL = os.path.join(CONFIG_DIR, CONFIG_FILE)

config = ConfigParser()

def get_config() -> ConfigParser:
    def set_default_config() -> None:
        config['last_accessed_folder'] = {
            'folder': ''
        }

    def write_file() -> None:
        if not os.path.exists(CONFIG_DIR):
            os.makedirs(CONFIG_DIR)
            
        with open(CONFIG_FILE_FULL, 'w') as file_handle:
            config.write(file_handle)
    
    if not os.path.exists(CONFIG_FILE_FULL):
        set_default_config()
        write_file()
    else:
        config.read(CONFIG_FILE_FULL)
         
    return config

def get_last_directory(config: ConfigParser) -> str:
    if 'folder' in config['last_accessed_folder']:
        folder_path = os.path.abspath(config['last_accessed_folder']['folder'])
    else:
        folder_path = os.getcwd()
    return folder_path

def update_last_directory(config: ConfigParser, fname: str) -> None:
    folder_path = os.path.dirname(os.path.abspath(fname))
    config['last_accessed_folder']['folder'] = folder_path
    with open('assets/settings/settings.ini', 'w') as configfile:
        config.write(configfile)