import logging
from pathlib import Path
from data_analysis import DataAnalysis
from utils import get_csv_path

logging.basicConfig(
    level=logging.WARNING,
    format=(
        "[%(asctime)s] %(levelname)s   %(message)s -  %(name)s:%(lineno)d"
    ),
    filemode="a",
    filename="./python_module.log",
)

logger = logging.getLogger(__file__)


if __name__ == "__main__":
    csv_path: Path = get_csv_path("dengue")
    analysis = DataAnalysis(csv_path)
