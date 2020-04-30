import socket
import time

class Tello:
    def __init__(self):
        self.local_ip = '192.168.10.2'
        self.local_port = 8889
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # socket for sending cmd
        self.socket.bind((self.local_ip, self.local_port))

        self.tello_ip = '192.168.10.1'
        self.tello_port = 8889
        self.tello_adderss = (self.tello_ip, self.tello_port)
        self.log = []

        self.MAX_TIME_OUT = 15.0

    def send_command(self, command):
        self.socket.sendto(command.encode('utf-8'), self.tello_adderss)

    def initialize(self):
        self.send_command('command')

    def takeoff(self):
        self.send_command('takeoff')
    
    def land(self):
        self.send_command('land')
