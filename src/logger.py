import logging
from datetime import datetime
import os
LOG_Flle = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOGS_PATH = os.path.join(os.getcwd(),"logs",LOG_Flle)

os.makedirs(LOGS_PATH,exist_ok=True)

LOGS_FILE_PATH = os.path.join(LOGS_PATH ,LOG_Flle)

logging.basicConfig(
    filename=LOGS_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)