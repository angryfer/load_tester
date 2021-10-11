import time

import requests


class Monitor:

    def __init__(self) -> None:
        self.requests_current = 0
        self.requests_all = 0

    def check_rps(self):
        start = self.requests_all
        time.sleep(1)
        diff = self.requests_all - start
        return diff
