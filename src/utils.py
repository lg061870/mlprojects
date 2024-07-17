import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('Xm_%d_XY_%H_XM_%S')}.log"
logs_path = os.path.join(os.getcwd(), 'logs', LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE = os.path.join(logs_path, LOG_FILE)

