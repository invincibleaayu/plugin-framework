import pluggy

from constants import PACKAGE_NAME

hookspec = pluggy.HookspecMarker(PACKAGE_NAME)


class BaseHookSpecifications:
    def __init__(self) -> None:
        pass

    @hookspec
    async def sync_contact(args):
        ...

    @hookspec
    async def sync_call_log(args):
        ...

    @hookspec
    async def manage_call(args):
        ...
