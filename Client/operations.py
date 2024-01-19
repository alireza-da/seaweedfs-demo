from weed.operation import WeedOperation, WeedMaster

class Operations:
    wo = None

    def __init__(self, master: WeedMaster) -> None:
        self.wo = WeedOperation()
        self.wo.master = master