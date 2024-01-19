from weed.filer import WeedFiler

from config import Config

class Filer:
    wf = None
    port = 0
    host = ''
    path = '/'
    
    def __init__(self) -> None:
        config = Config().data
        self.port = config['filer_port']
        self.host = config['filer_host']
        url = f'http://{self.host}:{self.port}'
        self.wf = WeedFiler(url)
        