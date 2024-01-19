# seaweedfs-demo
- Implementing SeaweedFS on Ubuntu machines: Master and Volume setup. 
- Developing a Python based client application for SeaweedFS
### Project Hierarchy
- **Master**
    - master.sh: Shell script to run master server. find and replace your server id with **-ip=<your_ip_address>** 
        ```console
        foo@bar:~$ chmod -x master.sh
        foo@bar:~$ bash master.sh
        ```
    - filer.sh: Shell script to launch filer server on master server. Configure it based on your desires. Replace your master ip address with **-master=<your_ip_address>**, accordingly for your filer server address replace **-ip=<your_ip_address>**
        ```console
        foo@bar:~$ chmod -x filer.sh
        foo@bar:~$ bash filer.sh
        ```
    - filer.toml: Filer server configuration file. If you wish to modify files' metadata data store platform set ``enabled=false`` to ``true``.
    - s3config.json: JSON file containing S3 server configuration including server identities, permissions, and credentials.
- **Volume**
  - init.sh: Shell script to launch a volume server that connects to the master server. Modify ``-mserver="192.168.1.109:9333"`` and ``-ip="192.168.1.110"`` based on your master and volume server ip addresses. You may also want to change ``-dataCenter`` and ``-rack`` as well for each volume you set up.
- **SeaweedFS Client**
    Developing py-weed library and executing some tests on it
  - config.yaml: Modify variables based on your master's address and master's port. For filer server you may also need to modify current configuration
  - config.py: You don't have to make any modification on this file. It just reads/writes on ``config.yaml``
  - filer.py: Contains Filer model `WeedFiler` that handles filer instantiation and connection.
  - master.py: Same as `filer.py` it also has `WeedMaster` instantiation and setting up a connection to master server
  - operations.py: Contains `WeedOperation` instance.
  - test.py: All unit testing and integration testing are done within this file. If you will to do some test operations just run
    ```console
    (venv) foo@terminal:$ python  test.py
    ``` 
    You must have virtual environment set up before executing any python script. All libraries inside `requirements.txt` must have been installed on the mentioned environment.
