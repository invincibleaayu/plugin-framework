from manager.pluginmanager import PluginManager
from uuid import UUID
from plugins.hubspot.hubspot_plugin_implementation import HubspotPluginImplementation

PluginManager(user_id=UUID("9e9a1a9f-965e-4103-981f-6a5ef5d26075")).run_hooks(
    selected_plugins=[HubspotPluginImplementation]
)
# from typing import Iterable
# import pluggy

# # Define a hook specification
# hookspec = pluggy.HookspecMarker("myplugin")

# # Define a hook implementation
# hookimpl = pluggy.HookimplMarker("myplugin")


# class BaseHookSpecifications:
#     # Define a hook
#     @hookspec
#     def sync_contact(args):
#         pass


# # Define a plugin
# class MyPlugin1:
#     @hookimpl
#     def sync_contact(self, args):
#         print("MyPlugin1 sync_contact executed with args:", args)


# class MyPlugin2:
#     @hookimpl
#     def sync_contact(self, args):
#         print("MyPlugin2 sync_contact executed with args:", args)


# # Initialize the plugin manager
# pm = pluggy.PluginManager("myplugin")
# pm.add_hookspecs(BaseHookSpecifications)

# # Register the plugins
# pm.register(MyPlugin1())
# pm.register(MyPlugin2())


# # Define a method to run hooks from selected plugins using subset_hook_caller
# def run_hooks(pm, selected_plugins):
#     caller = pm.subset_hook_caller(
#         name="sync_contact",  # Correctly target the sync_contact hook
#         remove_plugins=[
#             p for p in pm.get_plugins() if p.__class__ not in selected_plugins
#         ],
#     )
#     caller(args="contact")


# # Define the selected plugins
# selected_plugins = [MyPlugin1]

# # Run hooks from selected plugins
# run_hooks(pm=pm, selected_plugins=selected_plugins)
# print("runall")
# pm.hook.sync_contact(args="contact")
