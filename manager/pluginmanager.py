import pluggy
from constants import PACKAGE_NAME
from plugins.hubspot.hubspot_plugin_implementation import HubspotPluginImplementation
from plugins.pipedrive.pipedrive_plugin_implementation import (
    PipedrivePluginImplementation,
)
from plugin_specification_marker.hookspec import BaseHookSpecifications
from uuid import UUID
from domain.enums import CRMName
import copy


class PluginManager:
    def __init__(self, user_id: UUID):
        self.user_id = user_id
        self.connected_crm = [CRMName.HUBSPOT, CRMName.PIPEDRIVE]
        self.plugin_implementations = {
            CRMName.HUBSPOT: HubspotPluginImplementation(),
            CRMName.PIPEDRIVE: PipedrivePluginImplementation(),
        }
        self.pm = pluggy.PluginManager(PACKAGE_NAME)
        self.pm.add_hookspecs(BaseHookSpecifications)
        self.register_plugins()

    def register_plugins(self):
        for crm in self.connected_crm:
            self.pm.register(self.plugin_implementations[crm])

    def run_hooks(self, selected_plugins: list):
        pm_instance = copy.deepcopy(self.pm)
        for plugin in pm_instance.get_plugins():
            print(f"Plugin name{plugin.__class__}")
            if plugin.__class__ in selected_plugins:
                pm_instance.unregister(plugin)
        pm_instance.hook.sync_contact(args="contact")
        print("running all ")
        self.pm.hook.sync_contact(args="contact")
