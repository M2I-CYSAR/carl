import socket
import struct
import threading

class OI:

    def __init__(self):
        thread = threading.Thread(target=self.threadRoutine).start()
        self.LJoystickXAxisRaw = 0
        self.LJoystickYAxisRaw = 0
        self.AButtonRaw = 0
        self.BButtonRaw = 0

    def threadRoutine(self):
        # Define the IP address and port number to listen on
        ip_address = "0.0.0.0"
        port = 4143

        # Create a TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the IP address and port
        s.bind((ip_address, port))

        # Listen for incoming connections
        s.listen()

        # Accept a connection
        conn, addr = s.accept()

        while True:
            # Receive data
            data = conn.recv(4)
            self.LJoystickXAxisRaw, self.LJoystickYAxisRaw, self.AButtonRaw, self.BButtonRaw = struct.unpack('bbbb', data)

        # Close the connection
        conn.close()

    def getLeftJoystickXAxis(self):
        return self.LJoystickXAxisRaw

    def getLeftJoystickYAxis(self):
        return self.LJoystickYAxisRaw

    def getAButtonPressed(self):
        return self.AButtonRaw

    def getBButtonPressed(self):
        return self.BButtonRaw
