import pluggy

from constants import PACKAGE_NAME

hookspec = pluggy.HookspecMarker(PACKAGE_NAME)


class BaseHookSpecifications:
    def __init__(self) -> None:
        pass

    @hookspec
    def sync_contact(self, args):
        ...

    @hookspec
    def sync_call_log(self, args):
        ...

    @hookspec
    def manage_call(self, args):
        ...
