import threading
import os
import sys

def launch_untitled():
    os.system('python untitled.py')

def launch_monitor():
    os.system('python monitor.py')

u = threading.Thread(target=launch_untitled)
m = threading.Thread(target=launch_monitor)


try:
    u.start()
    m.start()
    u.join()
    m.join()
except KeyboardInterrupt:
    sys.exit()