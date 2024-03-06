import importlib
import os
import plugins
from constants import BASE

plugin_implementations: dict = {}


def load_plugin_implementation():
    path = plugins.__path__[0]
    for folder in os.listdir(path=path):
        print("Folder", folder)
        folder_path = f"{path}/{folder}"
        print("Folder path", folder_path)
        if not folder.startswith("_") and os.path.isdir(folder_path):
            if not folder == BASE:
                module_path = f"plugins.{folder}"
                print("Module path", module_path)
                module = importlib.import_module(module_path)
                plugin_implementations[folder] = getattr(
                    module, f"{folder.title()}PluginImplementation"
                )


load_plugin_implementation()
