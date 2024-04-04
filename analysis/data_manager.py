import pandas as pd
from pathlib import Path
from utils import get_csv_path, generate_name_with_timestamp
import logging

logger = logging.getLogger(__file__)


class DataManager:
    def __init__(
        self,
        path: Path,
    ) -> None:
        self.path = path

    def csv_converter(self) -> pd.DataFrame:
        self.df = pd.read_csv(self.path)
        return self.df

    def exclude_empty_columns(self) -> None:
        self.df = self.df.dropna(axis=1, how="all")

    @staticmethod
    def generate_new_csv(df: pd.DataFrame, filename: str) -> None:
        name: str = generate_name_with_timestamp(filename)
        df.to_csv(get_csv_path(name), index=False)
        logger.info(f"New csv file saved with name: {name}")
