from typing import Callable

from Sources.lib.events.event import Event

EVENT_TYPE = [
    "ON_CREATED",
    "ON_DELETED",
    "ON_MODIFIED"
]


class Events_File(Event):
    def __init__(self) -> None:
        super().__init__()
    
    @staticmethod
    def on_created(self, callback: Callable):
        return callback()
    
    @staticmethod 
    def on_modified(self, callback: Callable):
        return callback()

    @staticmethod 
    def on_deleted(self, callback: Callable):
        return callback()