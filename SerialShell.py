import serial
import sys
import os

connection = serial.Serial(sys.argv[1])  # open serial port

def runCommand(command):
    command += "\n"
    connection.write(command.encode())

def getOutput():
    output = ""
    while True:
        output += connection.read().decode("utf-8")
        if output[-1] == '>':
            break

    with open(os.getcwd() + '/session.txt', 'a') as myFile:
        myFile.write(str(output.replace('\n', '<br>')))

    with open(os.getcwd() + '/session.txt', 'r') as myFile:
        datashell = myFile.read()

    return datashell

if __name__ == "__main__":
    print(getOutput())

    while True:
        runCommand(input("")+"\n")
        print(getOutput())