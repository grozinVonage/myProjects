#!/usr/bin/python
import os
import threading
import time

# =========================================================


class MyThread(threading.Thread):

    def __init__(self, event, ui = None):
        threading.Thread.__init__(self)

        self.stop_event = event
        self.disconnect_interval = 0
        self.offline_time = 0
        self.daemon = True
        self.ui = ui
        self.is_connected = True

    # =========================================================
    def set(self, _disconnect_interval, _offline_time ):
        self.disconnect_interval = int(_disconnect_interval)
        self.offline_time = int(_offline_time)

    # =========================================================

    def run(self):
        print("Stared : %s" % time.ctime())
        while not self.stop_event.wait(self.disconnect_interval):
            self.do_disconnect()
            time.sleep(self.offline_time)
            self.do_connect()

    # =========================================================
    def do_connect(self):
        os.system("networksetup -setairportpower airport on")
        self.update_ui(True)
        print("Connected : %s" % time.ctime())

    # =========================================================
    def do_disconnect(self):
        os.system("networksetup -setairportpower airport off")
        self.update_ui(False)
        print("Disconnected : %s" % time.ctime())

    # =========================================================
    def update_ui(self ,status):
        if self.ui != None:
            self.ui.update(status)

