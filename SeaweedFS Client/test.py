import logging
import pprint

from filer import Filer
from master import Master
from operations import Operations
from weed.util import Status

logging.root.setLevel(logging.NOTSET)
logger = logging.getLogger('TEST') 
exampleFormatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.basicConfig(format='[%(asctime)s][%(levelname)s][%(name)s]: %(message)s')
# File Config TODO: move it to config.yaml
filepath = 'assets/sample.exe'
filename = 'sample.exe'
replacing_path = 'assets/replacing.zip'
replacing_name = 'replacing.zip'

def test_operations(master):
    logger.info('TESTING HTTP OPERATIONS  ⌛')
    wo = Operations(master).wo
    # put
    file = wo.put(filepath)
    logger.info(f'File {filepath} Uploaded {file.status}: {file.url}')
    # get
    ret_file = wo.get(file.fid)
    logger.info(f'File Retrieved {ret_file.status}: {ret_file.content_type}')
    # delete 
    del_file = wo.delete(file.fid)
    logger.info(f'File {file.fid} Deleted {del_file.status}')

def test_crud(master):
    logger.info("TESTING CRUD OPERATIONS ⌛")
    wo = Operations(master).wo
     # create
    file = wo.crud_create(filepath)
    logger.info(f'File Created {file.name} URL: {file.url}')
    
    # read
    rdf = wo.crud_read(file.fid)
    logger.info(f'File Read {file.fid} Type: {rdf.content_type}')
    
    # update
    replaced = wo.crud_update(replacing_path, file.fid)
    logger.info(f'File {file.fid} Replaced with {replaced.name} URL: {replaced.url}')
    r_replaced = wo.crud_read(replaced.fid)
    logger.info(f'Reading Replaced File Back {r_replaced.fid} Type: {r_replaced.content_type}')
    # delete
    deleted = wo.delete(replaced.fid)
    if deleted.status == Status.SUCCESS:
        logger.info(f'Successfully Deleted {replaced.fid}')
    else: 
        logger.error(f'Failed to Delete {replaced.fid}')
    logger.info("Trying to read deleted file back...")
    res = wo.crud_read(replaced.fid)
    if res.storage_size == 0:
        logger.info(f"File {replaced.fid} does not exist anymore")
    
def test_filer():
    logger.info("TESTING FILER OPERATIONS ⌛")
    filer = Filer()
    wf = filer.wf
    
    # put
    f = wf.put(filepath, filer.path)
    rem_path = f'{f}{filename}'

    if f:
        logger.info(f'File Put via Filer. Remote Path: {rem_path}')
    else:
        logger.error(f'Was not able to put file {filepath} via Filer')
    
    # get
    f_get = wf.get(rem_path)
    if f_get:
        
        logger.info(f'File Get via Filer. Content Length: {f_get['content_length']}B Content Type: {f_get['content_type']}')
    
    # delete
    f_delete = wf.delete(rem_path)
    if f_delete:
        logger.info(f'File {rem_path} does not exist on server anymore')
    else:
        logger.error(f'Was not able to delete {rem_path}')

def init():
    logger.info("Client Initiated ⌛")
    master = Master().master
    logger.info(f'Connecting to {master.url_base}')
    logger.info(f'Master version: {master.get_status()['Version']}')
    # getting volumes
    ak = master.acquire_new_assign_key()['fid']
    logger.info(f'Assign Key: {ak}')
    logger.info(f'Looking up assign key <<{ak}>>: {master.lookup(ak)}')
    vol = master.get_volume(ak)
    logger.info(f'Fetched volume data {pprint.pprint(vol.get_status())}')
    # HTTP operations
    test_operations(master)
    # CRUD Operations
    test_crud(master)
    # Filer 
    test_filer()
    logger.info("Finished Client Unit Testing ✅")



if __name__ == "__main__":
    init()