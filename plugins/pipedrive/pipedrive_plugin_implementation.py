from plugin_implementation_marker.hookimp import hookimpl


class PipedrivePluginImplementation:
    def __init__(self) -> None:
        pass

    @hookimpl
    async def sync_contact(args):
        ...

    @hookimpl
    async def sync_call_log(args):
        ...

    @hookimpl
    async def manage_call(args):
        ...
