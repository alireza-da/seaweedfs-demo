import yaml

class Config:
    """
    Configuration write/read using yaml library. Keep this class untouched
    """
    data = None
    def __init__(self) -> None:
        with open('config.yaml', 'r', encoding='UTF-8') as file:
            self.data = yaml.safe_load(file)
