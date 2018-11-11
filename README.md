# HTTPS-Serial-Gateway
Access your Arduino serial console over your local network!

## Installing the server
This server is designed to run on Unix-Like operating system.
The server is built on python3 so it is required to run.
You must install flask from PyPi for the server to run.
```
pip3 install flask
```
## Finding your serial port
Using a terminal run:
```
ls /dev/tty.*
```
select the correct serial port
It should look like `/dev/tty.usbserial-XXXXXXX`.

## Running the server
In the root directory run
```
python3 HTTPSerialShell.py <serial port>
```

## Viewing the server
In a browser, open localhost:5000.
Type in your data to the textbox and press send to transmit to your serial device.
