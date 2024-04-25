import logging
from pathlib import Path
from dengue_analysis import DengueAnalysis
from utils import get_csv_path
import seaborn

seaborn.set_theme()

logging.basicConfig(
    level=logging.INFO,
    format=(
        "[%(asctime)s] %(levelname)s   %(message)s -  %(name)s:%(lineno)d"
    ),
    filemode="a",
    filename="./python_module.log",
)

logger = logging.getLogger(__file__)


if __name__ == "__main__":
    csv_path: Path = get_csv_path("final_analysis")
    analysis = DengueAnalysis(csv_path)
    analysis.get_lowest_know_symptom(analysis.zona_sul)
