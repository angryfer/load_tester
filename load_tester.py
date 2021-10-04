import requests
import threading


class LoadTester():
    def __init__(self):
        self.config = './config.json'
        self.ammo = 'ammo.txt'
        self.workers = 1
        self.time = 30
        self.rps = 10
        self.url = 'http://127.0.0.1:5000/four'

    def start(self):
        while True:
            response = requests.get(self.url)


if __name__ == '__main__':
    load = LoadTester()
    load.start()