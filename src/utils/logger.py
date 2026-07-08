import logging
import os
from datetime import datetime

os.makedirs("logs", exist_ok=True)

LOG_FILE = datetime.now().strftime("%Y%m%d_%H%M%S.log")

logging.basicConfig(
    filename=os.path.join("logs", LOG_FILE),
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s"
)

logger = logging.getLogger("TaxiFarePrediction")