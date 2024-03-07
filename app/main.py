from manager.pluginmanager import PluginManager
from uuid import UUID
from plugins.hubspot.hubspot_plugin_implementation import HubspotPluginImplementation

PluginManager(user_id=UUID("9e9a1a9f-965e-4103-981f-6a5ef5d26075")).run_hooks(
    selected_plugins=[HubspotPluginImplementation]
)
