import logging
import os
from datetime import datetime

# Create a logs directory in the current working directory
logs_dir = os.path.join(os.getcwd(), 'logs')
os.makedirs(logs_dir, exist_ok=True)

# Generate a unique log filename
log_filename = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
log_filepath = os.path.join(logs_dir, log_filename)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    filename=log_filepath,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

if __name__ == '__main__':
    logging.info('Starting')