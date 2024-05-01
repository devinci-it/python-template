import os

class ModuleAutoloader:
    @staticmethod
    def autoload(root_directory='src'):
        for root, dirs, files in os.walk(root_directory):
            for file in files:
                if file.endswith(".py") and file != "__init__.py":
                    module_path = os.path.relpath(os.path.join(root, file)).replace(os.sep, '.')[:-3]
                    module_name = module_path.split('.')[-1]
                    globals().update({module_name: __import__(module_path)})

# if __name__ == "__main__":
#
#     ModuleAutoloader.autoload()

