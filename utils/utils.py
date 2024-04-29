import os

def get_root_dir():
    """Returns the root directory of the project."""
    return os.path.dirname(os.path.abspath(__file__))

def get_docs_dir():
    """Returns the directory path for documentation files."""
    return os.path.join(get_root_dir(), "../docs")

def get_stubs_dir():
    """Returns the directory path for stub files."""
    return os.path.join(get_root_dir(), "../stubs")
