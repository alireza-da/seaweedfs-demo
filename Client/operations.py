from weed.operation import WeedOperation, WeedMaster # pylint: disable=import-error

class Operations: # pylint: disable=too-few-public-methods
    wo = None

    def __init__(self, master: WeedMaster) -> None:
        self.wo = WeedOperation()
        self.wo.master = master
