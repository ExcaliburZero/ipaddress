# ipaddress
This is a simple Python script used to get the ip address of a computer. It works using `/sbin/ifconfig`, and thus it is required in order for the script to work.

This script ignores local ip addresses such as `127.0.0.1`.

## Downloading
To download and use this script, download the source code for the project, and then you can run the `ipaddress.py` file using python.

```
wget https://github.com/ExcaliburZero/ipaddress/archive/master.tar.gz
```

## Running
This program can be run by downloading the `ipaddress.py` file and running it via the terminal, using the following command:
```
python ipaddress.py
```

### Example
```
python ipaddress.py
120.4.163.100
```

## Licensing
- [MIT License](https://opensource.org/licenses/MIT)
