import logging
from pathlib import Path
from data_manager import DataManager
from dengue_analysis import DengueAnalysis
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
    csv_path: Path = get_csv_path("a3_renew_2024-04-03_20-23-48")
    data_manager = DataManager(csv_path)
    df = data_manager.csv_converter()
    dengue_analysis = DengueAnalysis(df)
    # dengue_analysis.relation_concern_measures()
    # dengue_analysis.relation_media_vaccine()
    # dengue_analysis.relation_treatment_salary()
    # dengue_analysis.relation_recidivism_age()
    # dengue_analysis.calculate_recidivism()
    # dengue_analysis.lesser_know_combat()
    # dengue_analysis.lesser_known_symptoms()
    # dengue_analysis.relation_symptoms_media()
    # dengue_analysis.relation_symptoms_schooling()
