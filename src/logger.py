import logging
import os 
import sys
from datetime import datetime
LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d')}.log"
LOG_DIR=os.path.join(os.getcwd(),"logs")
os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_PATH=os.path.join(LOG_DIR,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(levelname)s - %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)
if __name__=="__main__":
    logging.info("Logging has started")
    try:
        a=1/0
    except Exception as e:
        logging.error(e,exc_info=True)
        logging.info("Logging has ended")
        logging.info("Logging has ended")


    