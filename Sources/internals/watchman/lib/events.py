EVENT_TYPE = [
    "ON_CREATED",
    "ON_DELETED",
    "ON_MODIFIED"
]

class Detector:
    def __init__(self, before_list, after_list) -> None:
        self.before_list = before_list
        self.after_list = after_list

    def is_created(self) -> bool:
        if len(self.before_list) < len(self.after_list):
            return True
        else:
            return False
    
    def is_deleted(self) -> bool:
        if len(self.before_list) > len(self.after_list):
            return True
        else:
            return False
    
    def is_modified(self) -> list:
        pass

print(Detector(["aaa", 12, 13], ["aaa", 12, 14]).is_modified())