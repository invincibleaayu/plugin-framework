from manager.pluginmanager import PluginManager
from uuid import UUID

PluginManager(user_id=UUID("9e9a1a9f-965e-4103-981f-6a5ef5d26075")).run_hooks()
