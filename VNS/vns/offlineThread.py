#!/usr/bin/python
import os
import threading
import time
import vns.eventDispatcher

# =========================================================


class OfflineThread(threading.Thread):

    def __init__(self, ui = None):
        threading.Thread.__init__(self)

        self.offline_interval = 0
        self.daemon = False
        self.ui = ui


    # =========================================================

    def run(self, _offline_interval):
        print("Stared : %s" % time.ctime())
        self.offline_interval = int(_offline_interval)
        self.do_disconnect()
        time.sleep(self.offline_interval)
        self.update_ui()


    # =========================================================
    def do_disconnect(self):
        os.system("networksetup -setairportpower airport off")
        print("Disconnected : %s" % time.ctime())

    # =========================================================

    def update_ui(self):
        self.event_dispatcher.dispatch_event(
            vns.eventDispatcher.MyEvent(vns.eventDispatcher.MyEvent.DISCONNECTED, self))

