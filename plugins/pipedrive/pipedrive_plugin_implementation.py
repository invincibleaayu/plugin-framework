from plugin_implementation_marker.hookimp import hookimpl


class PipedrivePluginImplementation:
    def __init__(self) -> None:
        pass

    @hookimpl
    def sync_contact(self, args):
        print(args, "i am pipedrive")

    @hookimpl
    def sync_call_log(self, args):
        ...

    @hookimpl
    def manage_call(self, args):
        ...
