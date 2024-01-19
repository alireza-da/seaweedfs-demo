from weed.master import WeedMaster # pylint: disable=import-error
from config import Config
class Master:
    port = 0
    host = ''
    master = None

    def __init__(self) -> None:
        config = Config().data
        self.port = config['port']
        self.host = config['host']
        url = f'http://{self.host}:{self.port}'
        self.master = WeedMaster(url)
