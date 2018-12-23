# Quick Serial Talk
These scripts are made to ease the development of transmission protocols over a serial communication.
Instead of sending/displaying ASCII characters like any other terminal application, they use *byte* (0-255) values directly.

## Usage

### Send

#### Syntax
```bash
python send.py PORT[:BAUDRATE] byte1 byte2 ... byteN
```

#### Example
```bash
$ python send.py COM16:9600 65 98 99
> Sending characters to port COM16 at speed 9600 bauds.
```


### Receive

#### Syntax
```bash
python receive.py PORT[:BAUDRATE]
```

#### Example
```bash
$ python receive.py COM15:9600
> Waiting for incoming characters on port COM15 at speed 9600 bauds.
> 65
> 98
> 99
```
